# Cross-check of survey 02 "circuit-lower-bounds"

- Target: `research/survey/02-circuit-lower-bounds.md` (772 lines, read in full).
- Reviewer: independent red-team cross-checker. I did not write the survey. Date 2026-11-23. Single agent, no sub-agents.
- Method: I opened primary sources with WebFetch (ECCC report pages and PDFs, arXiv abstracts, GitHub issues/PRs, Williams' PDFs) and
  ran targeted web searches. I listed every ECCC 2026 report (TR26-001 to TR26-336) and the arXiv cs.CC listings for Oct and Nov 2026.
  Each item below names what I opened.
- Labels: VALID / INVALID / GAP / UNCHECKED-CITATION per row. Severity: FATAL / SERIOUS / MINOR. My own reasoning carries the
  CLAUDE.md label `informal-argument` (reviewer).

---

## 0. Plain-language summary

**Verdict: DAMAGED-REPAIRABLE** (structured verdict: needs-corrections).

1. **The numbers are mostly right.** I opened about 45 frontier rows and key quotes at source, and almost all match. They include
   the headline 4n − O(log n) bound and its AI disclosure, the THR∘THR n^{2.5−ε} bound, the 2026 AC0 "parity barrier" results, and
   the Williams and Murray–Williams quotes about E^NP and linear-size circuits.
2. **One omission changes what the lab should do next (SERIOUS).** The survey missed **cslib-frontier**, a large public Lean 4
   project built on CSLib. It is AI-assisted and was renamed from Complexitylib on 8 Nov 2026. It already contains Lean proofs of
   gate-elimination lower bounds for general fan-in-2 circuits (including the new 4n bound), Håstad, Razborov–Smolensky and
   Kannan's theorem. It also has an open issue, started 28 Oct 2026, to formalize exactly the survey's **#1-ranked** problem.
   - So **rank 3 is essentially done**, and **rank 1 is being worked on in public right now**.
   - The survey's formalization section (§8) says "none found". That is wrong.
3. **One listed bound moved.** The survey's "precisely 4n − 10d" is now **4n − 9d** in Lean (cslib-frontier PR #7449, merged
   22 Nov 2026). Only AI agents reviewed it. The leading constant 4 is unchanged.
4. **Some tractability scores are too optimistic.**
   - Rank 4: as worded, it asks the lab to refute a widely believed conjecture.
   - Rank 9 is too high.
   - Rank 2 is arguably too high.
5. **Smaller problems:** 7 minor errors (a misquoted bound, an internal inconsistency, a wrong venue, an attribution slip, two
   overstatements, bibliography gaps) and 14 missing items.

**Nothing I found settles any of the big open problems in §5.** That covers NP ⊄ ACC0, explicit rigid matrices, KRW / n^{3+ε}
formulas, depth-3 2^{n^{1/2+ε}}, THR∘THR beyond n^{2.5}, monotone exp(n^{1−ε}), NC0_3-Avoid, fixed-polynomial bounds for NP or
P^NP, E^NP ⊄ SIZE[2^{εn}], and Williams' L^{1.01} challenge.

---

## 1. What the survey claims, and whether it is well-defined

- The survey covers general fan-in-2 circuits (B2 and U2), formulas, AC0, AC0[p], ACC0, threshold circuits, monotone circuits,
  Kannan-type and near-maximum bounds, range avoidance, rigidity, magnification and barriers. It also has a section on Williams'
  23 Nov 2026 challenge and on the Oct-2026 ETH refutation.
- The model definitions match the standard ones. In particular:
  - B2 = all 16 binary gates. U2 = B2 minus XOR/XNOR, which with free negations is the De Morgan basis.
  - "Size" means the number of gates unless a row says wires.
  - "Explicit" is used for P or NP functions, and the E^NP / S2E / AMEXP rows are kept apart from explicit functions.
  - The i.o./a.e. qualifiers I spot-checked are right: K12 "S2E ⊄ i.o.-SIZE[2^n/n]" is an a.e. bound; §4.5's E^NP bound is i.o.;
    T2 is a.e.
- The `checked: yes/no` convention is honest. Every row I opened that was marked `checked: yes` matched its source.

---

## 2. Row-by-row verification (what I opened)

