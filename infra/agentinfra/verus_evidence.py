"""Pinned Verus VIR inventory; separate from Kani property classification.

An inventory identifies executed proof input. It cannot review the behavioral
adequacy of a theorem, or turn an external primitive contract into a proof.
"""
from pathlib import Path
import re
import shutil

from .destiny_reuse import digest, require
from .security import confined_path

SCHEMA = 1
MAX_VIR_BYTES = 6_000_000

def inventory(text, entry):
    require(isinstance(text, str) and len(text.encode()) <= MAX_VIR_BYTES, "incomplete or oversized Verus inventory")
    # This is the textual VIR format emitted by the pinned --log vir. Function
    # headers and bodies are separately identified; a nested CallTarget's
    # ':body None' does not mean its enclosing theorem has no body.
    require(re.search(r'\(arch_word_bits \(ArchWordBits (?:Either32Or64|Exactly \d+)\)\)\s*\Z', text),
            "missing VIR footer; incomplete inventory")
    prefix = Path(entry).stem + "::"
    checked, trusted, names = [], [], set()
    for block in re.split(r'(?m)(?=^\(@ )', text):
        header = re.match(r'^\(@ "([^"]+)" \(Function\s', block)
        if not header:
            continue
        name = re.search(r':name \(Fun :path ([^)]+)\)', block)
        require(name, "unrecognized pinned VIR Function name")
        if not name[1].startswith(prefix):
            continue
        mode = re.search(r':mode (Spec|Proof|Exec)\b', block)
        external = re.search(r':is_external_body (true|false)\b', block)
        body = re.search(r':is_async (?:true|false)\s*\)\s*:body (None|\(@@? "([^"]+)")', block)
        require(name and mode and external and body, "unrecognized pinned VIR Function header")
        require(name[1] not in names, "duplicate Verus symbol")
        names.add(name[1])
        flags = {flag: bool(re.search(r':' + flag + r' true\b', block)) for flag in
                 ('exec_assume_termination', 'exec_allows_no_decreases_clause')}
        row = {'symbol': name[1], 'mode': mode[1], 'declaration': header[1],
               'body': body[2], 'external_body': external[1] == 'true', 'flags': flags}
        if row['external_body']:
            trusted.append(row)
        elif row['mode'] in ('Proof', 'Exec'):
            require(row['body'] is not None, "nonexternal theorem/exec has no body")
            require(not any(flags.values()), "unchecked termination attributes require separate reviewed scope")
            require(not re.search(r'\b(?:verus_builtin|builtin)::(?:assume|admit)\b', block),
                    "local behavior uses an unchecked assumption")
            checked.append(row)
    require(checked, "empty Verus theorem/exec inventory")
    return {'schema': SCHEMA, 'entry': entry, 'checked': sorted(checked, key=lambda r:r['symbol']),
            'generated_trusted': sorted(trusted, key=lambda r:r['symbol']),
            'arch_word_bits': re.search(r'^\(arch_word_bits (.+)\)\s*$', text, re.M)[1]}

def log_path(root, argv):
    if '--log' not in argv or '--log-dir' not in argv:
        return None
    require(argv[argv.index('--log')+1] == 'vir', "reviewed Verus inventory requires --log vir")
    name = argv[argv.index('--log-dir')+1]
    require(name.startswith('.aegis/destiny/'), "Verus logs must be confined runtime artifacts")
    return confined_path(root, name + '/crate.vir')

def prepare_log(root, argv):
    path = log_path(root, argv)
    if path is not None:
        # Failures must never reuse a prior successful execution's VIR.
        path.unlink(missing_ok=True)

def capture(root, argv, run_id):
    path = log_path(root, argv)
    if path is None or not path.is_file():
        return None
    require(path.stat().st_size <= MAX_VIR_BYTES, "Verus VIR capture exceeds bound")
    parsed = inventory(path.read_text(), argv[-1])
    artifact = '.aegis/destiny/verus-artifacts/' + run_id + '.vir'
    target = confined_path(root, artifact)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, target)
    return {**parsed, 'artifact': artifact, 'artifact_sha256': digest(target.read_bytes())}

