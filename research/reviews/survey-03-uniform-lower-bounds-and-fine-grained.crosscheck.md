# Cross-check of survey 03 "uniform-lower-bounds-and-fine-grained"

- Reviewed file: `research/survey/03-uniform-lower-bounds-and-fine-grained.md` (614 lines, read in full).
- Reviewer: independent cross-checker (red-team role), 2026-11-23. I did not write the survey and did not edit it.
- Method: I opened primary sources (PDFs rendered page by page, arXiv abstract and HTML pages, ECCC report pages,
  GitHub issues and PRs, and the local cslib-frontier clone at commit 1435284b). I then searched arXiv, ECCC, GitHub
  and the web for 2023 – 23 Nov 2026 work on every open problem in §4. Each verdict below names what I opened.
- Labels: VALID / WRONG / INCOMPLETE / UNCHECKED-CITATION per row. Severity: FATAL / SERIOUS / MINOR. My own
  reasoning carries the CLAUDE.md status `informal-argument` (reviewer).
- **Verdict: DAMAGED-REPAIRABLE** (structured verdict: needs-corrections). No fatal errors: the classical frontier is
  accurate. Two serious problems affect what the lab should work on next. There are 9 minor errors and 11 missing items.

---

## 0. Plain-language summary

1. **The classical rows are right.** I checked every L-vs-NP time–space row I could open against its source, and they
   match:
   - Fortnow's theorem, Lipton–Viglas (√2), the golden-ratio bound, and Williams' record 2cos(π/7) ≈ 1.8019;
   - van Melkebeek's two "master theorems" and the ∛4 bound for tautologies;
   - all nine numbers in Buss–Williams' table of the best exponents current methods can prove (Fig. 8.2);
   - the theorems, corollaries and open questions of Williams' 2025 square-root-space paper.

   I found no invented citation.
2. **The survey's "cheapest high-value" task is already being done in public.** The survey's top verification target
   (V1, rated tractability 5) is an independent audit of Charlie Cruz's Lean proof that nondeterministic linear time is
   strictly weaker than deterministic linear space. On 22 Nov 2026, the day before the survey was written, Cruz opened
   cslib-frontier PR #7507. It ports his whole proof into cslib-frontier: about 60,000 lines in 185 files. The project
   coordinator has made it the "checked reference" and scheduled a review in slices. In addition, one of the three
   targets in open problem P4 ("nondeterministic time t in o(t) alternating time") is being formalized right now in
   cslib-frontier issue #4728, from another person's draft.
3. **One headline result is explained wrongly.** The new N^{3/2} lower bound for pushdown reachability
   (Balasubramanian–Majumdar, 20 Nov 2026) does **not** use Williams' 2025 simulation. It uses only the classical
   time hierarchy theorem plus a very efficient reduction; the paper itself says Williams' result "does not subsume" it.
   The survey's summary, its technique/barrier table and the rationale for P5 all say the opposite.
4. **Small errors:**
   - a missing co-author (Machmouchi on "Beame–Clifford");
   - a misquoted bound in Williams' Theorem 5.1;
   - a wrong digit in the Li–Ye Subset Sum exponent;
   - a false statement that cslib-frontier lacks ⊕TIME, Mod_qTIME and C₌TIME;
   - an unsourced "n^{1.759}";
   - two quantifier or strength slips;
   - a weak lead-scout inference in P6.
5. **No listed open problem has been solved.** For 2025 to 23 Nov 2026 I found no claim of any of the following:
   - a superlinear time lower bound for QBF;
   - a bound beating 2cos(π/7);
   - TreeEval ∈ L, or TIME[t] ⊆ SPACE[√t];
   - a barrier for Williams-type simulations;
   - a sublinear-space simulation of random-access machines;
   - DTIME ≠ NTIME beyond n√(log* n);
   - subquadratic Orthogonal Vectors;
   - a 2^{n^{1−ε}} algorithm for 3-SAT (Weak ETH).

   The only progress I found is the crowding in point 2.
6. **Scores.**
   - P1, ranked first, is harder than its T = 3 suggests. Williams ties it to a question that Cai and Watanabe could
     not settle in 2006, and he doubts the NNJAG route.
   - P3 and V1 are crowded.
   - P9's tractability is generous.

---

## 1. Scope and well-definedness

- The survey covers four areas:
  - time–space lower bounds for SAT on random-access machines (L vs NP);
  - branching-program tradeoffs;
  - time-vs-space simulations (P vs PSPACE) and explicit polynomial lower bounds;
  - NTIME vs DTIME/SPACE, plus a fine-grained addendum to survey 01.
- The model conventions are stated and standard: random-access TMs for the SAT bounds, multitape TMs for Williams/HPV,
  and branching programs with T = length and S = log size.
- Trap 8 ("state the model with every bound") is good practice, and the frontier rows follow it.
- The survey's label convention is honest: every row marked `checked: yes` that I opened matched its source. The two
  exceptions are row F6 and the S7 Theorem 5.1 sub-claim; see §3.

---

## 2. Row-by-row verification (what I opened)

