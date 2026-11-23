# PvsNP — Lean 4 library of the P vs NP lab

- Toolchain: `leanprover/lean4:v4.36.0` (see `lean-toolchain`)
- Mathlib: tag `v4.36.0`, commit `fc4f59e577feb1a4956671bc04ac18aaaf8cd842` (pinned in `lake-manifest.json`)

Build (uses Mathlib's prebuilt cache; never compiles Mathlib from source):

    lake exe cache get && lake build

Audit (build + forbidden-token scan + per-module kernel replay), and axiom check:

    ../scripts/lean_audit.sh --replay
    ../scripts/print_axioms.sh PvsNP.sanity

Layout: `PvsNP/Statements/` (main-theorem statements; changes logged in `research/STATEMENT_LOG.md`),
`PvsNP/WIP/` (work in progress, may contain `sorry`, never imported by the root module).
Current contents: smoke test only. No research claims yet.