| Row / claim | Source I opened | Verdict |
|---|---|---|
| G1 | ECCC TR26-260 page; rev. 1 PDF pp. 1–13 | **VALID.** Thm 1.1, and "4n − 10d" on p. 10. §1.6: "the proof of the main result was elicited from AI tools". §1.6: "close to the limit of what can be achieved using gate elimination". §1.5: "currently unknown if affine dispersers are computable by B2 circuits in linear size". §1.3: "we currently do not have non-trivial satisfiability algorithms even for linear-size circuits". The **additive term is superseded** (§4, S-1). |
| G1a | ECCC page and revision note | VALID |
| G2–G10, G12 | MS26 rev. 1 §1.3, pp. 3–6 (secondary, as the survey says) | VALID as secondary. Kloss–Malyshev Σx_ix_j; Schnorr Mod3 2n; Stockmeyer 2.5n−3; Mod3 has 3n+O(1) circuits; Blum 3n; Iwama–Morizumi 5n−o(n); Lachish–Raz 4.5n; Amano–Tarui; Chen–Kabanets 2.5n; GKST 2.99n; FGHK 3.11n for quadratic dispersers. |
| G11 | arXiv 2604.23958 and 2602.17942 abstracts | VALID |
| G13 | ECCC TR24-086 | VALID |
| GL1, GL3 | MS26 §1.5–1.6 | VALID |
| A1 | ECCC TR26-248 page; PDF pp. 1–3 | VALID. The bound matches. The upper bound 2^{O(n^{2/d})} is in Thm 5.1. The AI disclosure names "ChatGPT 6 Astra" and "Claude Opus 5.5". |
| A2 | ECCC TR26-261 page | VALID |
| A3 | `openai/math` CONTENTS.md, family 112; TR26-248 p. 2 | Main claim **VALID**. It is in fact an **a.e.** bound ("at every sufficiently large input length"). The implicit bound is **MISQUOTED**: see m1. |
| A4 | ECCC TR26-221; arXiv 2609.38677 | VALID |
| A5, A6 | TR26-248 p. 2 (secondary) | VALID as secondary (π/√6, n^{1/4}2^{√n}) |
| A7 | arXiv 2609.34029 (v2, 30 Sep 2026) | VALID. The abstract says "found by GPT-6 Astra". |
| A10 | ECCC TR26-139 (rev. 3, 20 Oct 2026); arXiv 2611.06231 | VALID |
| C2; §2.4 "Open" text | Murray–Williams PDF pp. 1–3 and 16–18 | VALID. Lemma 1.2 gives n^{ck^3}. §6 names the Gap-ACC-UNSAT obstacle verbatim. |
| C3 venue | IEEE Xplore 8948594 (search hit) | FOCS 2019 confirmed |
| C6 venue | LIPIcs ITCS.2023.34 (search hit) | **ITCS 2023.** The survey says "venue not verified". |
| C9 | ECCC TR26-208 | VALID ((2d/√ℓ)^k in v1, (4d/√ℓ)^k over any field in rev. 1) |
| C10 | ECCC TR24-074 page (rev. 1, 24 Nov 2025) | Row VALID. **Trap 12 overreaches**: see m5. |
| C11 | ECCC TR26-116 | VALID (Pago, ICALP 2026, is named in the abstract) |
| T1 | ECCC TR26-039 page; PDF pp. 1–4; ACM DOI 10.1145/3798129.3800802 | VALID. Thm 1.1: "The same holds for SYM∘THR". **STOC 2026 confirmed** (proceedings dated 9 Jun 2026). |
| T2 | ECCC TR26-167 page | VALID, but context is missing: see missing item 8. |
| T4 | ECCC TR26-330 | VALID |
| M5 | ECCC TR25-102; Rao's PDF p. 1 | VALID. The exponent is exp(Ω̃(n^{1/3})), per Rao's account of [CGRSS25]. |
| M6 | ECCC TR26-129 (rev. 5); PDF pp. 1–3 | VALID |
| F8, M8 | ECCC TR26-121 | VALID |
| K3 | Aaronson, arXiv cs/0504048, p. 2 | VALID: "Wilson [40] gave relativized worlds where NP and P^NP have linear-size circuits" |
| K8 | ECCC TR26-328 | VALID |
| K10 | ECCC TR26-313 | VALID |
| K12 | arXiv 2310.17762 | VALID |
| K14 | ECCC TR26-118 | VALID. The abstract does not say whether the bound is i.o. or a.e. |
| K16 | ECCC TR24-113 | VALID. It omits that the conference version's Thm 1.10 was incorrect (an erratum with J. Li is attached). |
| K17, §4.1, §4.4 rows 1–3, §4.5 item 1 | Williams, improved-algs-lbs2.pdf, pp. 1–3 and 20–21; MW PDF p. 18 | **VALID.** Thm 6.1 is verbatim, but it is a *proof sketch* in §6 "Discussion" of the May-2010 manuscript. Footnote 5 is verbatim. MW §6: "E^NP ⊄ SIZE[O(n)] is still open, and one has to prove this first!" |
| R8 | arXiv 2503.17114; ECCC TR25-034 | VALID: m > n, improved from an earlier m > cn². |
| R13 | ECCC TR25-210 | VALID (rev. 1 replaced the prBPP^Avoid proof and added an AI disclosure) |
| R14 | ECCC TR25-190 | VALID |
| R15 | ECCC TR26-302 | VALID. The original listing names only Korten; rev. 1 adds T. Yang. |
| X8 | arXiv 1611.05558; search | Statement OK. **Venue wrong**: see m3. |
| X10 | ECCC TR26-008 | VALID |
| H5 | ECCC TR22-086 | VALID |
| H7 | arXiv 2503.24061 | VALID |
| H8; Table 1 percentages; §4.2 uniform row | likelihoods.pdf pp. 3, 7–8, 11 (the director's link) | H8 and the 93% / 70% / 50% figures are VALID. The uniform row has an attribution slip: see m4. |
| §4.5, Anthropic deposit | hexagonmath.org/2610.00577v1 | VALID (v1 dated 27 Oct 2026) |

---

## 3. Hunt for the classic failure modes (adapted to a survey)

- **Quantifiers, i.o. vs a.e.** I found no swaps in the rows I checked (K12, A3, T2, §4.5). A3 could add "a.e.", which is a
  strength of OpenAI's result.
- **Uniform vs non-uniform.** §4.2 ("For SAT itself") says no SAT-specific bound beyond the trivial one was found. That is true for
  non-uniform B2 circuits. It misses the one SAT-specific circuit-depth bound that exists: SAT needs **polylogtime-uniform** NAND
  circuits of depth ≥ 3.603·log₂ n (Bathie–Williams, ITCS 2024; missing item 2). It is uniform, so it does not touch the
  L^{1.01} target, but it belongs in that table.
- **Size vs depth.** G13 keeps formula depth apart from size correctly.
- **Constants hidden in O().**
  - G1's lower-order term is already improved (S-1).
  - The cslib cost model charges only binary gates. Constants, projections and negations are free, so their bound is at least as
    strong as one stated in total gates.
- **Proves too much / trap formulation.** Rank 4's "kill the algebraic branch" asks to refute a believed conjecture (S-B).
- **Relativization / algebrization.**
  - The survey's AW09 line is marked `checked: no`. The AW09 abstract does support the NP case ("superlinear circuit lower bounds
    for PromiseMA but not for NP"). The P^NP version stays unverified.
  - The 2025/26 algebrization barriers of Chen–Hu–Ren are missing (missing item 3).
- **Natural proofs.** An unconditional natural-proofs barrier for "AC0-natural" proofs (Loff–Sherif–Talebanfard–Ugazio, 2026) is
  missing from §3 (missing item 4). It bites only at large depth, so it does not block rank 2.
- **Hype check.**
  - Rank 2's "moved it three times in 6 weeks" is literally true. But the movement is a √log n factor in the depth-3 exponent, while
    the target n^{1/2+ε} is a polynomial jump.
  - Rank 16's "cannot go past ~n·√log n" overstates the limit (m6).

---

## 4. Solved or superseded since the survey's sources (2023–2026 search)

- **S-1. G1 additive term: 4n − 10d → 4n − 9d** (SERIOUS for exactness; small in substance).
  - cslib-frontier PR #7449 ("tighten B₂ affine-disperser bound to 4n − 9d on binary gates") was merged 22 Nov 2026.
    The statement is `four_mul_le_size_add`: `4 * n ≤ C.size + 9 * d` for any B2 circuit computing a d-affine disperser.
  - The PR calls the potential weights (5, 3, 9) original to the formalization. It also gives an explicit-P corollary of
    `4 * N − 19332 * N^(4/5)` binary gates for `Li.primeDisperser`.
  - Caveats:
    - Only AI agents reviewed it; the PR says no human did.
    - CI was green, but I did not audit it for `sorry` or axioms.
    - The `4n − O(log n)` endpoint still waits on an O(log n)-dimension disperser in Lean (issue #4323).
    - The repo's manual page still shows 10d.
- **S-2. Rank 3 ("Lean 4 formalization of B2/U2 gate-elimination bounds… No B2 lower-bound formalization found") is essentially
  superseded.**
  - cslib-frontier issue #4322 tracks MS26's Theorem 4.1. Milestones 1–3 landed in PR #4356 (11 Nov 2026), refuter correctness in
    PR #4548, and the 9d strengthening on 22 Nov.
  - The manual page `manual/circuits-logic-and-other-models/circuits-and-formulas.md` also lists:
    `Computability/Complexity/AffineDisperser.lean` (3.5N − 42N/(⌊log₂N⌋+1) − 7 for an explicit disperser language, and
    3.5N − 15036·N^{4/5} for a Li/Shoup variant).
  - An attempted **original** U2 bound of 5n − 23(d+2) for affine dispersers (issue #7432) was paused on 23 Nov. The core modules
    were done with "0 sorrys, ~4.5k LOC", but the step lemma grew past ~19k lines.
  - What remains open is only Schnorr's 2n − O(1) and parity's 3(n−1) as separate Lean statements. Their impact is low.
- **S-3. §8 row "none found: any B2/U2 general-circuit lower bound…, algorithmic-method theorem, Kannan-type bound… in a proof
  assistant" is false as of 23 Nov 2026.** The same manual page lists:
  - `Circuit/Boolean/Hastad.lean`: an explicit parity ∉ AC0 bound.
  - `Smolensky.lean`: MOD_p ∉ AC0[q].
  - Khrapchenko, and Subbotovskaya/Andreev n^{2.5−o(1)}.
  - A superpolynomial monotone bound for bipartite perfect matching.
  - The Yao/Beigel–Tarui ACC → SYM∘AND simulation and Williams' evaluation lemma.

  The PR list also shows:
  - PR #4482, Razborov's GF(2)-rank result P ⊄ AC0[2] (merged 11 Nov).
  - PR #2020, **Kannan's theorem** Σ2 ∩ Π2 ⊄ SIZE(n^k), `exists_mem_SigmaP_two_inter_PiP_two_notMem_SIZE` (merged 31 Oct).
    Its review was an agent review, not human approval.
- **S-4. Rank 1 is not solved, but it is in active public progress.**
  - cslib-frontier issue #1539, "Circuit lower bounds from refuting ETH: E^NP ⊄ SIZE(O(n)) and Corollary 1.4", was opened
    28 Oct 2026 and is open. Progress so far:
    - Landed or merged: M1, E^NP as an oracle class (#2055); the CircuitSAT counter (#2052); the witness-bit bridge.
    - In review: M2, the exponential NTIME hierarchy (#2074); M3a/M3b, the Tseitin CNF and succinct tableau (#2082, #2083).
    - Waiting for human review: #4516, the verifier construction.
    - Still listed as available: M5–M7, the core theorem and Corollaries C.1 and 1.4.
  - A second, inactive request exists: `konard/p-vs-np` issue #645 (opened 3 Nov 2026, no progress).
- **S-5. C10 and trap 12 ("last progress" Nov 2025) are out of date.** Wesonga, arXiv 2610.19174 (13 Oct 2026, Lean-formalized
  per the abstract), answers 2 of Krishan–Vishwanathan's 5 open problems:
  - a bounded-lift lower bound d(B+1) = Ω(n);
  - explicit torus-polynomial approximations of degree ≤ n−1.

  ECCC TR26-116 (Jul 2026) also cites KV as ITCS 2026.
- **S-6. Rank 11 and T4 have active competition.** Reitwießner's Andreev results were first developed and merged in cslib-frontier
  by user `chris-ai1`:
  - PR #4720: exact (5/16+o(1))n² circuit;
  - PR #4718: sign-coherent Ω(n²/log³ n);
  - PR #4722: truncated circuits;
  - all merged 11–12 Nov, before the ECCC posting on 20 Nov.

  Issue #4640, "Andreev's function: sharper depth-two threshold bounds", is open there.
- **S-7. T1's venue is resolved.** STOC 2026, confirmed by DOI 10.1145/3798129.3800802.

I searched specifically for, and did **not** find: a B2 bound above 4n; any THR∘THR gate bound above n^{2.5}; a depth-3 bound above
2^{Ω(√(n log n))}; monotone exp(n^{1−ε}); new explicit rigidity; a cubic-plus formula bound; NC0_3-Avoid in FP^NP; or NP ⊄ ACC0.
For THR∘THR, a public repo (missing item 9) reports method barriers, not a new bound.

---

## 5. Important results missing from the survey (with citations)

1. **cslib-frontier** (github.com/cslib-community/cslib-frontier). Lean 4 + CSLib, AI-assisted, renamed from Complexitylib
   2026-11-08. See S-1 to S-6. The lab's registry check before any Lean or "beyond-frontier" work should include its issues and PRs.
2. **G. Bathie, R. Williams, "Towards Stronger Depth Lower Bounds", ITCS 2024, LIPIcs 287:10.**
   - "SAT requires polylogtime-uniform NAND circuits of depth at least 3.603 log₂ n".
   - Faster #SAT for subcubic De Morgan formulas ⇒ supercubic formula bounds.
   - Relevant to §4.2, G13 and rank 14. The survey cites "Bathie–Williams 2024" only second-hand, for the CAPP connection.
3. **L. Chen, Y. Hu, H. Ren, "New Algebrization Barriers to Circuit Lower Bounds via Communication Complexity of Missing-String",
   arXiv 2511.14038, ITCS 2026.** Algebrizing oracles where BPE has linear-size circuits on all lengths, and where PostBPE does i.o.
   A subclass of MA_E containing the hard language gets h(n)-size circuits for every super-half-exponential h. This belongs in §3
   and in every barrier audit the lab writes (CLAUDE.md rule 2).
4. **B. Loff, S. Sherif, N. Talebanfard, F. Ugazio, "The Switching Lemma shows what the Switching Lemma cannot prove: an
   unconditional natural-proofs barrier", arXiv 2606.12631 (Jun 2026).** No AC0-natural proof gives more than 2^{n^{7/(d−5)}}
   against depth d. It does not apply at depth 3.
5. **S. Wesonga, arXiv 2610.19174** (torus polynomials; see S-5).
6. **M. Gurumukhani, D. Kleber, R. Paturi, C. Rosin, M. Saks, N. Talebanfard, arXiv 2601.04072** (v3, 10 Nov 2026). The exact
   Σ3^3 (bottom fan-in 3) complexity of Majority is poly(n)·(2/6^{1/4})^n, and the paper cites Lecomte–Ramakrishnan's 2^{O(√n)}
   depth-3 Majority circuit. This complements A7 and trap 2.
7. **J. Błasiok, L. Meierhöfer, "Hardness of Clique Approximation for Monotone Circuits", CCC 2025 (LIPIcs 339:4), arXiv
   2501.09545.** Monotone clique-approximation bounds that imply 2^{Ω̃(√n)}. Rao's TR26-129 credits it with the strongest
   clique bounds. It belongs next to M3.
8. **O. Goldreich's comment on ECCC TR26-167 (9 Sep 2026) and the author's reply (27 Sep).** Goldreich argues the near-cubic wire
   bound is a reinterpretation of Chen–Tal–Wang that counts wires instead of gates. Nag agreed the credit was missing; a v2 is on
   Zenodo. This matters for any novelty judgement about T2.
9. **`MacchaCat/depth2-threshold-barriers`** (GitHub, 2026, "with Claude"; it says it contains no new lower bound; unrefereed).
   - Lean-verified *method barriers* to extending CTW beyond n^{2.5} (e.g. `ProblemQ.barrier`).
   - It calls ETHR∘ETHR and MTHR∘THR at n^{2.5−ε} "routine corollaries" of CTW.
   - Rank 7 needs a novelty check against it first.
10. **J. Li, D. Reichman, R. Williams, T. Wu, ECCC TR26-311 / arXiv 2611.21910 (6 Nov 2026).** An Ω(n^{1.5}/polylog n) size
    bound for an explicit P function against depth-3 sigmoid networks (extends Kane–Williams), plus near-tight wire bounds for
    PARITY. Belongs in §2.5.
11. **OpenAI math release, family 127, "Average sensitivity of polynomial threshold functions" (25 Sep 2026; AI-produced;
    Lean).** Average sensitivity of degree-d PTFs is ≤ 8d√n, the asymptotic Gotsman–Linial bound. Relevant to §2.5. Unrefereed.
12. **Kardeş–Rossman [KR26]**, a "different top-down argument" for all depths, cited in TR26-248 p. 2. **I could not locate it**:
    UNCHECKED-CITATION. It should go next to A4 once found.
13. **`konard/p-vs-np` issue #645**, a second open request to formalize the ETH ⇒ E^NP bound (see S-4).
14. **Chandrasekaran–Goodman–Zuckerman, "Quadratic Extractors", ECCC TR26-303 (5 Nov 2026).** Listed to prevent a misreading: it
    extracts from quadratic *sources* (images of quadratic maps) with min-entropy polylog(n). It does **not** give the dispersers
    for quadratic *varieties* that G3a / FGHK's 3.11n needs, so G3a stays conditional.

---

## 6. Tractability / impact scores I think are miscalibrated

| Rank | Problem | Survey T×I | Suggested | Reason |
|---|---|---|---|---|
| 1 | Lean transfer "fast sparse 3-SAT ⇒ E^NP ⊄ SIZE[c·n·√log n]" | 3×4 = 12 | I ≤ 2 if started from scratch; recast as "audit or contribute to cslib-frontier #1539" | It is being raced in public (S-4). The survey's "first end-to-end Lean-checked superlinear general-circuit lower bound" is undermined by cslib's Lean Kannan theorem, an n^k lower bound for general circuits (PR #2020; I did not audit it for `sorry`). Contributing upstream would need Sarim's approval (CLAUDE.md, Stage 6 rule). |
| 2 | Depth-3 2^{n^{1/2+ε}}, or pin down Goldreich–Tal f_n | 3×4 = 12 | T = 2 (8) | The 2026 gains are a √log n factor in the exponent. n^{1/2+ε} needs a polynomial jump. The area is crowded by OpenAI, the GPT-6-Astra/Claude-assisted Chukhin paper, and Li–Zhong, so the scoop risk is high. |
| 3 | Lean gate-elimination bounds | 4×3 = 12 | I = 1 (superseded) | S-2. |
| 4 | Kill the algebraic branch of the NE / VP^0_Z win-win, or push OMIN toward ONP or P^NP | 2×5 = 10 | **T = 1 (5)** | `informal-argument` (reviewer). The win-win is an inclusive "or". Read literally, "killing the algebraic branch" means proving VP^0_Z = VNP^0_Z, refuting a conjecture everyone believes. Otherwise it needs an algebraic⇒Boolean hardness transfer that is not known. "OMIN toward P^NP" is P^NP ⊄ SIZE[n^k], which CMMW19 show is equivalent to a Karp–Lipton collapse (K6). The better-posed target in the same paper is CGGM's fine-grained one: beat O(s·t^{d−1}) PIT by t^ε (§4.4 last row). |
| 7 | THR∘THR beyond n^{2.5} | 2×4 = 8 | unchanged | First run a novelty check against missing item 9. |
| 9 | NP ⊄ ACC0 via Gap-ACC-UNSAT | 2×4 = 8 | T = 1 (4) | Should match ranks 13–16, which have T = 1. MW's named obstacle (verified) has not moved since 2018. |
| 10 | B2 beyond 4n / U2 beyond 5n | 3×2 = 6 | T = 2 (4) | MS26 themselves say 4n is "close to the limit". cslib's "u2-beyond5n" worker stalled in a ~19k-line case analysis (#7432). The 9d tweak shows others are already mining the constants. |
| 11 | Andreev vs THR∘THR | 3×2 = 6 | unchanged | Competition: cslib issue #4640 is open (S-6). |

---

## 7. Issues by severity

**SERIOUS**
- **S-A.** The cslib-frontier omission makes §8 false, rank 3 superseded and rank 1 duplicative. Its "first" claim is likely false
  (S-2, S-3, S-4). It also hides the G1 improvement (S-1). These are the top-ranked items, so Stage 2 would pick a direction that
  is already done or already being raced.
- **S-B.** Rank 4 is miscalibrated and, as worded, is a trap: it asks to refute a believed conjecture (§6).

**MINOR** (7)
- **m1. A3 misquote.** The survey gives OpenAI's implicit bound as 2^{Ω(√n·log log n/log log log n)}. TR26-248 p. 2 says
  2^{Ω(√(n log log n / log log log n))}, with the square root over the whole expression. The survey overstates it.
- **m2. Internal inconsistency.** Rank 2 gives the Goldreich–Tal f_n lower end as 2^{Ω(√(n log n/log log n))}, Chukhin's bound.
  Row A2 (Li–Zhong) already gives 2^{Ω_d((n log n)^{1/(d−1)})} for the Goldreich–Tal trilinear function, i.e. 2^{Ω(√(n log n))}
  at depth 3.
- **m3. X8 venue.** Alman–Williams, "Probabilistic Rank and Matrix Rigidity", is **STOC 2017**, not FOCS 2017.
- **m4. §4.2 uniform row.** The n^{2cos(π/7)} time–space lower bound for SAT comes from the line [For00, FLvMV05, Wil08a, Wil13a]
  (Williams' essay §2.3). Buss–Williams 2012 only proves that current techniques cannot beat this exponent. The row credits the
  bound itself to Buss–Williams.
- **m5. Trap 12 overreaches.** KV TR24-074 rev. 1 proves "symmetric torus polynomials are weaker than their asymmetric
  counterparts" **for AND**. For MAJORITY it gives an error–degree trade-off. "Shown weaker … for Majority" is not what the
  abstract says.
- **m6. Rank 16 overstates the limit.** "That technique cannot go past ~n·√log n" is too strong. The E^NP bound tracks the
  sparse-3-SAT saving (01-survey O2: pieces with ρ < 1/√2 would give n·(log n)^{log₂(1/ρ)}). The *current* algorithms stop at
  √log n.
- **m7. Bibliography and venue gaps.**
  - C6 is ITCS 2023.
  - T1 is STOC 2026; this is now confirmed.
  - X12 (CKMS25) is STACS 2026, LIPIcs 364:28.
  - C12 (RSS) appears at ITCS 2026 (search hit).
  - The WilEss entry has no year; the essay cites 2018 work and is from the LNCS-volume era (2018–19).
  - K16 omits the Vyas–Williams erratum.
  - M5's exponent could be stated precisely as Ω̃(n^{1/3}).

---

## 8. What I did NOT check

- Rows I did not open at source:
  - Formulas and threshold: F1–F7, T3, T5–T9.
  - ACC0 and AC0[p]: C1, C3 (beyond its venue), C4, C5, C7, C8, C12.
  - Monotone: M1–M4, M7, M9.
  - Kannan-type and exponential classes: K1, K2, K4–K7, K9, K11, K13, K15.
  - Range avoidance: R1–R7, R9–R12, R16–R18.
  - Rigidity: X1–X7, X9, X11, X12.
  - Magnification: H1–H4, H6.
  - Most page and volume numbers in §10.
- I read only the abstracts of Li–Zhong, Nag, Korten, Lecomte–Ramakrishnan and CHLLTV, not their PDFs.
- I did not open the OpenAI ETH paper's Corollary 1.4 / C.1. cslib issue #1539 and OpenAI's CONTENTS summary corroborate that a
  quantitative fan-in-2 E^NP corollary exists.
- I did not build or audit any cslib-frontier Lean code for `sorry`, axioms or `native_decide`. All cslib statements above come from
  its issues, PRs and manual. Its reviews are mostly AI agents.
- I could not open Williams' 23 Nov 2026 thread, and I could not find Kardeş–Rossman [KR26].
- I did not use DBLP or Google Scholar. arXiv coverage is the cs.CC Oct/Nov 2026 listings plus targeted searches; earlier
  2023–2026 coverage relied on searches.
- Out of scope and not verified, for the lead to route to other scouts:
  - OpenAI's release index lists family 103 "L = RL = BPL", family 274 "Parity is not in QAC0" and family 108 "A cubic
    permanent–determinant lower bound".
  - ECCC TR26-323 is "NL = UL" (Hoza).

---

## 9. Proposed registry entries (for the lead to merge into KNOWN_RESULTS.md)

- [general-circuits][Lean; AI-reviewed only] Any d-affine disperser needs B2 circuits with ≥ 4n − 9d binary gates; explicit-P
  corollary 4N − 19332·N^{4/5} — cslib-frontier PR #7449 (2026-11-22) — checked: yes (PR page), Lean not audited
- [formalization] Lean: Håstad parity ∉ AC0; MOD_p ∉ AC0[q]; P ⊄ AC0[2] (Razborov rank); Kannan Σ2∩Π2 ⊄ SIZE(n^k); B2
  affine-disperser 4n − O(d) — cslib-frontier manual and PRs #4482, #2020, #4356, #7449 — checked: yes (pages), Lean not audited
- [formalization][in progress] Lean formalization of E^NP ⊄ SIZE(O(n)) and of OpenAI's Cor. 1.4 from the ETH refutation —
  cslib-frontier issue #1539 (opened 2026-10-28, still open) — checked: yes
- [uniform-depth] SAT needs polylogtime-uniform NAND circuits of depth ≥ 3.603·log₂ n — Bathie, Williams (2024), ITCS 2024,
  LIPIcs 287:10 — checked: yes (NSF PAR abstract)
- [barrier] Algebrizing oracles: BPE^Ã has linear-size A-oracle circuits on all lengths; a MA_E subclass has h(n)-size circuits
  for every super-half-exponential h — Chen, Hu, Ren (2025), arXiv 2511.14038 / ITCS 2026 — checked: yes (abstract)
- [barrier] No AC0-natural proof gives > 2^{n^{7/(d−5)}} against depth-d circuits (unconditional) — Loff, Sherif, Talebanfard,
  Ugazio (2026), arXiv 2606.12631 — checked: yes (abstract)
- [ACC0] Torus polynomials for Majority with lifts in an interval of width B need d(B+1) = Ω(n); explicit degree-(n−1)
  approximations — Wesonga (2026), arXiv 2610.19174 — checked: yes (abstract)
- [monotone] Clique-approximation lower bounds for monotone circuits implying 2^{Ω̃(√n)} — Błasiok, Meierhöfer (2025), CCC 2025,
  arXiv 2501.09545 — checked: no (search summary only)

---

## Sources (opened on 2026-11-23)

- ECCC reports: https://eccc.weizmann.ac.il/report/2026/260/ (and revision/1 PDF), /2026/248/ (and PDF), /2026/261/, /2026/208/,
  /2026/039/ (and PDF), /2026/167/, /2026/330/, /2026/221/, /2026/139/, /2026/129/, /2025/102/, /2026/313/, /2026/303/, /2026/241/,
  /2026/302/, /2026/328/, /2026/118/, /2026/121/, /2026/008/, /2026/116/, /2026/251/, /2026/224/, /2026/311/, /2024/113/,
  /2024/086/, /2024/074/, /2025/210/, /2025/190/, /2025/034/, /2022/086/
- ECCC year listing: https://eccc.weizmann.ac.il/year/2026/
- arXiv: https://arxiv.org/abs/2609.34029, /2611.06231, /2604.23958, /2602.17942, /2610.19174, /2601.04072, /2503.17114,
  /2503.24061, /2310.17762, /2609.38677, /2606.12631, /2511.14038, /2611.05136; listings https://arxiv.org/list/cs.CC/2026-10 and
  /2026-11
- Williams: https://people.csail.mit.edu/rrw/improved-algs-lbs2.pdf ; https://people.csail.mit.edu/rrw/easy-witness-nqp.pdf ;
  https://people.csail.mit.edu/rrw/likelihoods.pdf ; Aaronson https://arxiv.org/pdf/cs/0504048
- Rao: https://homes.cs.washington.edu/~anuprao/pubs/matchinglowerbound.pdf
- cslib-frontier: https://github.com/cslib-community/cslib-frontier ; issues/PRs #1539, #2020, #4322, #4640, #7432, #7433, #7449,
  and the manual page manual/circuits-logic-and-other-models/circuits-and-formulas.md
- https://github.com/konard/p-vs-np/issues/645 ; https://github.com/MacchaCat/depth2-threshold-barriers
- OpenAI release index: https://raw.githubusercontent.com/openai/math/main/CONTENTS.md ; https://github.com/openai/math/blob/main/lean/docs/127.md
- Bathie–Williams abstract: https://par.nsf.gov/biblio/10579532
- Anthropic deposit: https://hexagonmath.org/2610.00577v1
- Search hits used for venues: doi.org/10.1145/3798129.3800802 (CTW, STOC 2026); LIPIcs ITCS.2023.34 (Chen); LIPIcs STACS.2026.28
  (CKMS); LIPIcs CCC.2025.4 (Błasiok–Meierhöfer); arXiv 1611.05558 / Caltech TCS+ page (Alman–Williams, STOC'17)