| row(s) | source opened | verdict |
|---|---|---|
| U1 | vM07 p. 199, Thm 1.1 | VALID |
| U2 | vM07 p. 199 and fn. 1 | VALID |
| U3 | FLvMV05 PDF: abstract, Thm 1.1, Thm 1.2 (pp. 1–2) | VALID (including "linear time and space n^{1/c}") |
| U4 | search hits for Williams CCC 2005 and *Comput. Complex.* 15(4):433–470 (2006); ECCC TR07-036 abstract | √3: VALID. **"n^{1.759}": UNCHECKED-CITATION.** Neither abstract states it, so it cannot be attributed to CCC 2005 as written. The survey already marks the row `no`. |
| U5 | ECCC TR07-036 abstract; vM07 Thm 1.2 | VALID: n^{o(1)} space, cubic c³ − c² − 2c + 1 < 0, "c < 1.801 suffices", MOD₆ and composite non-prime-power m, at most one exceptional prime |
| U6 | vM07 p. 200 Thm 1.3; p. 201 (d²(d−1) − 2d + 1 = 0 gives 2cos(π/7)) | VALID |
| U7 | Buss–Williams journal PDF: Thm 1.1 (p. 5), Fig. 8.2 (p. 58), Fig. 8.3 (p. 59) | VALID. All nine (ε, c) pairs match, and "the computer-based search was able to *prove* there is no alternation trading proof for the next value of c" |
| U8 | Buss–Williams p. 3: "if SAT ∈ DTISP(n^c, n^ε) then c + ε ≥ 1.573" | VALID |
| U9 | vM07 p. 203, Thm 1.4 and 1.5; vM07 ref. [18] | VALID. The published versions are missing: COCOON 2009 (LNCS 5609) and *J. Comb. Optim.* 22(3):325–338 (2011) |
| U10 | vM07 Thm 1.7 (p. 207); p. 206 "To date we know of no nontrivial lower bounds for satisfiability on such models with two-sided error"; p. 208 (TAUT with one-sided error, n^{2cos(π/7)−o(1)}) | VALID. Thm 7.6 (Σ_k, d < k) not opened |
| U11 | vM07 p. 208 (narrative only) | consistent; Thm 1.8 not opened |
| U12 | FLvMV05 p. 2: "To date no better time lower bound than the trivial one is known on unrestricted random-access machines". vM07 Ch. 9, p. 292: "critically rely on sublinear space bounds", "all the ingredients we use relativize … quasi-linear time" | VALID |
| U13 | cslib `Speedup.lean` docstring cites [AroraBarak09] §5.4 for NTIME(n) ⊄ TISP(n^{1.2}, n^{0.2}) | consistent (book not opened) |
| U14 | vM07 ref. [31] | venue VALID |
| U15 | Lipton–Williams journal PDF p. 2 | VALID (quote verbatim, citing For00, FLvMV05, BW12) |
| B2, B4, B5, B6 | arXiv 1309.3690, pp. 1–2 | content VALID, **authors WRONG** (m1) |
| B10 | arXiv 2610.24377 abstract and pp. 2–3 | VALID |
| S3, S4, S5, S7, S7b | Williams 2025 v1 PDF, pp. 1–3, 12–13, 16–19 | VALID, except **Thm 5.1 misquoted** (m2) |
| S8 | search: DOI 10.1145/3798104 resolves to the J. ACM article (June 2026) | VALID; can be upgraded from `no` |
| S9 | search: LIPIcs vol. 383, CCC.2026.3 | VALID; venue missing (m6) |
| S10 | ECCC TR26-223 | VALID. The model is a strengthened parallel external-memory model, not a RAM |
| S11 | arXiv 2602.14320 (v1 15 Feb, v3 8 Nov 2026) | VALID |
| S12 | ECCC TR26-233 | VALID ("some hardness assumption is necessary … because they imply P ≠ PSPACE") |
| S13 | OpenAI `lean/docs/137.md` | VALID: one writable tape plus read-only input heads; time-capped and unknown-time simulators; "general multitape simulation" excluded |
| S14 | ECCC TR26-006 | VALID |
| S15, §8 Williams | clone: `DTIME_subset_DSPACE_sqrt` (Williams.lean:111), WilliamsSeparation theorem names | VALID |
| L2 | arXiv 2512.00297 | VALID (uses Williams 2025) |
| L3, L4 | arXiv 2611.27814, abstract and HTML | statements VALID; the AI statement is verbatim but sits in the "AI Methodology" section, not §1 or §7. **Its technique is misdescribed elsewhere in the survey** (S-2) |
| L5 | BM26 §1 | VALID |
| L6 | OpenAI `lean/docs/133.md` | VALID: n^{ck} with absolute c; multitape TMs and log-word RAMs; diameter ≤ 2; EXPTIME-complete on subcubic graphs |
| L9, L10 | LW13 abstract; Williams 2025 p. 17 "which is still open [Wil08, LW13]" | VALID |
| L12 | ECCC TR26-331 | VALID |
| L14 | clone: `palindrome_lower_bound` (n² ≤ 64·clog₂(\|Q\|+2)·T(n)), `isRegular_of_isLittleO` | VALID |
| N2 | ECCC TR01-022 abstract | VALID: n√(log* n). (A 2026 secondary source rendered it as "n lg* n"; the survey has it right.) |
| N4, N5, F9 | arXiv 2611.11832, abstract and HTML: Lemma 2.1, Thms 2–3, "long-standing open problem", "by necessity, does not relativize", Fact 1.3 | VALID |
| N6 | Cruz README | VALID (README says SPACE; uses "Complexitylib" definitions; "The draft is unrefereed") |
| N7 | cslib issue #2226 | VALID, but out of date: PR #7507 is missing (S-1) |
| N10, §8 CountingSimulation | clone: `FastSimulation.lean:101`, `CountingClasses.lean:391` | VALID |
| F6 | arXiv 2610.10446 | **exponent WRONG** (m3) |
| F10, F12 | arXiv 2611.10633, 2611.07308 | VALID |
| E3 | Shtetl-Optimized ?p=10239, comments #4, #17, #18, #31 | VALID |
| E4 | Fortnow, 10 Jun 2026 | VALID (all three quotes verbatim) |
| §2.9 item 2 | Aaronson–Wigderson abstract: "almost all of the major open problems—including P versus NP … —will require non-algebrizing techniques" | VALID; can be upgraded from `no` |
| §3 row 1, trap 5, [barrier] entry | vM07 p. 292 | VALID |
| P17 rationale | vM07 p. 293 ("the slack in Lemma 5.1 suggests … up to the golden ratio") | VALID |
| Traps 1–2 | arXiv 2508.14831 (v4 withdrawn 1 Jan 2026; comment verbatim); arXiv 2604.02606 (v2 withdrawn 7 Apr 2026) | VALID |
| Trap 10 | clone: `ModP/Time.lean:62,67` (`ParityTIME`, `ModTIME`), `CeqP/Time.lean:52` (`CeqTIME`) | **WRONG** (m4) |
| §8 #2896 | issue page; clone `Speedup.lean` | status VALID (M3 not started), but **INCOMPLETE**: the merged speedup is weaker than the textbook one (§6, P3) |

