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
- 2026-11-23: Director stopped the 32-agent Stage 1 run (only 2 scouts had started, none finished; no files written).
  New standing rule: **≤4 agents per workflow run**, stages run as sequential small batches (CLAUDE.md updated).
- Director forwarded Williams' "Some Estimated Likelihoods" essay and his 23 Nov 2026 thread; lead's web search found
  the claimed Oct 2026 AI refutation of ETH (OpenAI + Anthropic, Lean-checked, under community review). Recorded in
  research/survey/00-director-sources.md. Stage 1 re-planned around it:
  - Batch 1: (X) ETH refutation — primary sources, exact claims, technique, status, consequences;
             (Y) algorithmic method & Boolean circuit lower bounds frontier (incl. range avoidance) — each + cross-check.
  - Batch 2: uniform lower bounds (L vs NP time–space, P vs PSPACE/QBF, Williams' 2025 time–space simulation) and the
             rest of the P = NP side; meta-complexity/magnification + barriers & failed attempts.
  - Batch 3: proof complexity + logic/independence + KRW/communication; algebraic complexity & GCT; formalization state.

## 2026-11-23 — Stage 1, batch 1 done (4 agents; ~1.85M subagent tokens; ~91 min)
- Surveys: `survey/01-eth-refutation.md` (681 lines), `survey/02-circuit-lower-bounds.md` (771 lines). Cross-checks in
  `reviews/survey-0{1,2}-*.crosscheck.md`: both "needs-corrections" (3 serious + 14 minor; 2 serious + 7 minor); no
  invented citations found; frontier tables largely confirmed at source.
- Key facts (survived cross-check): ETH refutation claims = #3-SAT in ~2^{n/√log n} (OpenAI, Anthropic, 16 Oct 2026),
  Lean-checked, no flaw reported, not certified by the Impagliazzo–Paturi–Williams review; SETH/NSETH fall with it;
  P vs NP untouched; consequence E^NP ⊄ SIZE(c·n·√log n) already stated by the authors. Circuit record: 3.1n − o(n)
  (Li–Yang 2022) peer-reviewed; 4n claimed (Mishra–Santhanam preprint, 3 Nov 2026); 4n − 9d affine dispersers in Lean.
- **Novelty-gate hits (work we would otherwise have duplicated):**
  1. cslib-frontier (verified by cloning) already formalizes P, NP, Cook–Levin, 3SAT, Baker–Gill–Solovay, ¬ETH and many
     circuit lower bounds ⇒ mission item 4 is not novel; formalization track re-scoped (DIRECTIONS.md).
  2. Survey 02's top-ranked problem (Lean ETH ⇒ E^NP bound) is cslib-frontier issue #1539, in active progress.
  3. Survey 01's O3 (2^{o(n)} IPS refutations) claimed solved in Lean by Szeider (Zenodo, 16–17 Nov 2026), char ≠ 2.
  4. Survey 01's O2 ("better pieces", ρ < 1/√2) is capped at ρ ≥ 1/2 by a rank argument (cross-checker) ⇒ at best
     E^NP ⊄ SIZE(c·n·log n); route via Hrubeš/Naslund cannot beat 1/√2.
- Landscape lesson: 2026 complexity theory is crowded with AI-driven efforts (OpenAI, Anthropic, cslib-frontier, many
  AI-assisted preprints). Directions must be checked against live public work, not just published papers.
- Ledgers: KNOWN_RESULTS.md and BIB.md updated (mechanical merge of survey sections + cslib-frontier entry).
- Next: batch 2 (4 agents): (03) uniform lower bounds — L vs NP time–space, P vs PSPACE/QBF, Williams' √t-space
  simulation & tree evaluation, post-ETH fine-grained landscape; (04) meta-complexity/magnification + barriers & failed
  attempts. Every scout must also check cslib-frontier and Oct–Nov 2026 AI-produced results.
- Frontier watch added (`scripts/frontier_watch.py`, no agents): first run 2026-11-23 → 530 new items, 28 flagged,
  400 cslib-frontier commits in the last 7 days (~57/day). arXiv API was rate-limited and ECCC unreachable from the
  sandbox; RSS + listing pages work. Watch protocol written into CLAUDE.md.
- Mistake + fix: re-launched the batch-1 script by accident while starting batch 2; stopped within seconds, no files
  changed (git clean). Batches now use a parameterized script (`stage1-survey-batch`, areas passed as args, ≤2 areas).
- Competitor noted (director, 2026-11-23): pequalnp.com — a public, livestreamed AI agent fleet (by "Brilliant",
  brilliant.design) attacking P vs NP with Lean-checked lemmas, programs aimed at both P ≠ NP and P = NP, and a public
  "graveyard" of refuted approaches. Its Atom feed (https://pequalnp.com/feed.atom) is now in the frontier watch. As of
  today it is grinding many small conjectural lemmas (e.g. L-meta-133, L-gct-179). Their lemma record and graveyard are
  prior art for our novelty gate.
