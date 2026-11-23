# Lab log

Newest entries at the bottom. Each stage entry: what was tried, what survived, what died and why, what's next,
token/limit notes.

## 2026-11-23 — Stage 0: build the lab
- Lab constitution written: `CLAUDE.md` (mission, rules, pipeline, director's standing instructions).
- Seven agents in `.claude/agents/` (lit-scout, attacker, red-team, barrier-auditor, novelty-checker,
  lean-formalizer, paper-writer), all `model: claude-opus-5-5`, `effort: max`. Write access mechanically
  restricted per agent by `.claude/hooks/guard_paths.py` (red-team/barrier-auditor/novelty-checker cannot touch
  attack files; tested).
- Lean: elan 4.4.0; project `lean/` (`PvsNP`), toolchain `leanprover/lean4:v4.36.0`, Mathlib tag `v4.36.0`
  (commit fc4f59e577feb1a4956671bc04ac18aaaf8cd842); `lake exe cache get` pulled 9117 prebuilt files; `lake build`
  succeeds; `#print axioms` pipeline works.
- Mathlib observation: Mathlib v4.36.0 has Turing machines and `Turing.TM2ComputableInPolyTime`
  (`Mathlib/Computability/TuringMachine/Computable.lean`) but no definitions of the classes P, NP, polynomial-time
  reductions, or NP-completeness (grep for `InPolyTime` finds only that file). Formalization track starts there.
- RH "model to copy": a short check found Anthropic's published Nov-2026-era work to be a Lean-checked result about
  zeros of the zeta function rather than RH itself (status: unverified quick search; director asked not to spend
  more time on it). The methodology lessons are adopted regardless (CLAUDE.md "The model to copy").
- Director instructions recorded: parallel agents; hard novelty gate before investing in any idea; focus on P vs NP.
- Next: Stage 1 survey workflow (9 lit-scouts + independent cross-checkers, in parallel).
- Pilot (before Stage 1 fan-out): agent roles created mid-session are not registered until the next session
  (`agent type 'red-team' not found`). For this session, workflow agents read their role file from
  `.claude/agents/<role>.md` and run at effort max; the frontmatter write-guards only take effect from the next
  session, so the lead audits each stage's writes with `git status`/`git diff --stat` against each agent's
  allowed paths.

## 2026-11-23 — Stage 1: survey (started)
- Workflow `stage1-survey` launched: 10 areas (circuit lower bounds; magnification & meta-complexity; proof
  complexity; algebraic complexity & GCT; communication complexity & KRW; range avoidance; logic & independence;
  the P = NP side; formalization state; barriers & failed attempts). Per area: lit-scout → independent
  cross-checker (bounds re-verified at source; 2023–2026 search for solved "open" problems) → scout applies
  verified corrections. Then single-writer merge into KNOWN_RESULTS.md / BIB.md and a completeness critic.
  32 agents at effort max.