---

## 3. Issues by severity

### SERIOUS

**S-1. The top verification target V1, and part of P4, are already being done in public.**

- **cslib-frontier PR #7507** (author SeniorMars, the GitHub account hosting `SeniorMars/ntime.dspace`). Opened and
  marked ready for review on 22 Nov 2026.
  - Title: "feat(TimeSpace): NTIME[t] ⊆ DSPACE[t/√log t] and NTIME[n] ⊊ DSPACE[n]".
  - Size: 185 files, about 60k lines; the headline theorem is `NTIME_id_ssubset_DSPACE_id`.
  - The PR says its t/√log t bound is stronger than the T(log log T)²/√log T requested in issue #2226.
  - The coordinator (edemaine) asked that this full port, at commit 5ea218d, "serve as the checked reference". Smaller
    dependency-ordered PRs are to follow; the author proposed 11 slices. S. Schlesinger asked when the review agents
    should start.
  - Known open items listed in the PR: 321 projection chains, overlap with `ParityTIME`/`ModTIME`/`CeqTIME` on `main`,
    and a custom program language. No human or independent review yet.
- **What the survey says instead.**
  - It records only issue #2226 and "draft PR #2231 covers a first milestone only".
  - It rates V1 at T = 5 as cheap and impactful.
  - It asks the lab to "reconcile the T(log log T)²/√log T vs t/√log t versions". That question is already answered:
    the 1 Nov form (recorded in #2226) is the earlier, weaker bound; the 10 Nov paper and PR #7507 state the improved
    t/√log t.
- **P4's ATIME clause.** P4 lists "NTIME[t] ⊆ ATIME[o(t)]" as open. **cslib-frontier issue #4728** (opened 12 Nov 2026
  by user shmcg, who signs "Sam") formalizes "a uniform finite multitape alternating machine that checks a specified
  bit of the number of accepting paths within O(n + T/√log(T+2))".
  - The source is the opener's own draft.
  - Milestones so far: #4729 landed; #4741 and #4733 are under way; the latest commit is dated 22 Nov.
  - The coordinator and the author both say the full simulation is not yet proved.
  - For T = ω(n) this would give NTIME[T] ⊆ ATIME[o(T)]. At T = n it gives nothing, because the input term O(n) stays.
  - The survey lists #4728 in §8 but connects it neither to P4 nor to §5's competition table.
