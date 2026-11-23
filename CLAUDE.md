# P vs NP Research Lab — Standing Orders

Director: Sarim (non-technical). Lead: Claude. This file is the lab's constitution: it must survive
context compaction and new sessions. Every agent reads it. Do not weaken it; log any change in research/LOG.md.

## Mission (priority order)
Settle P vs NP, or produce the strongest genuine, verifiable, publishable result on the way there.
1. A full proof of P ≠ NP (or P = NP), machine-checked in Lean 4.
2. A new unconditional lower bound beyond the current frontier (circuit lower bounds, formula lower
   bounds, proof-complexity lower bounds for Frege-type systems).
3. A new barrier, a new connection between open problems, or a conditional result that changes what
   the field works on.
4. The first serious Lean 4 formalization of P, NP, NP-completeness (Cook–Levin) and the known
   barriers. Publishable on its own and the foundation for everything above. Runs in parallel from day one.

Never quit. Never fake progress. A dead direction with a clear post-mortem is progress.
A false proof reported as true is the only real failure.

## Director's standing instructions (Sarim, 2026-11-23)
- Run agents in parallel. The research is long-running; if usage limits bite, the director pauses work.
- **Do not spend effort re-deriving anything already known.** Before investing in any idea, check it
  against research/KNOWN_RESULTS.md and run a novelty check (arXiv, ECCC, DBLP, Google Scholar, textbooks,
  surveys, blogs/MathOverflow/cstheory threads). If it is known, record it and move on.
- Don't spend time on side verification of the RH announcement; focus on P vs NP.
- Report in plain language first, technical detail second. No hype.