def current_inventory(root, receipt, obligation):
    from .evidence import proof_output
    from types import SimpleNamespace
    require(receipt['id'] == 'verus' and receipt['proof_output_checked'], "not a counted successful Verus observation")
    require(receipt['status']=='OBSERVED_SUCCESS' and receipt['returncode']==0, "failed Verus observation")
    require(receipt['identity']['obligation'] == {
        'method':'verus', 'entry':obligation['entry'], 'expected_checks':obligation['expected_checks']},
        "Verus entry/count differs")
    commands=receipt['commands']
    require(len(commands)==1 and [c['argv'] for c in commands]==receipt['identity']['commands'], "wrong/empty Verus command inventory")
    command=commands[0]
    require(command['returncode']==0 and not any(command[k] for k in ('timed_out','stdout_truncated','stderr_truncated')),
            "failed or incomplete Verus output")
    require(not set(command['argv']) & {'--no-verify','--verify-function','--verify-module','--verify-only-module'},
            "verification disabled or narrowed")
    require(proof_output(receipt['identity']['obligation'],SimpleNamespace(**command)), "zero/wrong/failed Verus result")
    value = receipt.get('verus_inventory')
    require(value and value['schema'] == SCHEMA and value['entry'] == obligation['entry'], "missing or wrong Verus inventory")
    artifact = confined_path(root, value['artifact'], must_exist=True)
    require(value['artifact'].startswith('.aegis/destiny/verus-artifacts/'), "inventory artifact escaped runtime state")
    require(digest(artifact.read_bytes()) == value['artifact_sha256'], "changed/incomplete VIR artifact")
    actual = inventory(artifact.read_text(), obligation['entry'])
    require(all(actual[key] == value[key] for key in actual), "recorded Verus symbols differ from actual VIR")
    require(len(actual['checked']) == obligation['expected_checks'] > 0, "unexpected theorem/exec inventory")
    return actual

def validate_symbol_mapping(actual, declared):
    require(declared['schema'] == SCHEMA and declared['entry'] == actual['entry'], "symbol mapping entry/schema differs")
    expected = {row['symbol']: row for row in actual['checked']}
    rows = declared['symbols']
    require(rows and len(rows) == len(expected) and len({r['symbol'] for r in rows}) == len(rows), "empty/wrong/duplicate symbol mapping")
    require({r['symbol'] for r in rows} == set(expected), "missing or unreferenced theorem/exec symbol")
    for row in rows:
        require(row['mode'] == expected[row['symbol']]['mode'], "mapped symbol mode differs")
        require(row['obligations'] and row['relation'].strip() and row['review'].strip(), "unreviewed symbol or missing semantic relation")
    return set(expected)

def validate_case_map(catalog, source_inventory, mapped):
    """Preserve qualified assertion/setup accounting without granting credit."""
    ids={row['id'] for row in catalog}
    require((len(catalog),len(ids),len({(r['source'],r['test']) for r in catalog}),
             len({r['source'] for r in catalog}))==(531,531,509,34), "catalog denominator differs")
    originals={row['id']:row for row in source_inventory['cases']}
    rows={row['id']:row for row in mapped['cases']}
    require(len(source_inventory['cases'])==len(originals)==len(mapped['cases'])==len(rows)==531,
            "omitted/duplicate qualified case")
    require(set(originals)==set(rows)==ids, "omitted or ambiguous qualified identity")
    require(mapped['original_commit']==source_inventory['original_commit']==catalog[0]['original_commit'], "original pin differs")
    groups=mapped['obligations']
    require(groups, "empty concurrency obligation inventory")
    for authority in catalog:
        row=rows[authority['id']];source=originals[authority['id']]
        require(row['original_source_sha256']==source['original_source_sha256']==authority['original_source_sha256'],
                "original hash differs")
        for lane,field in (('assertion','assertion_ids'),('dependency','dependency_ids')):
            mapped_sites=row[lane+'_mappings']
            require(row[field]==source[field] and len(mapped_sites)==len(source[field])
                    and {m['id'] for m in mapped_sites}==set(source[field]), "missing/ambiguous "+lane+" mapping")
        require(row['execution_obligation']['required'] is True and row['execution_obligation']['relation'].strip(),
                "missing setup/execution/no-unexpected-error obligation")
        requirements=row['required_obligations']
        require(len(requirements)==len(set(requirements)) and all(r in groups for r in requirements), "unknown/duplicate derived obligation")
        if row['concurrency_relevance']=='required_concurrency_obligation':
            require(requirements and row['applicability_rationale'].strip(), "missing required concurrency relation")
    return rows
