"""Deterministic human review packets and bounded finding adjudication."""
from __future__ import annotations

import html
from pathlib import Path

from .roadmap_records import bindings_current, canonical, digest, require
from .security import confined_path


STAGES = ("classify", "requirements", "inspect", "challenge", "adjudicate", "deduplicate", "report")


def render_packet(root: Path, packet: dict) -> str:
    require(packet.get("schema") == 1, "unknown review packet schema")
    require(bindings_current(root, packet.get("inputs", [])), "review inputs missing or stale")
    pieces = ["<!doctype html><html lang='en'><meta charset='utf-8'>",
              "<meta http-equiv='Content-Security-Policy' content=\"default-src 'none'; style-src 'unsafe-inline'\">",
              "<title>Aegis proof review</title><style>body{font:16px system-ui;margin:2rem;max-width:90rem}pre{white-space:pre-wrap;background:#f3f5f7;padding:1rem}section{border-top:1px solid #ccc}code{overflow-wrap:anywhere}</style>",
              "<h1>Aegis proof review</h1><p>Review is separate from successful formal verification.</p>",
              f"<p>Packet identity: <code>{digest(packet)}</code></p>"]
    for binding in packet["inputs"]:
        path = confined_path(root, binding["path"], must_exist=True)
        content = path.read_text(encoding="utf-8")
        require(len(content.encode()) <= 1_000_000, "review source too large; prepare exact bounded source regions")
        pieces.append(f"<section><h2>{html.escape(binding['path'])}</h2><code>{binding['sha256']}</code><pre>{html.escape(content)}</pre></section>")
    for field in ("original_test", "semantics", "harness", "production_path", "assumptions", "bounds",
                  "assertions", "covers", "counterexamples", "changes", "outcomes"):
        pieces.append(f"<section><h2>{field}</h2><pre>{html.escape(canonical(packet.get(field, 'NOT_SUPPLIED')).decode())}</pre></section>")
    pieces.append("<p>Record a scoped decision through Aegis. This document cannot change verifier outcomes.</p></html>")
    return "\n".join(pieces)


def validate_decision(packet: dict, decision: dict) -> None:
    require(decision.get("schema") == 1, "unknown review decision schema")
    require(decision.get("packet_digest") == digest(packet), "review decision is stale")
    require(decision.get("decision") in {"approve_translation", "approve_classification", "request_repair", "human_intervention"}, "decision cannot grant proof credit")
    require(bool(decision.get("human")) and bool(decision.get("provenance"))
            and bool(decision.get("scope")), "scoped human provenance required")
    require(packet.get("review_scopes") and set(decision["scope"]) <= set(packet["review_scopes"]),
            "review decision extends outside the declared packet scope")


def advance_review(state: dict, stage: str, evidence: list[dict], *, campaign_authorized: bool) -> dict:
    require(campaign_authorized, "actual flaw-analysis campaign is deferred")
    require(state.get("schema") == 1, "unknown review state")
    history = state.get("stages", [])
    require(len(history) < len(STAGES) and STAGES[len(history)] == stage, "review stages must execute sequentially")
    require(bool(evidence), "review stage needs actual evidence")
    return dict(state, stages=[*history, {"stage": stage, "evidence": evidence}])


def adjudicate_findings(root: Path, findings: list[dict]) -> list[dict]:
    result = {}
    for finding in findings:
        require(finding.get("classification") in {"confirmed", "hypothesis"}, "finding classification required")
        require(all(finding.get(k) for k in ("requirement", "impact", "confidence", "repair")), "finding lacks actionable evidence")
        require(bindings_current(root, finding.get("sources", [])), "finding source is missing/stale")
        if finding["classification"] == "confirmed":
            require(bool(finding.get("demonstration")), "confirmed finding requires a demonstration")
        ident = digest({"requirement": finding["requirement"], "sources": finding["sources"],
                        "demonstration": finding.get("demonstration"), "impact": finding["impact"]})
        result.setdefault(ident, dict(finding, id=ident))
    return [result[k] for k in sorted(result)]