- **Consequence for the lab.**
  - V1 as worded duplicates an effort that is already scheduled, and its impact falls; see §6.
  - P4 is more crowded than §5 shows: Cruz (PR #7507), the #4728 opener, R. Yang with T. Pitassi, and S. McGuire.
  - Whether "shmcg" is the S. McGuire named in [Cru26] §1.2 is **not** verified.

**S-2. The pushdown-reachability lower bound is attributed to the wrong technique.**

- **What the paper does.** In arXiv 2611.27814 (BM26), the N^{3/2−ε} bound comes from a chain of reductions plus the
  deterministic time hierarchy theorem, with "a careful counting of the computation time":
  1. TM run → locally addressable circuit ("following the construction discussed by Shalunov"; a recursive simulation
     attributed to Koucký; Pippenger–Fischer O(T log T) circuits);
  2. circuit → relation programs;
  3. relation programs → PDA (intersection) non-emptiness of size ≈ T^{2/3}.

  The contradiction is "with the time hierarchy theorem". Williams 2025 appears **only** in related work: it is used by
  Wehar, not by BM26, and "This result does not subsume our bounds for a single pushdown system".
- **What the survey says.**
  - §1: "In 2025–2026 this [Williams' simulation] was used to prove new polynomial time lower bounds for natural
    problems (pushdown reachability needs N^{3/2} time …)".
  - §3, row "Diagonalization through completeness (… space hierarchy + Williams + efficient reductions)": covers L1–L6
    and says "the Williams step does not [relativize]".
  - P5: "The 2026 method (Williams + succinct circuits + careful constants)".
- **What is right.** Row L3 itself describes the chain correctly. Only L1 and L2 use Williams; L3–L6 are hierarchy plus
  reduction-efficiency arguments in the line of Cook's AuxPDA, Adachi–Iwata–Kasai and Swernofsky–Wehar.
- **Why it matters.**
  - The gap between N^{3/2} and the cubic upper bound in P5 is a question of **reduction efficiency**. An encoding of
    time-T computations into instances of size T^{1/c} yields a T^{c−ε} lower bound. Better space simulations are not
    the lever.
  - The barrier analysis in §3 should not credit these bounds with a non-relativizing Williams step.

### MINOR (9)

- **m1. Authorship.** arXiv 1309.3690 is by **P. Beame, R. Clifford and W. Machmouchi** (title page). The survey says
  "P. Beame, R. Clifford" and uses key `BC13` in B2, B4–B6, §9 and §10. The quotes themselves are verbatim (p. 1).
- **m2. S7, Theorem 5.1 misquoted.**
  - v1 p. 18 states: TIME-LENGTH^A[t(n), √t(n)·log t(n)] ⊆ SPACE-LENGTH^A[√t(n)·log t(n), √t(n)·log t(n)]. It
    extends the warm-up Thm 3.1.
  - The survey writes √(t log t) in all three places, which overstates it by a √(log t) factor.
- **m3. F6 exponent (also in §9).** Li–Ye's abstract gives 2^{0.49999\overline{7}n}: four 9s, then repeating 7s, about
  2^{0.4999978n}. The survey has "O(2^{0.49999977n})".
- **m4. Trap 10 is false at the commit the survey cites.**
  - The survey says Cruz's Thm 7.1 uses locally defined ⊕TIME/Mod_qTIME/C₌TIME because "CSLib Frontier lacks them".
  - Clone 1435284b defines `ParityTIME`, `ModTIME` (`Classes/ModP/Time.lean:62,67`) and `CeqTIME`
    (`Classes/CeqP/Time.lean:52`). PR #7507 lists this overlap as a known item.
  - The claim was copied from Cruz's lean/README, which is now stale.
- **m5. U4's "n^{1.759}" has no source.** The CCC 2005 paper and its journal version state n^{√3}. Drop 1.759 or cite
  where it comes from.
- **m6. Bibliography gaps.**
  - Shalunov is now CCC 2026 (LIPIcs 383, CCC.2026.3).
  - DvMW (U9) was published at COCOON 2009 and in *J. Comb. Optim.* 22(3):325–338 (2011).
  - S8 (J. ACM 2026) and §2.9 item 2 (AW09) can be marked `checked: yes`.
- **m7. Quantifiers and strength in §1 and §2.9 item 1.** "A polynomial SAT algorithm must use super-polylogarithmic
  space or ≥ n^{1.8} time" omits two things:
  - the lower bounds are infinitely-often statements: no algorithm meets both bounds at all large input lengths;
  - the space alternative is actually n^{Ω(1)} (from the golden-ratio tradeoff), which is stronger than
    super-polylogarithmic.
- **m8. §2.9 item 5 understates the obstacle** (informal-argument, reviewer).
  - Any proof of NTIME[t] ⊆ DSPACE[t^{1−ε}], by any route and not just a counting route, refutes SH. Reason: SAT
    instances of size s lie in NTIME[s·polylog s] on multitape TMs, and DSPACE[s′] ⊆ DTIME[2^{O(s′)}].
  - By [MITHG26] (claimed), SH is equivalent to Weak ETH.
  - So P4's polynomial-saving version is at least as hard as P13 (T = 1). Only the sub-polynomial targets of P4
    (t/(log t)^{1/2+δ}, t/log t) are realistic.
- **m9. The P6 lead-scout inference is weak** (informal-argument, reviewer).
  - Williams' SETH remark (v1 p. 18) concerns *multilinear* extensions of CNFs.
  - In his simulation the per-node bottleneck is computing a low-degree extension of a b-step block, at cost
    2^{Θ(b)}.
  - ETH-era counting would at best give about 2^{O(b/√log b)} per node. The requested 2^{Õ(t^ε)} with blocks of
    length ≈ t^{1−ε} needs a 2^{b^{o(1)}}-type evaluation.
  - Evaluating multilinear extensions that fast implies weighted counting for size-b circuits on Θ(b) inputs in
    2^{b^{o(1)}} time. That would refute Weak #ETH, so it is not "unexamined low-hanging fruit".
  - Only Williams' own escape (non-multilinear low-degree extensions) remains open.

---

## 4. 2023 – 23 Nov 2026 search: solved, superseded or crowded

**Sources searched.**
- ECCC 2026 listing (both halves, to TR26-331) and individual reports.
- arXiv abstract and HTML pages for every 2025–26 item cited, plus targeted web/arXiv searches:
  - QBF lower bounds; TreeEval in L or √t space; barriers for Williams-type simulations;
  - quasi-linear Cook–Levin; improvements on 2cos(π/7);
  - DTIME vs NTIME; branching-program tradeoffs;
  - Orthogonal Vectors (OV); Weak ETH; RAM sublinear space;
  - NTIME in sublinear space (Yang/Pitassi/McGuire); CFL/Dyck reachability lower bounds.
- Fortnow's catalogue of OpenAI TCS results (both halves).
- cslib-frontier issues #2226, #2896, #4225, #4728, PR #7507, an issue search, and the lab watch digest of
  2026-11-23.

| item | status found |
|---|---|
| P1 barrier for locality-based simulations | Nothing found. Williams 2025 p. 18 links the restricted-relativization question to Cai–Watanabe [CW06] (missing; see §5) |
| P2 superlinear QBF / multitape t^{1/2−ε} | Nothing found beyond OpenAI's one-tape T^{2/5} (Sep 2026) and SiW26 (Oct 2026) |
| P3 Lean SAT time–space bounds | **Crowded, not solved.** #2896: M1–M2 merged, M3 "not started"; claimed by agent worker w30-tisp; fork commits by orbitingflea (8 Nov). #4225: active Jetski worker `jetski-aa8b-qcl`. Its target is O(T log³ T) by sort-and-check; local computability, which the #2896 transfer needs, is out of M1 scope |
| P4 NTIME in less space or alternating time | **Crowded.** PR #7507 (22 Nov); issue #4728 for the ATIME clause (12–22 Nov); Yang–Pitassi and McGuire (via [Cru26]; no public preprint found) |
| P5 lower bounds for problems in P | BM26 (20 Nov) is the latest; nothing newer found. Technique: see S-2 |
| P6 time–space tradeoff for Williams' simulation | Nothing found (see m9) |
| P7 better quasi-linear Cook–Levin | Only SS26 Lemma 2.1 (O(t) variables across 2^{O(t/b)} CSPs) |
| P8 RAMs in sublinear space | Nothing found. SiW26 does not treat RAMs; Chen–Wang is relativized time evidence only |
| P9 DTIME ≠ NTIME beyond n√(log* n) | Nothing found. Conditional route: Mittal–Raz 2021 (§5) |
| P10 BP n^{1+Ω(1)} at polylog space | Nothing found |
| P11 OV / CNF-SAT | Still standing (searched to Nov 2026) |
| P12 superlinear SAT with no space bound | Nothing for multitape TMs or RAMs. Restricted one-work-tape models have had superlinear bounds since 2004 (§5, van Melkebeek–Raz) |
| P13 Weak ETH / SH | Stands; MITHG26 v2 (16 Nov) calls it plausible |
| P14–P17 | Nothing found |
| V1 Cruz audit | **Effectively taken up by cslib-frontier** (S-1). The "two versions" sub-question is answered |
| V2 one-tape and WL artifacts; V3 BM26 | No visible audit or formalization found |
| Context C2 (NL = UL) | **Already formalized** in cslib-frontier: `Cslib.Complexity.NL_eq_UL` (`Classes/LogSpace/Hoza.lean:85`; issue #6747 closed 22 Nov). A native development toward OpenAI's L = RL = BPL is also in progress (`LogSpaceDerandomization/*`; the equality is not yet stated as a theorem in the clone) |

---

## 5. Important results missing from the survey

1. **cslib-frontier PR #7507** (22 Nov 2026) and **issue #4728** (12–22 Nov 2026). See S-1.
2. **G. Bathie, R. Williams, "Towards Stronger Depth Lower Bounds", ITCS 2024, LIPIcs 287:10.** SAT requires
   polylogtime-uniform NAND circuits of depth ≥ 3.603·log₂ n.
   - This is a *uniform* lower bound for SAT obtained in the alternation-trading tradition.
   - The survey-02 cross-check flagged it for survey 02; it belongs in §2.1 here.
   - Source: abstract via the survey-02 cross-check; not re-opened by me.
3. **A. S. Mudigonda, R. Williams, ITCS 2021, LIPIcs 185:50** (abstract opened).
   - Some problems verifiable in O(n) time with QMA protocols are not solvable in n^c time and n^{o(1)} space, for
     c < (3+√3)/2 ≈ 2.366.
   - For MA-verifiable problems: no randomized n^c time with O(log n) space for c < 1.465, improving Diehl. The quantum
     version of that bound is c < 1.5.
   - Belongs next to U10/U11 and bears on P14.
4. **D. van Melkebeek, R. Raz, "A time lower bound for satisfiability", TCS 348:311–320 (2005); ICALP 2004**
   (abstract via search).
   - A deterministic machine with one d-dimensional work tape and random-access input cannot solve SAT in time n^a for
     a < √((d+2)/(d+1)).
   - These are superlinear SAT time bounds with no explicit space bound, in a restricted model. They bound the claim
     in U12/P12.
5. **Lipton–Williams 2013, Corollary 1.3** (journal PDF p. 3): "Either QBF cannot be solved in n^{1+ε} time for some
   ε > 0, or P ⊄ NC/poly." This is a known disjunction directly about P2.
6. **Williams 2025 §5, two pointers the survey drops:**
   - Cai–Watanabe, "Random access to advice strings and collapsing results", *Algorithmica* 46(1):43–57 (2006). Williams
     says the restricted-relativization barrier question "seems related to the fact that Cai and Watanabe were unable
     to collapse PSPACE to P with 'random access to advice'" (p. 18). Relevant to P1.
   - **Hypothesis 3.7** (p. 13): reducing time-t computations to TreeEval instances of height
     O((t/b)/log(t/b)) would give TIME[t] ⊆ SPACE[√t] *without* TreeEval ∈ L. Relevant to P15; Nye's withdrawn paper
     was an attempt of this kind.
7. **K. Mittal, R. Raz, "Block Rigidity: Strong Multiplayer Parallel Repetition implies Super-Linear Lower Bounds for
   Turing Machines", ITCS 2021, arXiv 2011.09093** (abstract opened). A strong parallel-repetition theorem for
   "independent games" would give an explicit block-rigid function that multitape TMs, even with advice, cannot compute
   in linear time (PPST-style). A conditional route for P5/P9.
8. **A. Z. Salamon, M. Wehar, "Superlinear Lower Bounds Based on ETH", STACS 2022, arXiv 2008.06805** (abstract
   opened).
   - Log-CircuitSAT is not in essentially-linear time unless ETH fails (paired with an essentially-linear k-Clique
     condition).
   - Its ETH basis is now claimed refuted, which is relevant to P5 and to survey 01's "basis lost" ledger.
   - The exact disjunction was not read.
9. **cslib-frontier `NL_eq_UL`** and the in-progress LogSpaceDerandomization development (§4, last row). These are the
   formalization status of context rows C1/C2.
10. **Williams 2025 p. 17, the folk "Theorem"**: unless HPV can be improved, TreeEval with constant arity cannot be
    solved in o(h·b/log(h·b)) space. Williams quotes it as an example of a "barrier" that turned out wrong. A useful
    caution for P1.
11. Bibliography entries for m1 and m6, plus the Beame–Clifford–Machmouchi conference version. The arXiv page lists no
    venue, and I did not verify one.

---

## 6. Calibration of tractability (T) × impact (I)

| # | survey T×I | suggested | reason |
|---|---|---|---|
| P1 | 3×3 = 9 (rank 1) | **T = 2 (6)** | Williams ties the restricted-relativization barrier to Cai–Watanabe's 2006 failure (§5 item 6). He says of the NNJAG route "we believe the answer is probably no". One model covering HPV pebbling, Cook–Mertz algebraic recomputation, OpenAI's one-tape factorization and tensor-contraction counting does not yet exist even as a definition. It is still the least crowded item, so keep it, but not as the "safe" first pick. |
| P3 | 4×2 = 8 | **T = 3, I = 1–2**; recast as "coordinate with #2896/#4225, don't duplicate" | Crowded (§4). The merged speedup is TISP(t, s) ⊆ Σ₂TIME(√t·(s + n log² n + log² t)). Its own docstring says "The bound is weaker than the textbook one … Reaching √(t s) … remains open". *Reviewer `informal-argument`:* with virtual padding this probably suffices for the subpolynomial-space exponents (√2, 2cos(π/7)). It does **not** suffice for Fortnow's n^{1−ε}-space theorem (U1) or the polynomial-space part of the golden-ratio tradeoff (U3). The SAT transfer needs a locally computable quasi-linear Cook–Levin, out of scope for #4225 M1. "Engineering on existing modules" understates the work. |
| P4 | 2×3 = 6 | **I = 2 (4)**; mark crowded | S-1 and m8. |
| P5 | 3×2 = 6 | keep; rewrite rationale | S-2: the lever is reduction efficiency. BM26's authors, working with AI tools, are the obvious competitors for CFL and Dyck reachability. |
| P6 | 2×3 = 6 | **T = 1–2** | m9. |
| P9 | 2×3 = 6 | **T = 1 (3)** | No new tool since Santhanam 2001; only a conditional route exists (Mittal–Raz). This is consistent with the survey's own T = 1 for P12/P16. |
| V1 | 5×3 | **I = 1–2**; recast | It is being done by cslib (S-1). The residue still worth doing cheaply (T = 5, I = 2) is a statement-faithfulness check of `NTIME_id_ssubset_DSPACE_id` against textbook NTIME/DSPACE: encodings, how the input tape and work space are counted, and non-constructible t. Do it independently of cslib's agent reviewers, as CLAUDE.md rule 5 asks for main statements. |
| others | — | reasonable | P2 (2×4), P7, P8, P10–P17, V2, V3 look calibrated. |

**An unexamined connection (reviewer `informal-argument`; likely folklore, novelty not checked).**
- A **polynomial-time** version of P6 for multitape machines, TIME[t] ⊆ TISP[t^{O(1)}, t^{1−ε}], would combine with
  Fortnow's theorem (U1) to give SAT ∉ multitape TIME[n^{1+o(1)}], i.e. P12 for multitape TMs.
- Williams' 2^{Õ(t^ε)}-time version does not, because Fortnow needs the second machine to run in polynomial time.

---

## 7. Hunt for the classic failure modes (adapted to a survey)

- **Quantifier swaps; i.o. vs a.e.:** one slip (m7). U2's formal o(1) quantifier structure is stated correctly.
- **Uniform vs non-uniform:** §2.2's direction is right: BP lower bounds imply uniform ones. Bathie–Williams is a
  uniform-circuit bound and is missing (§5).
- **Model mixing:**
  - well handled overall (trap 8);
  - S10 is correctly marked as not a RAM model;
  - S-2 is a technique mix-up, not a model mix-up.
- **Constants in O():** BM26's "caring about the particular constants" is correctly emphasized.
- **Reductions that blow up size:** L11's O(n²) SPACE[n] → QBF reduction and P7 are right. The inference
  QBF ∉ SPACE[N^{1/2−ε}] is sound (space hierarchy plus an on-demand reduction).
- **Relativization and algebrization:**
  - the vM07 Ch. 9 quotes are verbatim;
  - SS26: "by necessity, does not relativize";
  - Williams: Thm 1.1 is non-relativizing but satisfies length-restricted relativization (with m2's correction);
  - S-2 removes the "Williams step" from L3–L6.
- **"Proves too much":** m8 and m9 are the two places where the survey's reasoning is weaker than it looks. Neither
  overclaims a result.

---

## 8. What I did NOT check

- **Rows not opened:**
  - B1 (Ajtai), B3 (BSSV), B7 (Yu–Zhan), B8, B9;
  - S1, S2 and S4 beyond Williams' reference list;
  - S6 beyond search abstracts;
  - N1 (PPST PDF), N3, N8, N9;
  - L7, L13 (OpenAI multiplication), L8 (beyond the title in Williams' references);
  - F1–F5, F7, F8, F11;
  - C1, C3;
  - E1, E2, E5, E6;
  - vM07 Thm 1.8 and Thm 7.6.
- **Proofs.** I did not red-team any proof: not Cruz, BM26, OpenAI's one-tape or WL results, SS26, or Li–Ye.
- **Lean.** I built no Lean development: not cslib-frontier, PR #7507, `ntime.dspace`, or the OpenAI artifacts. I did
  not audit for `sorry`, axioms or `native_decide`. All cslib statements come from source text, issue and PR pages.
- **Unverified facts:**
  - whether GitHub user "shmcg" is S. McGuire;
  - the exact disjunction in Salamon–Wehar;
  - the venue of the Beame–Clifford–Machmouchi conference version;
  - Williams' MFCS 2026 talk content;
  - the J. ACM text of Williams' paper (only the DOI resolution);
  - Williams' 23 Nov 2026 thread.
- **Coverage limits.** No DBLP, Google Scholar, MathOverflow or cstheory searches. Coverage of the arXiv listing is
  through targeted searches, not a full Nov 2026 cs.CC title scan. The ECCC 2026 listing was scanned in full through
  TR26-331.

---

## 9. Proposed corrections and registry entries (for the lead to merge)

**Corrections.**
- §1, §3 and P5: replace "Williams … used to prove … pushdown reachability" with "time hierarchy + T^{2/3}-size PDA
  encoding (BM26); only Wehar's DFA bound uses Williams".
- Trap 10: delete "CSLib Frontier lacks them".
- m1–m3: fix authorship, the Thm 5.1 bound and the F6 digits.
- V1: recast to the statement-faithfulness residue only.
- P4: add #7507 and #4728 to §5.

**Registry entries.**
- [formalization][in progress] Full Lean port of Cruz's NTIME[t] ⊆ DSPACE[t/√log t] and NTIME[n] ⊊ DSPACE[n]
  (`NTIME_id_ssubset_DSPACE_id`), 185 files / ~60k lines, AI-assisted, unreviewed — cslib-frontier PR #7507
  (22 Nov 2026) — checked: yes (PR page), Lean not built.
- [formalization][in progress] Bitwise accepting-path counting in alternating time O(n + T/√log T) (would give
  NTIME[T] ⊆ ATIME[o(T)] for T = ω(n)); a draft claim, not proved — cslib-frontier issue #4728 (12 Nov 2026) —
  checked: yes (issue page).
- [formalization] Hoza's NL = UL for native logspace classes (`Cslib.Complexity.NL_eq_UL`) — cslib-frontier,
  `Classes/LogSpace/Hoza.lean` (#6747 closed 22 Nov 2026) — checked: yes (source read; not built).
- [uniform-SAT] SAT needs polylogtime-uniform NAND circuits of depth ≥ 3.603·log₂ n — Bathie, Williams (2024), ITCS
  2024, LIPIcs 287:10 — checked: no (via the survey-02 cross-check).
- [time-space] Some QMA-linear-time-verifiable problem has no n^c-time, n^{o(1)}-space algorithm for
  c < (3+√3)/2 ≈ 2.366; MA-type: no randomized n^c time and O(log n) space for c < 1.465 — Mudigonda, Williams (2021),
  ITCS 2021, LIPIcs 185:50 — checked: yes (abstract).
- [time-SAT-restricted] SAT ∉ time n^a for deterministic machines with one d-dimensional work tape and random-access
  input, for a < √((d+2)/(d+1)) — van Melkebeek, Raz (2005), TCS 348:311–320 — checked: no (search abstract).
- [QBF] Either QBF ∉ TIME[n^{1+ε}] for some ε > 0, or P ⊄ NC/poly — Lipton, Williams (2013), Comput. Complex. 22(2),
  Cor. 1.3 — checked: yes.
- [explicit-lower-bounds][corrected] Pushdown reachability ∉ multitape DTIME(N^{3/2−ε}). The proof is the deterministic
  time hierarchy plus a T^{2/3}-size PDA encoding of time-T runs; it does not use Williams 2025 —
  Balasubramanian, Majumdar (2026), arXiv 2611.27814 — checked: yes (HTML).

---

## 10. Sources opened (all accessed 2026-11-23)

- **L vs NP classics:**
  - FLvMV05: https://lance.fortnow.com/papers/files/tst.pdf (pp. 1–3)
  - vM07: https://pages.cs.wisc.edu/~dieter/Papers/sat-lb-survey-fttcs.pdf (pp. 198–208, 292–296, 300–303)
  - Buss–Williams: https://mathweb.ucsd.edu/~sbuss/ResearchWeb/npProofLimits/paper-journal.pdf (pp. 1–6, 55–60)
  - ECCC TR07-036, TR01-022
  - Lipton–Williams: https://people.csail.mit.edu/rrw/qbf-nc-journal-rev.pdf (pp. 1–3)
  - Aaronson–Wigderson: https://www.scottaaronson.com/papers/alg.pdf (p. 1)
- **Time vs space:**
  - Williams 2025: https://arxiv.org/pdf/2502.17779v1 (pp. 1–4, 13–15, 17–24)
  - arXiv 2508.14831, 2604.02606, 2602.14320, 2610.24377 (abstract, pp. 2–3)
  - ECCC TR26-223, TR26-233, TR26-006, TR26-045, TR26-331
  - OpenAI `lean/docs/137.md` and `133.md`; Fortnow's catalogue https://lance.fortnow.com/openai-math-tcs.htm
    (both halves)
- **Explicit lower bounds:** arXiv 2611.27814 (abstract and HTML, both halves), 2512.00297, 2008.06805, 2011.09093;
  LIPIcs ITCS.2021.50 (Mudigonda–Williams).
- **NTIME:** arXiv 2611.11832 (abstract and HTML); https://github.com/SeniorMars/ntime.dspace (README).
- **cslib-frontier pages:** issues #2226, #2896, #4225, #4728; PR #7507; an issue search page.
- **cslib-frontier clone files:** `Classes/TimeSpace/{Speedup,Williams}.lean`,
  `Classes/CountingSimulation/{FastSimulation,CountingClasses}.lean`, `Classes/{ModP,CeqP,PP,SharpP}/Time.lean`,
  `Classes/LogSpace/Hoza.lean`, `Machines/Turing/SingleTape/{Palindrome,NLogNGap}.lean`, `roadmap/complexity.md`.
- **Fine-grained:** arXiv 2610.10446, 2611.10633, 2611.07308.
- **Commentary:** https://blog.computationalcomplexity.org/2026/06/respect-p-v-np-problem.html ;
  https://scottaaronson.blog/?p=10239
- **Search hits relied on for metadata only:**
  - DOI 10.1145/3798104 (J. ACM 2026)
  - LIPIcs CCC.2026.3 (Shalunov)
  - DvMW COCOON 2009 / J. Comb. Optim. 2011
  - van Melkebeek–Raz TCS 2005
  - Williams CCC 2005 / Comput. Complex. 2006 abstracts (√3)
- **Lab files:** `research/watch/2026-11-23.md`.