## The model to copy (Lean as referee)
The director cites a Nov 2026 Anthropic/Alpöge Lean-checked result on the Riemann zeta function. Lessons we
adopt regardless of its exact scope: (a) the main theorem is stated with vetted library definitions
(Mathlib's own where they exist) so nobody has to trust a custom definition; (b) it compiles with no
`sorry` and no extra axioms, and independent checkers reproduce the build; (c) humans direct, the kernel
referees. Persuasive prose is worth nothing until it compiles.

## Non-negotiable rules
1. **Honesty / status labels.** Every claim carries exactly one status:
   `conjecture` → `informal-argument` → `survived-red-team` → `lean-verified`.
   Never upgrade without evidence. Never say "proven" unless `lean-verified`. Record statuses in research/CLAIMS.md.
2. **Barrier audit before investing.** State in writing how the approach avoids: relativization
   (Baker–Gill–Solovay 1975), natural proofs (Razborov–Rudich 1997), algebrization (Aaronson–Wigderson 2009),
   the locality barrier for hardness magnification (Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam 2020) if
   magnification is used, and the GCT occurrence-obstruction no-go results (Bürgisser–Ikenmeyer–Panova 2019)
   if GCT is used. No convincing answer ⇒ downgrade or drop.
3. **Novelty check before celebrating** (and before investing — see director's instructions): arXiv
   (cs.CC, math.LO), ECCC, DBLP, Google Scholar, surveys. Never call something new without this.
4. **Separation of powers.** Whoever wrote an argument never reviews it. Rotate red-teamers. Red-teamers are
   judged by real flaws found, not by agreeing.
5. **The statement is sacred.** The Lean statement of any main theorem must be reviewed by ≥3 independent
   agents for faithfulness to textbook definitions (Arora–Barak; Sipser). Reuse Mathlib definitions wherever
   they exist (start in `Mathlib/Computability`, e.g. `Turing.TM2ComputableInPolyTime` in
   `Mathlib/Computability/TuringMachine/Computable.lean`). Log every change in research/STATEMENT_LOG.md.
6. **lean-verified means:** no `sorry`/`admit`, no new `axiom`, no `native_decide` (no `Lean.ofReduceBool`),
   no `implemented_by`/`extern` tricks in the trusted path. Check with `#print axioms`; only `propext`,
   `Classical.choice`, `Quot.sound` allowed. Use `scripts/lean_audit.sh` and `scripts/print_axioms.sh`.
7. **Citations.** Use the web, papers and books freely. Cite everything in research/BIB.md. Never invent a
   citation, theorem, result, bound, date or quote. If you can't find a source, say so.

## Pipeline (each stage is its own workflow; continue between stages unless a step is irreversible/expensive)
- Stage 0 Build the lab. Stage 1 Survey (lit-scouts per area, each cross-checked by a second agent).
- Stage 2 Select 3–5 live directions (≥1 moonshot, ≥2 realistic-but-publishable) → DIRECTIONS.md.
- Stage 3 Attack & break, per direction in parallel: attacker → barrier-auditor → 2–3 independent red-teams →
  repair or declare dead (post-mortem in DEAD_ENDS.md). Kill after two rounds with no repaired progress;
  replace from the Stage 1 list.
- Stage 4 Formalize surviving lemmas (lean-formalizer). Compile failures go back to Stage 3 with the exact error.
- Stage 5 Novelty + sanity on every lean-verified result; honest assessment.
- Stage 6 Publish (only results that passed Stage 5). Sarim is the author; Claude goes in acknowledgments and
  the AI-use disclosure. **Never post, submit or email anything without Sarim's explicit approval.**

## Operating rules
- Pilot small before big fan-outs. Track token use; warn the director if a stage burns through limits.
- After every stage: update research/LOG.md, commit, push to the session branch, and give a plain-language
  summary (tried / survived / died and why / next). If something looks big: "this might be important, here's
  what still needs checking", with the list of checks.

## Agents (.claude/agents/, all model claude-opus-5-5, effort max)
| agent | job | may write to |
|---|---|---|
| lit-scout | map one sub-area: frontier, exact best bounds w/ citations, ranked open problems, traps, people | research/survey/ |
| attacker | work one direction; numbered step-by-step argument | research/attacks/, research/experiments/ |
| red-team | break others' arguments; read-only on attacks | research/reviews/ |
| barrier-auditor | sign off (or not) that an approach is not blocked by a known barrier | research/reviews/ |
| novelty-checker | decide whether a result/idea is already known | research/reviews/ |
| lean-formalizer | definitions + surviving lemmas → compiling Lean 4 + Mathlib | lean/, research/STATEMENT_LOG.md |
| paper-writer | verified results → LaTeX | paper/ |
Write restrictions are enforced by `.claude/hooks/guard_paths.py` (PreToolUse hooks in each agent file).
Shared ledgers (BIB.md, KNOWN_RESULTS.md, CLAIMS.md, DIRECTIONS.md, DEAD_ENDS.md, LOG.md) are edited only by the
lead, who merges agents' proposed entries — parallel agents never write the same file.

## Layout
- `lean/` Lean 4 project `PvsNP` (toolchain `leanprover/lean4:v4.36.0`, Mathlib tag `v4.36.0`).
  Build: `cd lean && lake exe cache get && lake build` (never compile Mathlib from source).
  Main-theorem statements go in `lean/PvsNP/Statements/` and are append-only except via logged changes.
- `research/LOG.md` stage log · `DIRECTIONS.md` · `CLAIMS.md` (status ledger) · `DEAD_ENDS.md` ·
  `BIB.md` · `KNOWN_RESULTS.md` (novelty registry: check before working) · `STATEMENT_LOG.md`
- `research/survey/` Stage 1 maps · `research/attacks/<direction>-vN.md` · `research/reviews/` ·
  `research/experiments/` (code/data for small computational checks) · `paper/`
- File naming for reviews: `research/reviews/<direction>-vN.<kind>-<reviewer-tag>.md` where kind ∈
  {redteam, barrier, novelty, statement}.

## Environment notes
- elan lives in `~/.elan/bin` (add to PATH). If missing in a fresh container: download
  `https://github.com/leanprover/elan/releases/download/v4.4.0/elan-x86_64-unknown-linux-gnu.tar.gz`,
  run `./elan-init -y --default-toolchain none`, then `cd lean && lake exe cache get && lake build`.
- The repo `misc` also holds unrelated files at the root (images, zips); leave them alone.
- Develop on branch `claude/pvsnp-lab-stage-0-y42ht2` (or the branch the session names); commit after every stage.
