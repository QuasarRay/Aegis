# Formal Verification for Python: Tools and Approaches

**Executive Summary:** Formal verification of Python code is harder than for statically-typed languages, but recent tools have emerged. Most approaches either restrict Python (typed subsets, limited features) or *translate* Python into another verification framework. The strongest tools today include:

- **Nagini:** An automated *deductive verifier* for (concurrent) Python, based on the Viper infrastructure. Nagini supports a rich subset of statically-typed Python 3 and a contract language for pre/postconditions and loop invariants. It even lets you specify **input/output relations**, progress properties, and information-flow policies. Nagini aims to prove complex safety and correctness properties of real-world code.
- **ESBMC-Python (BMCPython):** An SMT-based *bounded model checker*. It infers types, translates Python to an intermediate form (and then to SMT), and uses the ESBMC engine to check assertions. In one report it found a “real problem in the Ethereum Consensus Specification”. This is essentially the first full-model-checking tool for Python code.
- **PyVeritas:** An **LLM-augmented** pipeline. An LLM (e.g. GPT-4) transpiles Python to C, and then the CBMC C model checker verifies assertions. Early results (2025) show high correctness (80–90% accurate transpilation on small benchmarks), enabling existing C model checking tools to apply to Python logic. This is a novel approach that leverages mature C verification tech.
- **Dafny-of-Python:** A *deductive verifier* that translates Python (with type hints) into [Dafny](https://dafny.org/) code. Users write specs as comments (e.g. `# post ...`); the tool emits a Dafny function with an `ensures` clause and invokes Z3. For example, annotating
  ```python
  # post res == x*x*x
  def cube(x: int) -> int:
      return x
  ```
  produces a Dafny function with `ensures (res == x*x*x)` that is then checked. Passing the Dafny proof implies the Python spec holds.
- **CrossHair:** A *symbolic execution* tool. Given Python 3.9+ code with type annotations and a (Pythonic) contract, CrossHair repeatedly invokes the code with symbolic inputs and uses an SMT solver to try to find counterexamples. It “blurs the line between testing and type systems”. In practice it finds bugs efficiently, but it does **not** guarantee full proof (it is essentially a smart fuzzer/analysis).
- **Others:** Smaller tools or libraries (e.g. Why3-py for statistics, micro-Python front-end to Why3) exist but have narrow scope. Traditional static checkers (Mypy, Pyre) and property-testers (Hypothesis) help code quality, but are not formal verifiers.

Each approach has trade-offs. Nagini and Dafny-of-Python perform *full deductive verification* but require manual annotations (loop invariants, types, contracts). Bounded model checkers (ESBMC-Python, PyVeritas) are more automated for finding bugs but only give *bounded* guarantees. CrossHair is easy to use but incomplete. In the sections below we compare these tools and suggest recommended workflows.

## Comparative Analysis

| Tool            | Approach            | Specs & Language                                              | Automation / Solver           | I/O Spec Support                 | Maturity / Integration                                  | Pros / Cons                            |
|-----------------|---------------------|---------------------------------------------------------------|------------------------------|-----------------------------------|--------------------------------------------------------|----------------------------------------|
| **Nagini**      | Deductive (Viper)   | Python *contracts* (`Requires(a)`, `Ensures(a)`) in code | Fully automated (SMT via Viper/Boogie) | **Yes**: can express input/output relations and progress | Research tool (ETH Zurich). VSCode plugin and Docker available. Requires Python 3.12–3.14 and type hints. | + Very expressive (I/O specs, concurrency). Provides proofs. – High annotation burden; only static subset. |
| **ESBMC-Python**| Bounded MC (SMT)    | Python with type hints; handles arithmetic, arrays, etc. | Automated (SMT via ESBMC)     | *Limited*: only checks asserts or C-like contracts | Academic (ISSTA 2024). Built on mature ESBMC (ANSI-C checker). No IDE plugin yet. | + Automatic type inference; catches many bugs. – Only bounded checking; no high-level specs; might miss deep bugs. |
| **PyVeritas**   | Bounded MC (SMT)    | Assertions in Python; transpiled to C (via LLM) | Automated (LLM + CBMC)        | *No*: only assertion checking | Experimental (2025). Leverages existing CBMC/SMT. Relies on external LLM. | + Leverages powerful C tools; partially automated. – Transpilation errors; small-scale; not formal proof (only bounded). |
| **Dafny-of-Python** | Deductive (Dafny) | Python type annotations + `# pre/post` comments | Automated (Z3 via Dafny)     | *No*: focuses on functional contracts | Prototype (NUS 2020). Built on Dune (OCaml). Command-line only. | + Clean specification syntax; modular proofs. – Limited Python subset; requires external Dafny knowledge; slower to set up. |
| **CrossHair**   | Symbolic Execution  | Python 3.9+ type hints + contracts in docstrings/asserts | Partially automated (SMT)    | *No*: only verifies specified contracts | Mature (pip package). IDE support (VSCode, PyCharm). Works on real Python. | + Very easy to run (no compilation). Great for finding counterexamples. – Not a prover; can miss issues or report false alarms; loop support limited. |

- **Automation:** Nagini and Dafny-of-Python perform full proof search (via SMT solvers), but require rich annotations. ESBMC-Python/PyVeritas automate translation but only check bugs up to a bound. CrossHair automates symbolic tests but isn’t sound.
- **Specification Languages:** Nagini uses its Python `nagini_contracts` library (e.g. `Requires(x>0); Ensures(Result()>0)` at function entry). Dafny-of-Python uses `# pre ...` and `# post ...` in comments. ESBMC and PyVeritas rely on in-code `assert` or Python `if` for assumptions. CrossHair supports function annotations and `assert`/docstring contracts.
- **I/O Relations:** Nagini is unique in supporting **explicit I/O specifications** derived from, e.g., Isabelle/HOL models. ESBMC/PyVeritas check stateful behavior only via asserts. 
- **Use Cases:** Nagini has been used to verify protocol implementations, router code, and security properties. ESBMC-Python demonstrated finding an Ethereum bug. Dafny-of-Python and PyVeritas are relatively new (proof-of-concept). CrossHair is widely used for small to medium Python libraries.

## Comparative Table of Features

| Feature                    | Nagini                     | ESBMC-Python               | PyVeritas                       | Dafny-of-Python              | CrossHair                 |
|----------------------------|----------------------------|----------------------------|---------------------------------|-----------------------------|---------------------------|
| **Specification Style**    | Python contracts via `Requires`/`Ensures` | Type-annotated Python; mostly internal logic checks (asserts) | Python asserts + any code; uses LLM to C | Python comment specs (`# pre/post`) | Type hints + Pythonic contracts (assert/docstring) |
| **SMT/Prover Backend**     | Viper/Boogie (Z3)          | ESBMC (Z3)                 | CBMC (Yices/other)               | Dafny (Z3)                  | Z3 via symbolic engine    |
| **Counterexamples**        | Yes (counterexample if spec fails) | Yes (bounded trace)        | Yes (via CBMC)                  | Yes (refined to Python positions) | Yes (SMT-generated)      |
| **LTL/CTL Model Checking** | No (mostly sequential)     | No (no temporal logic)     | No                              | No                          | No                        |
| **Concurrency**            | Yes (handles threads/semaphores) | Limited (focused on sequential) | N/A (transpiler focus) | No (single-threaded) | No                        |
| **Scaling**                | Moderate (handles non-trivial code with specs) | Medium (bounded loops/unrolls) | Small (proof-of-concept examples) | Small-medium (educational) | Small (local routines)    |
| **CI/CD Integration**      | Via CLI or VSCode plugin | Custom scripts (ESBMC CLI) | No standard pipeline yet      | CLI with Dune (possible via scripts) | Runs in dev environment (watch mode) |
| **License/Cost**           | Open-source (MPL 2.0)      | Research (likely open; based on ESBMC) | Research (arXiv)            | Open (GitHub)               | Open-source (MIT)         |

## Recommended Tools and Workflows

**Best Single Tool:** *Nagini* is generally the strongest verifier for Python if you can constrain your code to its supported subset. It has a powerful specification language (including I/O behavior) and proven success on real code. However, it requires thorough static typing and specifications. If your project can afford writing these annotations, Nagini can provide full proofs of correctness.

**Best Practical Toolchain:** In practice, no one tool covers everything. A practical workflow might combine tools:

- **Static Contracts & Deductive Check (Nagini or Dafny-of-Python):** Use Nagini on critical modules. Write Python type hints and `Requires/Ensures` contracts. Run `nagini` (or use the Docker) to verify them. For other parts of code (e.g. algorithmic functions), you can use Dafny-of-Python by writing specs in comments.
- **Property Testing (Hypothesis) and Symbolic Testing (CrossHair):** Complement with Hypothesis to test properties automatically, and use CrossHair (`pip install crosshair-tool` and `crosshair watch .`) to catch counterexamples in code.
- **Bounded Model Checking:** For deep bug-finding, use ESBMC-Python on code by annotating types. It can automatically check for overflow, out-of-bounds, etc. Alternatively, try PyVeritas to translate smaller functions to C and run CBMC for assertion checking.
- **Integration:** Automate verification in CI by running these tools on a clean checkout. Nagini has a Docker image (e.g. `docker run --rm -v $(pwd):/code ghcr.io/bigtalk-org/docker-nagini module.py`). ESBMC-Python and Dafny-of-Python have CLI modes. CrossHair can be run on demand in dev mode.

**Example Workflow (Nagini):**

1. **Write code with specs:** Annotate functions with types and Nagini contracts. For example:
   ```python
   from nagini_contracts.contracts import *

   def max_list(l: list[int]) -> int:
       Requires(len(l) > 0)
       Ensures(all(x <= Result() for x in l))
       m = l[0]
       for x in l:
           if x > m:
               m = x
       return m
   ```
2. **Run verifier:** Execute Nagini. Using Docker (no install needed):
   ```bash
   docker run --rm -v $(pwd):/code ghcr.io/bigtalk-org/docker-nagini max_list.py
   ```
   Nagini will attempt to prove the postcondition; if it fails, it reports a counterexample path (lines/conditions).
3. **Interpret results:** A “no errors” result means the spec holds (up to the verifier’s logic). If there’s an error, inspect the counterexample to fix the code or strengthen the spec.

**Example Workflow (Dafny-of-Python):**

1. **Write specs in comments:** For example, in `cube.py`:
   ```python
   # post res == x*x*x
   def cube(x: int) -> int:
       return x
   ```
2. **Run verifier:** Assuming Dafny-of-Python is installed (via Dune):
   ```bash
   dune exec src/bin/main.exe < cube.py
   ```
   It will generate a Dafny file and attempt to verify it. Output points to Python source lines. A success means the postcondition is proven.
3. **Refine:** If there are errors (“postcondition might not hold”), adjust the code or spec and rerun.

**Example Workflow (CrossHair):**

1. **Write a contract:** For example, in `sorter.py`:
   ```python
   def sort_nums(xs: list[int]) -> list[int]:
       """Returns a sorted list with the same elements."""
       # (no explicit contract here; CrossHair infers from context or docstring)
       return sorted(xs)
   ```
2. **Install and run CrossHair:** 
   ```bash
   pip install crosshair-tool
   crosshair watch sorter.py
   ```
   CrossHair will symbolically run `sort_nums` and check if any assertion or contract is violated. It reports counterexamples if found.
3. **Use results:** Fix any found counterexamples or add explicit assertions if needed.

```mermaid
flowchart LR
    A[Write Python code + specs] --> B[Translator/Parser (Nagini/Dafny/...)]
    B --> C[Invoke SMT/Model Checker]
    C --> D{Spec holds?}
    D -- Yes --> E[Success: Verified]
    D -- No --> F[Counterexample/Error Trace]
```

## Example Commands and Snippets

- **Nagini (Docker):**  
  ```bash
  # Verify a file without installing locally:
  docker run --rm -v $(pwd):/code ghcr.io/bigtalk-org/docker-nagini my_module.py
  ```  
  Nagini will analyze `my_module.py` and report any spec violations.

- **Dafny-of-Python:**  
  ```bash
  dune exec src/bin/main.exe < example.py
  ```  
  This translates `example.py` (with `# post` specs) to Dafny and invokes the verifier.

- **CrossHair:**  
  ```bash
  pip install crosshair-tool
  crosshair watch path/to/code
  ```  
  Monitors the code and checks annotated functions for counterexamples.

- **ESBMC-Python:** (work in progress) – after installing and annotating types, run  
  ```bash
  esbmc-python myscript.py
  ```  
  (CLI will perform a bounded model check on `myscript.py`.)

- **PyVeritas:** Use the provided scripts (e.g. a Python wrapper) to transpile and then run CBMC on the result (details in the PyVeritas paper).

## Verification Plan for a Sample End-to-End Spec

Suppose we have a Python function for a simple application (e.g. a string-to-number converter or a state machine) and we want to verify its overall behavior from input to output. A plan might be:

1. **Specify the E2E behavior in logical terms.** For example: “For any input `s: str` that is a decimal string, `int_parser(s)` returns an integer equal to the parsed value, or raises `ValueError` if `s` is not a valid decimal.” Express this as preconditions/postconditions.
2. **Annotate the code with types and specs.** If using Nagini, add `Requires(...)` and `Ensures(...)` to functions. If using Dafny-of-Python, add `# pre ...` and `# post ...` comments. For example, for a decimal parser:
   ```python
   # pre all(c.isdigit() for c in s)  # input must be digits
   # post Result() == int(s)
   def parse_int(s: str) -> int:
       ...
   ```
3. **Run the chosen tool.** E.g., run Nagini or Dafny-of-Python on the module. The tool will attempt to prove the postcondition for all inputs satisfying the precondition.
4. **Analyze output.** If verification fails, examine the counterexample or failure: perhaps the code or spec is wrong (e.g. forgot to handle negative numbers). Fix and repeat.
5. **Iterate and refine.** Continue until the tool (semi-automatically) discharges all proof obligations under the spec. 

Throughout, integrate these checks into development: e.g., run Nagini in CI after type-checking, or use CrossHair during development to catch quick bugs. The goal is to ensure the Python application meets its formal end-to-end spec. 

## References

- Eilers and Müller, *Nagini: A Static Verifier for Python* (CAV 2018) – Nagini overview.  
- Farias et al., *ESBMC-Python: A Bounded Model Checker for Python* (ISSTA 2024) – ESBMC-Python intro.  
- Orvalho & Kwiatkowska, *PyVeritas: …Transpilation and BMC for C* (arXiv 2025).  
- Choudhury & Cheema, *Dafny-of-Python* (2020) – GitHub tool description.  
- Schanely, *CrossHair documentation*; *CrossHair PyPI page*.  
- Why3-py paper (Tanaka & Kawamoto 2026) – survey of Python verification tools.  
- Nagini Wiki (specification language).  
- EthZ Nagini project page and publications. (Sources cited inline.)