# 03 — Uniform lower bounds and the post-ETH fine-grained landscape

Lit-scout survey, area 03 "uniform-lower-bounds-and-fine-grained". Written 2026-11-23 by the lit-scout (Claude).
Single author, not yet cross-checked by a second agent.

**How to read the labels** (same conventions as survey 01).
- `checked: yes` = I opened the primary source on 2026-11-23 (PDF, abstract page, Lean source/README) and the row
  matches it. `yes (abstract)` = abstract or catalogue summary only. `yes (via X)` = the statement is taken from
  a secondary source X that I opened and that states it with attribution; the original was not opened.
- `checked: no` = from memory, a search snippet, a source I could not open, or another lab survey. Do not build on it.
- **claimed** = the authors' claim; no completed independent review. **[AI]** = the source says the result or its
  proof was produced mainly by an AI system.
- **Lead-scout inference** = my own reasoning; status `informal-argument`; nobody has red-teamed it.
- No item in this file has lab status `lean-verified`. External Lean checks are the authors' own.

**Cross-references (not repeated here).** Survey 01 (`01-eth-refutation.md`) owns the ETH refutation itself, its
hypothesis ledger (§2.5) and its follow-ups; survey 02 (`02-circuit-lower-bounds.md`) owns circuit lower bounds and
Williams' "SAT ∉ SIZE[L^{1.01}]" challenge (§4). Read both cross-checks in `research/reviews/` first. Entries already in
`research/KNOWN_RESULTS.md` (e.g. Strassle–Subercaseaux, MIT Hardness Group's SH ⇔ Weak ETH, Alman–Vassilevska
Williams 3SUM/APSP) are referenced, not re-entered, except where this survey adds a verified detail.

---

## 1. Plain-language summary

"Uniform" lower bounds ask how much time or memory one fixed algorithm (a Turing machine or a random-access machine)
needs. Ryan Williams' view is that we must first prove the "easier" relatives of P ≠ NP: that SAT cannot be solved
with tiny memory (L ≠ NP), and that polynomial memory is more powerful than polynomial time (P ≠ PSPACE). For
L vs NP the record has not moved since 2007: an algorithm for SAT that uses n^{o(1)} memory needs about n^{1.8019}
steps, and Buss and Williams proved that the known proof method cannot go further; I found no 2024–2026 improvement.
For P vs PSPACE there was a real jump in 2025: Williams showed that any t-step multitape computation can be redone in
about √(t log t) memory, so some linear-memory problems need nearly n² time. In 2025–2026 this was used to prove new
polynomial time lower bounds for natural problems (pushdown reachability needs N^{3/2} time, the first superlinear
bound for it; DFA intersection needs about n²), and OpenAI claims a T^{2/5}-memory simulation for one-tape machines. Still, no superlinear time lower bound
is known for the canonical PSPACE problem QBF, and nothing extends to random-access machines. After the October 2026
refutation of ETH, Strassle and Subercaseaux showed that nondeterministic time t can be simulated deterministically in
time 2^{O(t/√log t)}, and Charlie Cruz claims (with his own Lean proof, unreviewed) that it fits in O(t/√log t)
memory, which would separate nondeterministic linear time from deterministic linear space. In the fine-grained world,
Orthogonal Vectors, CNF-SAT with unbounded clause width and "Weak ETH" (no 2^{n^{1−ε}} 3-SAT algorithm) still stand,
while Subset Sum below 2^{n/2} is now claimed by two groups. None of this settles P vs NP, and experts moved only
slightly (Aaronson: P = NP from 3% to 5%). The cheapest high-value things for the lab are an independent audit of the
new Lean-checked claims and Lean formalization of the classical time–space lower bounds.

---

## 2. Frontier table

### 2.1 L vs NP: time–space lower bounds for SAT and NP (uniform, random-access machines)

Model unless stated: deterministic random-access Turing machines ("RAMs"); `DTISP(n^c, n^d)` = time n^{c+o(1)} and
space n^{d+o(1)}; `DTS(n^c)` = `DTISP(n^c, n^{o(1)})`. All bounds hold for NTIME(n) and, through quasi-linear
reductions, for essentially all standard NP-complete problems [vM07 §1].

| id | precise statement | reference | checked |
|---|---|---|---|
| U1 | ∀ε > 0, SAT cannot be solved by **both** (i) a (co-non)deterministic RAM in time n^{1+o(1)} and (ii) a (co-non)deterministic RAM in polynomial time and space n^{1−ε}. In particular SAT ∉ DTISP(n^{1+o(1)}, n^{1−ε}). | L. Fortnow, "Time-space tradeoffs for satisfiability", JCSS 60:337–353 (2000); CCC 1997 [For00] | yes (via [vM07] Thm 1.1) |
| U2 | SAT ∉ DTS(n^{√2 − o(1)}) (formally: ∀f = o(1) ∃g = o(1): no algorithm runs in time n^{√2−g(n)} and space n^{f(n)}) | R. Lipton, A. Viglas, "On the complexity of SAT", FOCS 1999, 459–464 [LV99] | yes (via [vM07] p. 199 and fn. 1) |
| U3 | ∀c < φ ≈ 1.618 ∃d > 0: no deterministic RAM solves SAT in time n^c and space n^d; d → 1 as c → 1. On co-nondeterministic RAMs the same for every c < √2. Applies to NTIME(n), to "almost all natural NP-complete problems", and even to languages solvable nondeterministically in linear time and space n^{1/c}. | L. Fortnow, R. Lipton, D. van Melkebeek, A. Viglas, "Time-space lower bounds for satisfiability", J. ACM 52:835–865 (2005) [FLvMV05] | yes (abstract) |
| U4 | Intermediate records SAT ∉ DTS(n^{√3−o(1)}) (≈1.732) and n^{1.759} | R. Williams, CCC 2005 [Wil05]; journal version "Inductive time-space lower bounds for SAT…" | no (search snippet only) |
| U5 | **Record.** For every c > 1 with c³ − c² − 2c + 1 < 0 (i.e. c < 2cos(π/7) ≈ 1.8019; "c < 1.801 suffices"): SAT, MOD₆-SAT, MOD_m-SAT for every composite m that is not a prime power, and MOD_p-SAT for all primes p with at most one (unidentified) exception, are not solvable on RAMs in time n^c and space n^{o(1)}. | R. Williams, "Time-space tradeoffs for counting NP solutions modulo integers", CCC 2007, 70–82; Comput. Complex. 17(2):179–219 (2008); ECCC TR07-036 [Wil07] | yes (ECCC abstract; [vM07] Thm 1.2) |
| U6 | "Master theorem" (deterministic): ∀c, d with (c−1)d < 1 **or** cd(d−1) − 2d + 1 < 0, ∃e > 0: SAT cannot be solved by both a co-nondeterministic RAM in time n^c and a deterministic RAM in time n^d and space n^e; e → 1 as c → 1 with d fixed. c = d gives φ (first condition) and 2cos(π/7) (second). | D. van Melkebeek, "A survey of lower bounds for satisfiability and related problems", FnT TCS 2(3):197–303 (2006/07), Thm 1.3 [vM07] | yes |
| U7 | **Method limit.** With the alternation-trading inference rules R0–R2 (all known speedup/slowdown arguments), a contradiction from SAT ∈ DTS(n^c) is derivable **only for c < 2cos(π/7)** (proves Williams' conjecture). For space n^ε the largest c provable by alternation trading (5 digits): ε = 0.001: 1.80083; 0.01: 1.79092; 0.1: 1.69618; 0.25: 1.55242; 0.5: 1.34070; 0.75: 1.15765; 0.9: 1.06011; 0.99: 1.00583; 0.999: 1.00058 (the search also proves no proof exists for the next value). | S. Buss, R. Williams, "Limits on alternation-trading proofs for time-space lower bounds", CCC 2012; Comput. Complex. 24(3):533–600 (2015); ECCC TR11-031 [BW15], Thm 1.1, Fig. 8.2 | yes |
| U8 | Earlier tradeoff form: SAT ∈ DTISP(n^c, n^ε) ⇒ c + ε ≥ 1.573 | [FLvMV05] as stated in [BW15] §1 | yes (via [BW15]) |
| U9 | Tautologies on **nondeterministic** RAMs: no algorithm in time n^{∛4 − o(1)} (∛4 ≈ 1.587) and space n^{o(1)}. Master theorem (nondeterministic): ∀c, d with (c² − 1)d < c or c²d < 4 ∃e > 0: TAUT not solvable by both a nondeterministic RAM in time n^c and one in time n^d, space n^e. | S. Diehl, D. van Melkebeek, R. Williams, UW-Madison TR 1601 (2007) [DvMW]; [vM07] Thm 1.4, 1.5 | yes (via [vM07]) |
| U10 | Randomized: ∀d < 2 ∃e > 0: Σ₂SAT cannot be solved by a two-sided-error randomized RAM in time n^d and space n^e (e → 1/2 as d → 1); for k ≥ 3, Σ_kSAT for every d < k. TAUT on one-sided-error randomized machines: n^{2cos(π/7)−o(1)} at subpolynomial space. **No nontrivial lower bound for SAT itself on two-sided-error machines** (as of the survey). | S. Diehl, D. van Melkebeek, SICOMP 36:563–594 (2006) [DvM06]; [vM07] Thm 1.7, 7.6, §1 | yes (via [vM07]) |
| U11 | Quantum: ∀ε > 0 ∃d > 1: MajMajSAT has no two-sided-error quantum algorithm in time n^d and space n^{1−ε}. | D. van Melkebeek, T. Watson (2007), using Allender et al.; [vM07] Thm 1.8, Cor 1.2 | yes (via [vM07]) |
| U12 | **Without a space bound nothing superlinear is known:** "To date no better time lower bound than the trivial one is known on unrestricted random-access machines" (2004); the indirect-diagonalization arguments "critically rely on sublinear space bounds" and "all the ingredients we use relativize" (relative to a TQBF oracle all the models are quasi-linear-time equivalent). My Oct–Nov 2026 searches found no claim otherwise. | [FLvMV05] §1; [vM07] Ch. 9 | yes |
| U13 | Textbook instance: NTIME(n) ⊄ TISP(n^{1.2}, n^{0.2}) | S. Arora, B. Barak (2009) §5.4, as quoted in cslib-frontier issue #2896 | no (secondary) |
| U14 | Kannan: nondeterministic multitape machines are more powerful than deterministic multitape machines with an additional space bound growing strictly more slowly than their time bound; nondeterministic 2-tape beats deterministic 1-tape | R. Kannan, Math. Systems Theory 17:29–45 (1984) [Kan84] and an earlier Kannan paper | yes (via [PPST83] §1) |
| U15 | Stated amplification route: if one could prove "SAT ∈ TIMESPACE[n^{O(1)}, log n] ⇒ SAT ∈ TIMESPACE[n^{1.1}, n^{0.7}]", then NP ≠ L would follow from the known tradeoffs (U3, U7) | R. Lipton, R. Williams, Comput. Complex. 22(2):311–343 (2013), §1 [LW13] | yes |

### 2.2 Model-independent (branching-program) time–space bounds for problems in P

Branching programs (BPs) are non-uniform: time T = length, space S = log(size). These bounds therefore also hold for
every uniform model.

| id | precise statement | reference | checked |
|---|---|---|---|
| B1 | ∀k ≥ 1, ∀ sufficiently small ε > 0, n large: no Boolean (2-way) BP of size < 2^{εn} computes, in time kn, the parity of #{⟨x, y⟩ : x, y ∈ X, x < y, x + y ∈ X} for inputs X ⊆ {0, …, n−1} (a function in P). Key lemma: rank of every δn × δn submatrix of a random Hankel-type GF(2) matrix ≥ cδ·\|log δ\|^{−2}·n. | M. Ajtai, "A non-linear time lower bound for Boolean branching programs", Theory of Computing 1(8):149–176 (2005); FOCS 1999 [Ajt05] | yes |
| B2 | For multi-way BPs, any linear-time algorithm for element distinctness (ED) must use linear space | M. Ajtai (1999), as stated in [BC13] §1 | yes (via [BC13]) |
| B3 | Randomized (two-sided error, even arbitrary error on a small fraction of inputs) Boolean BPs, for Ajtai's functions: T = Ω(n·√(log(n/S)/log log(n/S))); for S = O(n^{1−ε}): T = Ω(n√(log n/log log n)). (Optimizing Ajtai's own argument gives T = Ω(n log log n/log log log n) for S = O(n^{1−ε}).) | P. Beame, M. Saks, X. Sun, E. Vee, FOCS 2000, 169–179; J. ACM 50(2):154–195 (2003); ECCC TR00-025 [BSSV03] | yes (FOCS abstract) |
| B4 | ED on multi-way BPs with S = n^{o(1)}: T ∈ Ω(n√(log(n/S)/log log(n/S))) | [BSSV03] as stated in [BC13] §1 | yes (via [BC13]) |
| B5 | "The largest lower bound known for multi-way branching programs computing **any** single-output problem in P is only T ∈ Ω(n log((n log n)/S))" (2013 statement) | P. Beame, R. Clifford, "Element distinctness, frequency moments, and sliding windows", arXiv:1309.3690 (2013) [BC13] | yes |
| B6 | ED is not the route to quadratic bounds: randomized multi-way BP for ED in T ∈ Õ(n^{3/2}/S^{1/2}) for every S ∈ [c log n, n] | [BC13] | yes |
| B7 | Open-problem statement: an n^{1+Ω(1)} time lower bound for decision problems with polylog(n) space is "long-standing open"; they prove T²S = Ω(n^{2.5}/log n) for deterministic **oblivious** BPs on a multi-output function that has an O(log n)-space, O(n log n)-time randomized oblivious algorithm | H. Yu, W. Zhan, arXiv:2306.15817 (2023) [YZ23] | yes (abstract) |
| B8 | Beame–Jayram–Saks (first Boolean BP tradeoff, quadratic forms over GF(2)) and Beame–Vee (multiparty-communication method; larger tradeoffs on large domains) | JCSS 63(4):542–572 (2001) [BJS01]; STOC 2002, 688–697 [BV02] | no (titles/venues only; bounds not opened) |
| B9 | Quadratic time–space lower bounds for natural functions relative to a random oracle | D. McKay, R. Williams, ITCS 2019 | no (not opened) |
| B10 | Catalytic memory provably helps time-and-space-bounded computation: with O(log n) free space and poly(n) catalytic space (natural output model), sorting and DFT in n^{1+o(1)} time and matrix multiplication in n^{ω+o(1)}, beating the Ω(n²) / Ω(n³) time–space product lower bounds that hold without catalytic space (Borodin–Cook, Beame, Yesha, Abrahamson) | A. Morrison Orozco, N. Sheffield, R. Williams, arXiv:2610.24377 (17 Oct 2026) [MSW26] | yes (abstract) |

### 2.3 Time versus space (P vs PSPACE direction): simulations

Model: multitape TMs unless stated; TIME/SPACE = deterministic.

| id | precise statement | reference | checked |
|---|---|---|---|
| S1 | TIME[t] ⊆ SPACE[O(t/log t)] (multitape) | J. Hopcroft, W. Paul, L. Valiant, FOCS 1975; J. ACM 24(2):332–337 (1977) [HPV77] | yes (via [Wil25] abstract) |
| S2 | O(t/log t)-space simulations of time t exist for random-access and multidimensional models | W. Paul, R. Reischuk, JCSS 22(3):312–327 (1981) [PR81]; J. Halpern, M. Loui, A. Meyer, D. Weise, Math. Syst. Theory 19(1):13–28 (1986) [HLMW86] | yes (via [Wil25] §5) |
| S3 | Pebbling lower bounds were "a major bottleneck to improving [HPV75]"; the Cook–Mertz procedure "definitely breaks space lower bounds for pebbling DAGs and trees" | [Wil25] §5 | yes |
| S4 | Best known alternation speedup: TIME[t] ⊆ ATIME[t/log t] | P. Dymond, M. Tompa, JCSS 30(2):149–161 (1985) [DT85] | yes (via [Wil25] §5) |
| S5 | One writable tape: time t in space O(√t) (Hopcroft–Ullman 1968; Paterson 1972); nondeterministic one-tape: NTIME₁[t] ⊆ NSPACE₁[O(√t)] ⊆ DTIME[2^{O(√t)}] (needs t ≥ n²) | [HU68], [Pat72] via [Wil25] §5; chain via [SS26] §1.1 | yes (via [Wil25], [SS26]) |
| S6 | Tree Evaluation in space O(log n · log log n) (and time n^{O(log log n)}), improving O(log² n/log log n) (Cook–Mertz 2020); Ω(log² n) space lower bounds are known only for restricted models. Consequences stated: KRW would imply L ≠ NC¹; every n-bit function has amortized/catalytic BPs of length poly(n), width 2^{O(n)}. | J. Cook, I. Mertz, "Tree Evaluation is in Space O(log n · log log n)", STOC 2024, 1268–1278; ECCC TR23-174 [CM24] | yes (abstract; time bound via [HPR26]) |
| S7 | **Williams 2025.** Thm 1.1: ∀t(n) ≥ n, TIME[t] ⊆ SPACE[√(t log t)]. Cor 1.2: ∀ space-constructible s(n) ≥ n, ∀ε > 0, SPACE[s] ⊄ TIME[s^{2−ε}]. Cor 1.3: L = {⟨M, x, 1^k⟩ : \|M\| ≤ k and M(x) halts in space k} requires n^{2−ε} time on multitape TMs ∀ε > 0. Cor 1.4: ∃ universal k: every bounded fan-in circuit of size s ≥ n has a branching program of size ≤ 2^{k√s log^k s}. Thm 1.5: d-dimensional multitape time t ⊆ SPACE[(t log t)^{1−1/(d+1)}]. Remark 1.6: no extension to arbitrary random-access models (in-degree too high); yes for oblivious ones. Cor 3.6: TreeEval ∈ L ⇒ TIME[t] ⊆ SPACE[√t]. Thm 5.1 (restricted relativization): ∀ oracle A, TIME-LENGTH^A[t, √(t log t)] ⊆ SPACE-LENGTH^A[√(t log t), √(t log t)]. Non-relativizing in general. | R. Williams, "Simulating Time With Square-Root Space", arXiv:2502.17779v1 (25 Feb 2025); STOC 2025 (doi:10.1145/3717823.3718225); ECCC TR25-017 [Wil25] | yes |
| S7b | Stated open: whether TIME[t] ⊄ Σ₂TIME[t^{1−ε}] ("remains open and almost certainly cannot be refuted using the ideas of this paper"; it would suffice for the Nisan–Wigderson subexponential derandomization of BPP) | [Wil25] §1, footnote 2 | yes |
| S8 | Journal version: J. ACM, published 16 Jun 2026, doi:10.1145/3798104 | search snippet; DOI page returned 403 | no |
| S9 | Circuit evaluation for size-s bounded fan-in circuits in O(√(s log s)) space, by a direct reduction to Tree Evaluation; recovers time-t TMs in O(√t · log t) space | Y. Shalunov, arXiv:2504.20950 (v2 19 Jun 2025); ECCC TR25-078 [Sha25] | yes (abstract) |
| S10 | Extension of Williams' reduction to a strengthened parallel external-memory model; applications: Lex-First 2SAT (P-complete) in Õ(√n) space; unbounded fan-in {NOT, AND, OR, XOR} circuits with n gates evaluable in O(√(n log n)) space; d-dimensional cellular automata, t steps, in O((t log t)^{1−1/(d+1)}) space. No o(t)-space claim for general RAMs. | D. Sibgatullin, R. Williams, "Space-Efficient Simulations Beyond Multitape Turing Machines", ECCC TR26-223 (2 Oct 2026) [SiW26]; also Williams' MFCS 2026 invited talk [Wil26m] | yes (abstract summary) |
| S11 | Catalytic TreeEval with O(log n) free space, polynomial time and 2^{O(log^ε n)} catalytic space ∀ε > 0 (previous catalytic: O(log n) free, poly time, O(√n) catalytic, Cook–Mertz STOC 2020); implies an improved simulation of time by catalytic space via [Wil25]. Framework: matching-vector families + "decoders". | A. Henzinger, E. Pyne, S. Ragavan, arXiv:2602.14320 (v3 8 Nov 2026); ECCC TR26-022 [HPR26] | yes (abstract) |
| S12 | Conditional "plasticity": under average-case hardness of (a low-space variant of) Range Avoidance, t-time algorithms can be simulated in space t^ε (∀ε > 0) correctly on average over random inputs, and in linear time with enough alternations; some assumption is necessary because the conclusion implies P ≠ PSPACE | Z. Li, R. Tell, ECCC TR26-233 (7 Oct 2026) [LiT26] | yes (abstract summary) |
| S13 | **One writable tape, claimed [AI]:** a fixed deterministic machine with one writable tape (plus finitely many read-only input heads, unit moves) is simulated, given a binary time cap T ≥ 2, in O(T^{2/5} polylog(T+2)) work-space bits (unrestricted simulation time); answers Williams' one-tape question; **not** a 2/5 bound for multitape machines (§4 of the paper gives only Õ(√T) for any fixed number of writable tapes). Lean statement via Comparator (`OneTapeSpace.lean`). | OpenAI, "Simulating One-Tape Time in Two-Fifths-Power Space", OpenAI Math Release, 25 Sep 2026 (github.com/openai/math, family 137) [OAI26t] | yes (paper abstract + §1; Lean scope doc; not built) |
| S14 | Relative to a random oracle with O(log n)-bit answers, some function computable in O(n) time on a RAM requires n²/polylog(n) time on every multitape TM | L. Chen, Y. Wang, ECCC TR26-006 (Jan 2026) [ChW26] | yes (abstract) |
| S15 | Space hierarchy corollaries formalized: SPACE(n) ⊄ TIME(n^{2−ε}) and TIME(n²/(log₂ n + 1)²) ⊊ SPACE(n) | cslib-frontier `Classes/TimeSpace/WilliamsSeparation.lean` (commit 1435284b) | yes (source read; not built) |

### 2.4 Unconditional time lower bounds for explicit problems (and QBF)

| id | precise statement | reference | checked |
|---|---|---|---|
| L1 | A linear-space PSPACE-complete language (bounded-space halting, S7 Cor 1.3) needs n^{2−ε} multitape time | [Wil25] Cor 1.3 | yes |
| L2 | DFA intersection non-emptiness (PSPACE-complete; number of DFAs part of input): unconditional time lower bound Ω(n²/(log³ n (log log n)²)), via [Wil25] + space hierarchy (multitape model per [BM26] §1) | M. Wehar, arXiv:2512.00297 (v1 29 Nov 2025, v2 23 Mar 2026) [Weh25] | yes (abstract; model via [BM26]) |
| L3 | **Pushdown reachability** (PDA emptiness; in P, cubic upper bound): ∀ε > 0 no deterministic multitape TM decides it in O(N^{3/2−ε}) time, already for sparse instances; transfers to quasi-linear-equivalent program-analysis problems (CFL reachability, 2NPDA recognition, …). Proof: TM runs → locally-addressable circuits with H = ⌈log₂(8T)⌉-bit addresses (via [Sha25]) → "relation programs" → PDA of size ≈ T^{2/3}. AI statement: "GPT 6.1-Sol found the proof of the lower bound completely by itself". | A. R. Balasubramanian, R. Majumdar, arXiv:2611.27814 (20 Nov 2026) [BM26] Thm 1 [AI] | yes (PDF §1, §7) |
| L4 | Intersection non-emptiness of one PDA and k−1 NFAs: no O(N^{3k/2−ε}) multitape algorithm, ∀ fixed k ≥ 1, ε > 0 (for k = 2: not truly subcubic) | [BM26] Thm 2 | yes |
| L5 | Earlier: intersection of a PDA and k−1 DFAs needs n^{ck} for an unspecified constant c (no nontrivial bound for PDA reachability itself); Ω(n^k) lower bounds for fixed-pebble combinatorial games in P; Cook's AuxPDA characterization transfers DTIME(n^k) bounds | J. Swernofsky, M. Wehar, ICALP 2015, LNCS 9135:414–426; A. Adachi, S. Iwata, T. Kasai (1984); S. Cook (J. ACM 1971) | yes (via [BM26] §1) |
| L6 | **Claimed [AI]:** ∀ sufficiently large fixed k, deciding k-dimensional Weisfeiler–Leman equivalence of two n-vertex graphs (explicit adjacency matrices; even connected, uncolored, diameter ≤ 2) requires n^{Ω(k)} deterministic time on multitape TMs and on sequential log-word RAMs (Lean scope: ≥ n^{ck} for one absolute c > 0); with k in binary the problem is EXPTIME-complete (even subcubic graphs) | OpenAI, "Unconditional time lower bounds for Weisfeiler–Leman equivalence" + 3 companions, 25 Sep 2026 (family 133) [OAI26w] | yes (catalogue abstract + Lean scope doc `lean/docs/133.md`; paper not opened) |
| L7 | PPST's proof gives Ω(n(log* n)^{1/4}) for any language complete for NTIME(n) under deterministic linear-time reductions; Grandjean exhibited natural NP problems of this kind | [PPST83]; E. Grandjean (SIAM J. Comput.) — as stated in [BM26] §1 | yes (via [BM26]) |
| L8 | Succinct QBF (a slight generalization of QBF) requires non-linear time on multitape TMs, random-access TMs, tree computers and log-cost RAMs (reduction from alternating time t(n) to instances of size O(t(n)) + diagonalization) | R. Williams, ECCC TR08-076 (2008) [Wil08q] | yes (abstract) |
| L9 | For c, d > 1, e < 1 with c < (1 − e + d)/d: either QBF ∉ TIME[n^c] or Circuit Evaluation has no n^d-size, n^e-depth circuits; QBF has no n^c-time uniform NC circuits for all c < 2 | [LW13] abstract | yes |
| L10 | **QBF itself:** no n^{1.0001} time lower bound for any PSPACE-hard problem solvable in linear space, "such as QBF" (2019); in 2025 Williams: a super-linear time lower bound for QBF "is still open". After 2025 the first half no longer holds for multitape TMs (L1, L2), the QBF half does; no 2026 claim found. | [Wil19] §2.6; [Wil25] §5 | yes |
| L11 | Lead-scout inference (folklore-level): QBF ∉ SPACE[N^{1/2−ε}] (linear space reduces to QBF instances of size O(n²) by the Savitch-style formula, then the space hierarchy), so time–space bounds for QBF are only interesting above space √N | my derivation | no (inference) |
| L12 | Claimed: deterministic multitape TM stably sorts n binary keys (N total bits) in O(N log n/(log log log n)^η) time, O(N) space, explicit η > 0; the Ω(N log N) bound for comparison-and-copy algorithms does not extend to all multitape sorting | Y. Tal, ECCC TR26-331 (22 Nov 2026) [Tal26] | yes (abstract summary) |
| L13 | Claimed [AI]: two n-bit integers multiplied in deterministic O(n(log n)^{1−κ}) time, κ = 2^{−182}, on one fixed multitape TM, "disproving" the Schönhage–Strassen n log n optimality conjecture in that model | OpenAI, "Integer multiplication below n log n", 23 Sep 2026 (family 109) [OAI26m] | yes (catalogue abstract; no Lean scope doc found) |
| L14 | One-tape classics (formalized): a deterministic single-tape TM deciding palindromes needs Ω(n²) (Hennie); single-tape time o(n log n) ⇒ regular language (Trakhtenbrot 1964, Hartmanis 1968, Kobayashi 1985) | cslib-frontier `Machines/Turing/SingleTape/Palindrome.lean`, `NLogNGap.lean` | yes (docstrings read; not built) |

### 2.5 Nondeterministic versus deterministic time and space

| id | precise statement | reference | checked |
|---|---|---|---|
| N1 | DTIME(n) ≠ NTIME(n) for multitape TMs: some language accepted by a 2-tape NTM in linear time is accepted by no multitape DTM in linear time (read-only input tape). Key step (Thm 3.3): ∀ time-constructible f ≥ n log* n, DTIME(f) ⊆ Σ₄TIME(f/log* f), via a "segregator theorem" for block-respecting computation graphs. | W. Paul, N. Pippenger, E. Szemerédi, W. Trotter, "On determinism versus non-determinism and related problems", FOCS 1983, 429–438 [PPST83] | yes (PDF) |
| N2 | DTIME(n√(log* n)) ≠ NTIME(n√(log* n)); at least one of {P ≠ L, ∀ constructible t: DTIME(t) ≠ NTIME(t)} holds; whether NTIME(t) = NSPACE(t) is tied to sublinear separators for certain graph families | R. Santhanam, "On separators, segregators and time versus space", CCC 2001, 286–294; ECCC TR01-022 [San01] | yes (abstract) |
| N3 | DTIME(t) ⊊ Σ₂TIME(t) for time-constructible t (Gupta) | as stated in M. Hauptmann, arXiv:1602.04781 abstract | no (secondary) |
| N4 | Lipton's conjecture "∀ε > 0: NTIME[t] ⊆ DTIME[2^{εt}]" (2009) was open until Nov 2026; Kalyanasundaram–Lipton–Regan–Shokrieh improved the constant c in DTIME[2^{ct}]; the conjecture is false relative to some oracles (Moran 1981, Doty 2010) and, by Bennett–Gill, relative to a random oracle — so any proof is non-relativizing | [SS26] §1.1 citing [Lip09], [KLRS12] TCS 417:66–73, [Mor81], [Dot10] | yes (via [SS26]) |
| N5 | **Claimed (Nov 2026).** Thm 1: ∀t(n) ≥ n, NTIME[t] ⊆ DTIME[2^{O(t/√log t)}] (multitape); from the published 3-SAT bounds only 2^{O(t log log t/√log t)}. Thm 2 (transfer): if circuit-CSP with n variables, arity ≤ k(n), density ≤ 2 is solvable in 2^{O(n/s(n))}·poly(\|Φ\|) (2 ≤ s(n) ≤ n/log n) then NTIME[t] ⊆ DTIME[2^{O(t/k(t))}·2^{O(t/s(t))}]. Thm 3: 3-SAT with O(n) clauses in 2^{O(n/s(n))} ⇒ NTIME[t] ⊆ DTIME[2^{O(t log s(t)/s(t))}]. Lemma 2.1 (generalized Cook–Levin): 2^{O(t/b)} circuit-CSPs, each with O(t) variables, arity O(b), density ≤ 2, O(t/b) circuits of size O(b log b). Improving quasilinear Cook–Levin (O(t log t) variables) is called "a long-standing open problem". | C. Strassle, B. Subercaseaux, arXiv:2611.11832 (9 Nov 2026) [SS26] (already in KNOWN_RESULTS; details added here) | yes (PDF §1–2) |
| N6 | **Claimed (Nov 2026), Lean-checked by the author.** Thm 1.1: ∀t(n) ≥ n (t need not be constructible), NTIME[t] ⊆ SPACE[O(t/√log t)] (deterministic multitape; simulator time 2^{O(t/√log t)}). Cor 1.2: (i) NTIME[n] ⊊ SPACE[n], and NTIME[t] ⊊ SPACE[t], NTIME[t] ⊊ NSPACE[t] for space-constructible t ≥ n (answers Santhanam's question N2 negatively); (ii) NTIME[t√log t] ⊆ SPACE[t]; (iii) ∃L ∈ SPACE[n] such that every NTM deciding L or its complement needs ≥ c·n√log n steps on some input of every large length; (iv) PPTIME[t] ⊊ SPACE[t], BPTIME[n] ⊊ SPACE[n]. Thm 7.1: PPTIME, BPTIME, ⊕TIME, Mod_qTIME, C₌TIME ⊆ SPACE[t/√log t]. Remark 8.3: does not relativize (oracle BSA). Method: count accepting choice strings; HPV blocking (head schedule O(t/log t) bits) turns each schedule into a network of size O(t); Anthropic-style grid recursion with new signed "pieces" from walks on the Boolean cube, evaluated depth-first bit by bit. Lean: CSLib Frontier `NTIME`/`DSPACE` over `encBits`, only `propext`, `Classical.choice`, `Quot.sound`, Comparator against CSLib-Frontier-only statements (`ntime_ssubset_dspace`). | C. Cruz, "Separating Nondeterministic Time from Deterministic Space", github.com/SeniorMars/ntime.dspace (paper dated 10 Nov 2026; PDF built 22 Nov 2026) [Cru26] | yes (PDF, README, lean/README; Lean not built) |
| N7 | cslib-frontier issue #2226 (opened 1 Nov 2026) records the earlier form of Cruz's claim: NTIME(T) ⊆ DSPACE(T(log log T)²/√log T), hence NTIME(n) ⊊ DSPACE(n); draft PR #2231 covers a first milestone only. **Two versions of the bound exist; report both.** | github.com/cslib-community/cslib-frontier/issues/2226 | yes (issue page via WebFetch) |
| N8 | Parallel claims reported by Cruz: R. Yang (working with T. Pitassi; with Claude Opus 5.5) NTIME[T] ⊆ SPACE[T(log log T)²/√log T]; S. McGuire the bound t/√log t (personal communication) and a note (30 Oct 2026) simulating NTIME and BPTIME t in DTIME 2^{O(t/√log t)} | [Cru26] §1.2 | no (not opened) |
| N9 | NTIME(T) ⊆ DTIME(2^{O(T(log log T)³/√log T)}) via Subercaseaux's encoding (exposition); NTIME_RA[t] ⊆ DTIME[2^{O(t/√log t)}] for random-access NTMs (blog comment citing a Williams tweet) | survey 01 E1 (O'Donnell); ethdiscussion.blog comment by N. Chukhin, 2 Nov 2026 | no (I did not open either) |
| N10 | Formalized: NTIME[T], BPTIME[T], PPTIME[T] ⊆ ⋃_C DTIME[2^{C·T/√⌊log₂ T⌋}] with workspace T^d, and exact #TIME[T] counts (uses OpenAI Thm D.1); NTIME[T] ⊊ DTIME[2^T] and NTIME[T·⌊√⌊√⌊log₂ T⌋⌋⌋] ⊊ DTIME[2^T] for time-constructible T with max(n, 2) ≤ T(n) | cslib-frontier `Classes/CountingSimulation/FastSimulation.lean`, `CountingClasses.lean`, `Separation.lean` (issues #1833, #2050 closed) | yes (source read; no `sorry` by grep; not built) |

**Sanity check of Cruz's claim N6 (lead-scout inference, `informal-argument`; this is not a proof check).**
(1) It implies NTIME[t] ⊆ DTIME[2^{O(t/√log t)}], which agrees with N5. (2) It contradicts no known theorem: the
strictness of NTIME(n) ⊆ DSPACE(n) was open (Santhanam's 2001 question N2; [Cru26] §1: no earlier o(t)-space simulation
of multitape NTIME; survey 01's cross-checker found no cheap derivation, and noted that NTIME(n) = DSPACE(n) would give
NP = PSPACE by padding). (3) Its #3-SAT corollary (bits of the count in space O(m/√log m), time 2^{O(m/√log m)})
matches the known counting time of [Ant26]/[OAI26]. (4) It is non-relativizing, as any such result must be
([Cru26] Remark 8.3; N4). (5) The two published forms of the bound differ (N6 vs N7). Verdict: plausible and
unrefuted, not independently verified; see V1 in §4.2. Do not cite it as established.

### 2.6 The post-ETH fine-grained landscape: additions to survey 01's ledger, and best SAT/QBF algorithms

Status of ETH, SETH, NSETH, #ETH, Gap-ETH, Weak ETH/SH, OV, CNF-SAT, Max-kSAT, k-Clique, hyperclique: see survey 01
§2.5 (and its cross-check). Rows below add what survey 01 lacks.

| id | precise statement | reference | checked |
|---|---|---|---|
| F1 | OV with d = c log n solvable in n^{2−1/O(log c)} (randomized), derandomized later; no n^{2−ε}·poly(d) known | A. Abboud, R. Williams, H. Yu, SODA 2015; T. Chan, R. Williams, SODA 2016 | no (snippets) |
| F2 | OV hypothesis stands as of Nov 2026: "Theorem 1 does *not* refute the Orthogonal Vectors hypothesis" (Anthropic); k-OV conjecture proved only for constant-depth circuits; "remains open even for k=2" (Chukhin, 4 Nov 2026) | survey 01 §2.5 and its cross-check | no (I did not reopen) |
| F3 | CNF-SAT with m clauses in 2^{n(1−1/O(log(m/n)))}·poly(m) (Calabro–Impagliazzo–Paturi 2006; Dantsin–Hirsch); no 2^{(1−δ)n} for unbounded width | CIP06 (CCC 2006) as attributed by Pătraşcu–Williams | no (symbols lost in PDF extraction) |
| F4 | 3SUM in O(n^{1.9992}), APSP in O(n^{2.9995}) (arXiv abstract); the Anthropic Lean project states "(min,+)-product and APSP in O(n^{2.99942}) steps" on word RAMs. **The two exponents differ; report both.** Refuted hypotheses listed: 3SUM, APSP, real-valued 3SUM/APSP, Exact Triangle, Zero-Weight k-Clique, the three rectangular hinted OMv conjectures (van den Brand–Nanongkai–Saranurak). The standard OMv conjecture is not listed; I found no refutation of it. | J. Alman, V. Vassilevska Williams, arXiv:2610.06783 (5 Oct 2026); github.com/anthropics/formal-math `3sum-apsp/` README | yes (abstract; README) |
| F5 | Independent simplified proofs: selected-entry matrix multiplication (Schönhage inner/outer identity) gives truly subquadratic 3SUM and truly subcubic APSP with weaker exponents; randomized truly subquadratic integer 3SUM without matrix multiplication; odd-k k-SUM in O(n^{⌈k/2⌉−ε_k}); deterministic reductions for real 3SUM/APSP | S. R. Karingula, S. Lovett, ECCC TR26-247 / arXiv:2610.15663 (Oct 2026); T. Chan, R. Itakura, Z. Ma, Y. Yu, arXiv:2610.42012 (v2 14 Nov 2026) | yes (abstracts) |
| F6 | **Subset Sum below 2^{n/2} (claimed).** Randomized O(2^{0.49999977n}) via "partial match" (extends Randolph–Węgrzycki, STOC 2026; uses Alman–Li FOCS 2025 depth-2 linear circuits); and, claimed [AI], randomized O(2^{0.49n}) word-RAM time, plus poly(n)·2^{n/2} time with O(2^{n/5}) words of space | B. Li, L. Ye, arXiv:2610.10446 (v2 2 Nov 2026); OpenAI, "Subset Sum in Time O(2^{0.49n})" (4 Oct 2026) and "A Low-Space Algorithm for Worst-Case Subset Sum" (26 Sep 2026), family 138 | yes (abstract; catalogue abstracts) |
| F7 | Deterministic 3-SAT in 1.32736^n (practical-regime record; branching + chains) | B. Cui, S. C. Liu, Y. Yu, arXiv:2611.16814 (12 Nov 2026) | yes (abstract) |
| F8 | Randomized (unmodified) PPSZ: Unique-3-SAT in O*(1.306969598^n), general 3-SAT in O*(1.307031578^n) (via Scheder–Steinberger lifting) | T. Jiang, S. Cai, arXiv:2607.10697 (v2 27 Oct 2026) | yes (abstract) |
| F9 | Galactic: #k-SAT in 2^{O(n/√log n)}-type bounds (OpenAI, Anthropic); circuit-CSP with arity ≤ n^{9/10} and constant density in 2^{O(n/√log n)}·poly(\|Φ\|) | survey 01 F1–F9; [SS26] Fact 1.3 | yes (via [SS26]) |
| F10 | QBF (n variables, m clauses) in 1.685^m·poly(n) time and space (memoized search on conflict-graph vertex covers); previous best 1.709^m (Williams) | Z. Chen, H. Yao, arXiv:2611.10633 (7 Nov 2026) | yes (abstract) |
| F11 | QBF algorithms vs lower bounds: two-block quantified 3-CNF in deterministic 2^{n−Ω(√n)}·poly(m); q-block poly-size CNF in zero-error 2^{n−n^{1/(q+1)}}·poly(n); circuits of size s in 2^{n−Ω(q)}·poly(s); a 2^{n−n^{ω_q(1/q)}} algorithm for q-block poly-size CNF QBF (or 2^{n−ω(log n)} for O(log n) blocks) ⇒ NEXP lacks poly-size O(log n)-depth circuits | R. Santhanam, R. Williams, SODA 2015; ECCC TR13-108 (rev. Dec 2014) [SaW15] | yes (abstract) |
| F12 | New non-standard hypothesis in circulation: "self-referential K-SAT exhaustive-search hypothesis" (SRK-ESH) ⇒ no O(n^{2−η}) LCS/edit distance; via OV hardness in polylog dimension | G. Zhou, arXiv:2611.07308 (5 Nov 2026) | yes (abstract) |

### 2.7 Neighbouring 2026 space-complexity claims (context only)

| id | statement | reference | checked |
|---|---|---|---|
| C1 | Claimed [AI], Lean-checked by OpenAI's Comparator: L = RL = BPL (bounded-error randomized logspace equals deterministic logspace) | OpenAI, "Exact derandomization of logarithmic space: L = RL = BPL", 23 Sep 2026 (family 103; `lean/docs/103.md`) | yes (catalogue + Lean scope doc) |
| C2 | Claimed: NL = UL, via an O(log(wn))-space min-isolating weight generator plus Reinhardt–Allender | W. Hoza, ECCC TR26-323 (20 Nov 2026) | yes (abstract) |
| C3 | Unconditional separation of DSPACE(log log n) from its catalytic counterpart (POW2 with O(log log n) work + O(log n) catalytic) | S. Bhardwaj, ECCC TR26-252 / arXiv:2610.15554 (rev. 17 Oct 2026) | yes (abstract) |

None of C1–C3 touches L vs NP directly; they change the space-bounded landscape a lab working on L ≠ NP must cite.

### 2.8 Expert views and estimates

| id | statement | reference | checked |
|---|---|---|---|
| E1 | Williams' personal likelihoods: L ≠ NP 95%, P ≠ PSPACE 90%, P ≠ NP 80%, ETH 70%, SETH 25%, NSETH 15%. L ≠ NP will be proved "possibly long before P vs NP", but needs ideas of "a Gödel-incompleteness-level of cleverness". QBF "call to arms": "why can't we prove an n^{1.0001} time lower bound against solving QBF?" | R. Williams, "Some Estimated Likelihoods for Computational Complexity" (LNCS, 2019), Table 1, §2.3, §2.6 [Wil19] | yes |
| E2 | Williams, 23 Nov 2026 thread: a resolution in the next few months would require P = NP (and "polynomial time" might then need an ultrafinitist reformulation); if P ≠ NP, first resolve P ≠ PSPACE or L ≠ NP; "Prove that SAT on instances of length L doesn't have L^{1.01} size circuits first!" | director's screenshots, summarized in `00-director-sources.md` §2 | no (secondary) |
| E3 | Aaronson: raised P = NP from 3% to 5% after the ETH news (comment #4); a subexponential CircuitSAT algorithm (#18) or Weak ETH falling (#31) would raise it to 20–30%; ETH result "still a long way from P=NP" (#17) | S. Aaronson, Shtetl-Optimized ?p=10239, 26 Oct 2026 [Aar26] | yes |
| E4 | Fortnow: "I do not believe we will see a P v NP proof in my lifetime proven by man or machine"; "We know by relativization that simulation and diagonalization will not work"; "Don't waste your time trying a formal approach via Lean." | L. Fortnow, "Respect the P v NP Problem", Computational Complexity blog, 10 Jun 2026 [For26r] | yes |
| E5 | O'Donnell on Weak ETH: "I personally disbelieve it, but there is a much higher chance of it being true now" | survey 01 cross-check §2.4 item 5 | no (secondary) |
| E6 | 2019 poll: ~88% of respondents believe P ≠ NP | W. Gasarch, SIGACT News 50(1) 2019, as reported by Wikipedia | no (secondary) |

### 2.9 What a P = NP-direction programme would have to overcome (each item sourced)

1. **Unconditional uniform lower bounds that every SAT algorithm must respect:** n^{2cos(π/7)−o(1)} time at n^{o(1)}
   space (U5); the c(ε) tradeoff curve (U7); NTIME(n) ≠ DTIME(n) (N1). A polynomial SAT algorithm must use
   super-polylogarithmic space or ≥ n^{1.8} time. (It may still run in n^{1+o(1)} time with large space: U12.)
2. **Relativization and algebrization.** There is an oracle B with P^B ≠ NP^B [BGS75], so a P = NP proof cannot
   relativize either; the ETH-era simulations are already non-relativizing (N4; [Cru26] Remark 8.3). To my memory
   [AW09] states that resolving P vs NP in either direction needs non-algebrizing techniques (checked: no).
3. **Weak ETH / SH stands** and the new algebraic methods are provably stuck near 2^{n/polylog n}: Majdoddin's
   rewrite-and-merge class excludes 2^{n^{1−c}}, Dias–Lima's interpolation cost model gives 2^{Ω(√n)}, single
   contraction trees stop at ≈4/9, monotone/DNNF circuits need 2^{Ω(n)} (all in survey 01 §2.4 and KNOWN_RESULTS).
   Reaching NP ⊆ SUBEXP needs 2^{n^{o(1)}} for 3-SAT, because polynomial reductions lose 2^{o(n)} savings [OAI26 §1].
4. **Restricted algorithm classes have exponential lower bounds** (resolution, hence DPLL/CDCL). Examples: "Strong
   ETH holds for regular resolution" (Beck–Impagliazzo 2013, as quoted from [OAI26] in survey 01 L7; checked: no by
   me) and the ECCC title "Strong ETH Holds for Bounded-Depth Resolution over Parities" (Efremenko–Itsykson,
   TR25-188; title only). Cross-reference the proof-complexity survey (pending).
5. **Counting-based space simulations tie memory to #SAT speed:** an evaluator in space D(s) gives #3-SAT in time
   2^{O(D(O(m)))} ([Cru26] §8, Lean-proved implication). So pushing NTIME ⊆ SPACE[t^{1−ε}] by this route would refute
   Weak #ETH/#SH (⇔ by [MITHG26]); "NP ≠ PSPACE via counting" would need #3-SAT in 2^{m^{o(1)}}.
6. **Galactic constants.** All 2026 subexponential algorithms beat brute force only for astronomically large inputs
   (survey 01 L8), so even an eventual P = NP proof of this style need not be "practical" (cf. E2).

---

## 3. Key techniques and which barriers they hit or evade

| technique | what it gave | relativization | natural proofs | algebrization | other barriers / limits (cited) |
|---|---|---|---|---|---|
| Indirect diagonalization / alternation trading (Nepomnjaščiĭ–Kannan speedup TISP(t, s) ⊆ Σ₂TIME(√(ts)); slowdown from the contradiction hypothesis; nondeterministic time hierarchy) | U1–U11 | **Hits it**: "all the ingredients we use relativize", and relative to a TQBF oracle all the models are quasi-linear-time equivalent, so no time lower bound without a space bound [vM07 Ch. 9] | Not applicable (uniform diagonalization, not a property of truth tables) | Not analysed in sources I found | **Buss–Williams**: rules R0–R2 cannot beat 2cos(π/7) [BW15]; quadratic is the natural ceiling for subpolynomial space [vM07 Ch. 9]; randomized setting blocked by the black-box MA→AM overhead (Diehl) [vM07 Ch. 9] |
| Combinatorial BP lower bounds (Borodin–Razborov–Smolensky embedded rectangles; Ajtai's rank lemma; multiparty communication, Beame–Vee) | B1–B5 | N/A (non-uniform) | Not known to apply (specific functions; no largeness/constructiveness analysis found) | N/A | Stuck at T = Ω(n log((n log n)/S)) for single-output problems in P on multi-way BPs [BC13]; ED cannot give quadratic bounds (B6); n^{1+Ω(1)} at polylog space open [YZ23] |
| Block-respecting simulation + pebbling (HPV, PPST segregators) | S1, N1, N2 | **Evades** through tape locality: HPV and Cruz's simulation fail relative to the oracle BSA [Cru26] Remark 8.3; but these simulations survive length-restricted oracles (Tretkoff 1986 for "the simulation of TIME[t] in Σ₂TIME[o(t)], of PPST", as worded in [Wil25] §5; PPST's own paper states Σ₄TIME(f/log* f)) | N/A | N/A | Pebbling lower bounds cap pebbling methods at t/log t ([Wil25] §5; Paul–Tarjan–Celoni per cslib roadmap, checked: no) |
| Tree Evaluation / algebraic recomputation (Cook–Mertz low-degree extensions; Williams' reduction; Shalunov; Sibgatullin–Williams) | S6–S11, L1–L4 | **Evades in general, keeps restricted relativization** (length-restricted oracles, [Wil25] Thm 5.1) | N/A | Not analysed | Needs low-dimensional locality: random access gives too-high in-degree ([Wil25] Remark 1.6); recursion blocked because each block must compute a low-degree extension ([Wil25] §5); TreeEval ∈ L would only remove the √log factor (Cor 3.6); possible NNJAG barrier is open ([Wil25] §5) |
| One-tape block-visit factorization with interpolation (OpenAI) | S13 | Not stated | N/A | N/A | Works for one writable head; multitape gives only Õ(√T) [OAI26t] §1 |
| Counting through ETH-refutation algebra (HPV blocking + Anthropic/OpenAI decompositions) | N5, N6, N10 | **Must evade**: Lipton's conjecture is false relative to some oracles and to random oracles [SS26] §1.1; Cruz's bound fails relative to BSA [Cru26] | N/A | Not analysed | Space ↔ #SAT speed link ([Cru26] §8); OR/AND pieces cannot cancel (Prop. 8.1); signed integer pieces need squared-width factor ≥ 2 (Prop. 8.2); "pieces" capped at ρ ≥ 1/2 by a rank argument (survey 01 cross-check) |
| Diagonalization through completeness (EXPTIME-complete with k in input ⇒ n^{Ω(k)} for fixed k; space hierarchy + Williams + efficient reductions) | L1–L6 | Hierarchy part relativizes; the Williams step does not | N/A | N/A | Exponent limited by reduction efficiency: "caring about the particular constants" is essential ([BM26] §7) |
| Algorithmic method (fast SAT ⇒ circuit lower bounds) | survey 02 | survey 02 §3 | survey 02 §3 | survey 02 §3 | survey 02 §3 |
| Fine-grained reductions under SH (MIT Hardness Group) / OV | survey 01 C8 | N/A | N/A | N/A | Bounds lose arbitrarily small constants in the exponent (survey 01) |

Locality barrier (hardness magnification) and GCT no-go results do not apply to any technique in this area as far as
the sources show.

---

## 4. Open sub-problems ranked by tractability × impact

T = tractability for this lab now, I = impact on the mission; each 1–5. "Open" means: stated open in the cited source
and no claim found in my Oct–Nov 2026 searches (arXiv cs.CC Oct–Nov 2026 listings, cs.DS Nov 2026 listing, ECCC 2025
and 2026 listings, the OpenAI math catalogue, ethdiscussion.blog, cslib-frontier issues; see §11).

### 4.1 Ranked open problems

| # | problem | T | I | T×I | why these scores | stated open in | latest progress found |
|---|---|---|---|---|---|---|---|
| P1 | **A barrier for locality-based space simulations.** Define a model that captures HPV, Cook–Mertz/Williams, OpenAI's one-tape method and Cruz's counting simulation (e.g. length-restricted relativization, or an NNJAG-like model with algebraic recomputation) and prove that such simulations cannot reach TIME[t] ⊆ SPACE[t^ε] (the route to P ≠ PSPACE) | 3 | 3 | 9 | A new barrier is mission item 3; Williams names the question and supplies Thm 5.1 as a handle; Li–Tell show assumptions are needed for t^ε simulations, which hints at what a barrier must capture | [Wil25] §5 ("Is there a barrier to further progress?"; "Is there a barrier to improving such (restricted) relativizing results to obtain P ≠ PSPACE?") | Feb 2025 ([Wil25]); 7 Oct 2026 ([LiT26], conditional simulations) |
| P2 | **A superlinear time lower bound for QBF on multitape TMs**, e.g. by proving multitape TIME[t] ⊆ SPACE[t^{1/2−ε}] (then TIME[t] ⊆ ATIME[t^{1−2ε}], which gives QBF ∉ TIME[n^{1+δ}]), extending OpenAI's one-tape T^{2/5} method | 2 | 4 | 8 | The call to arms; the one-tape case just fell (claimed), and the paper isolates why multitape fails; impact also on RAM simulation ([Wil25] §5 via PF79) | [Wil25] §5; [Wil19] §2.6; [OAI26t] §1 ("not a two-fifths bound for arbitrary multitape machines") | 25 Sep 2026 ([OAI26t], one tape) |
| P3 | **Lean: classical SAT time–space lower bounds in cslib-frontier**: NTIME(n) ⊄ TISP(n^{1.2}, n^{0.2}) and Lipton–Viglas (#2896 M3 open), then the golden-ratio bound, 2cos(π/7), and the transfer to SAT via quasi-linear Cook–Levin (#4225 open) | 4 | 2 | 8 | Engineering on existing TISP/Σ₂ speedup/slowdown modules; the first machine-checked L-vs-NP-direction lower bound; high competition risk | cslib-frontier #2896 (M3 and "beyond" items), #4225 | PRs #2971, #3132 (Nov 2026; speedup TISP(n¹², n²) ⊆ Σ₂TIME(n⁸) merged) |
| P4 | **Push NTIME into less space**: NTIME[t] ⊆ SPACE[t/(log t)^{1/2+δ}] (even this "would be new"), SPACE[t/log t] (HPV's question NTIME[t log t] ⊆ NSPACE[t]), or NTIME[t] ⊆ ATIME[o(t)] | 2 | 3 | 6 | Counting route is tied to #SAT speed (§2.9 item 5) and to the ρ ≥ 1/2 cap, so a new idea is needed; payoff is a cleaner uniform separation | [Cru26] §8 (Nov 2026) | 10–22 Nov 2026 ([Cru26]) |
| P5 | **More unconditional polynomial lower bounds for natural problems in P on multitape TMs**: close the gap N^{3/2} vs cubic for pushdown reachability / CFL reachability, or find other P problems with n^{1+Ω(1)} bounds | 3 | 2 | 6 | The 2026 method (Williams + succinct circuits + careful constants) is fresh and AI-searchable; publishable; small impact on P vs NP | [BM26] §1 (no O(n^{3−ε}) algorithm known; lower bound only N^{3/2}) and §7 | 20 Nov 2026 ([BM26]) |
| P6 | **Time–space tradeoff for Williams' simulation**: TIME[t] ⊆ TIMESPACE[2^{Õ(t^ε)}, Õ(t^{1−ε})]. Lead-scout inference: Williams' stated obstacle (fast evaluation of low-degree extensions of CNFs would refute SETH) loses force if SETH is false; whether the ETH-era tensor contractions evaluate the needed extensions fast is unexamined | 2 | 3 | 6 | A concrete question where the 2026 algorithms might plug in; novelty check required | [Wil25] §5 | Feb 2025 (question); Oct 2026 (¬SETH claimed) |
| P7 | **Improve quasi-linear Cook–Levin** (fewer than O(t log t) variables for time-t NTMs) | 2 | 3 | 6 | Would transfer SAT algorithms and lower bounds to NTIME losslessly; SS's Lemma 2.1 is a partial step | [SS26] §1 ("a long-standing open problem") | 9 Nov 2026 ([SS26] Lemma 2.1) |
| P8 | **Random-access machines in sublinear space**: time t in space t^{1−ε} for log-cost RAMs (or separate linear time on RAMs from multitape TMs) | 2 | 3 | 6 | Williams' method needs locality; Chen–Wang give only relativized evidence of the gap | [Wil25] Remark 1.6 and §5 | 2 Oct 2026 ([SiW26]); Jan 2026 ([ChW26]) |
| P9 | **DTIME(t) ≠ NTIME(t) beyond n√(log* n)** (e.g. t = n log n), or an improvement of PPST's Ω(n(log* n)^{1/4}) | 2 | 3 | 6 | 40-year stall; the new NTIME simulations are upper bounds and do not help directly | [San01] disjunction; [SS26] §1.1 ("very little was known") | 2001 ([San01]) |
| P10 | **n^{1+Ω(1)} time with polylog space for a decision problem in P on general BPs** | 1 | 5 | 5 | Would be a model-independent L ≠ P-type step; techniques stuck at Ω(n polylog) | [YZ23] | 2003 ([BSSV03]); 2013 statement ([BC13]) |
| P11 | OV in n^{2−ε}·poly(d), or CNF-SAT in 2^{(1−δ)n}·poly(m) | 1 | 5 | 5 | Survey 01 O6 | survey 01 §4 O6 | 4 Nov 2026 (Chukhin, constant depth only) |
| P12 | Superlinear time lower bound for SAT with no space restriction (multitape TMs or RAMs) | 1 | 4 | 4 | Beyond indirect diagonalization (U12); would be a first | [FLvMV05] §1; [vM07] Ch. 9 | 2007 (survey) |
| P13 | Weak ETH / SH: 3-SAT in 2^{n^{1−ε}}? | 1 | 4 | 4 | Survey 01 O8; Aaronson would move to 20–30% for P = NP | [MITHG26] (SH "plausible") | 16 Nov 2026 ([MITHG26] v2) |
| P14 | Nontrivial time–space lower bound for **SAT** on two-sided-error randomized machines | 2 | 2 | 4 | Diehl's black-box MA→AM obstacle; only Σ₂SAT known | [vM07] Ch. 9 | 2006 ([DvM06]) |
| P15 | Remove the √log factor: TIME[t] ⊆ SPACE[√t] (TreeEval ∈ L suffices) | 2 | 2 | 4 | TreeEval ∈ L is a major problem; one claimed proof failed (trap 1) | [Wil25] §5, Cor 3.6 | 8 Nov 2026 ([HPR26], catalytic only) |
| P16 | Beat 2cos(π/7) at n^{o(1)} space | 1 | 3 | 3 | Needs a non-alternation-trading ingredient [BW15]; Williams expects "extraordinarily clever" ideas | [Wil19] §2.3; [BW15] | 2012/2015 ([BW15]) |
| P17 | Tautologies on nondeterministic machines: raise ∛4 toward φ | 3 | 1 | 3 | van Melkebeek points to slack in his Lemma 5.1; small impact | [vM07] Ch. 9 | 2007 ([DvMW]); no later result found (search not exhaustive) |

### 4.2 Verification targets (claims the lab can check cheaply; not open problems)

| # | target | T | I | why |
|---|---|---|---|---|
| V1 | **Independent build and statement audit of Cruz's Lean proof** of NTIME[t] ⊆ SPACE[t/√log t] and NTIME[n] ⊊ DSPACE[n] (github.com/SeniorMars/ntime.dspace): `lake build`, `#print axioms`, compare `NtimeChallengeGeneral.lean`/`NtimeChallengeCross.lean` with cslib-frontier's `NTIME`/`DSPACE`; reconcile the T(log log T)²/√log T vs t/√log t versions (N6, N7) | 5 | 3 | Built on the same cslib-frontier definitions the lab plans to adopt; a confirmed NTIME(n) ⊊ DSPACE(n) would enter KNOWN_RESULTS; supersedes survey 01's O4 |
| V2 | Audit OpenAI's Comparator statements for the one-tape T^{2/5} simulation (`OneTapeSpace.lean`) and the WL n^{Ω(k)} lower bound | 4 | 2 | AI-produced, Lean-checked by the authors only |
| V3 | Red-team the N^{3/2} pushdown-reachability proof ([BM26]); it is unformalized and AI-found | 3 | 2 | Unrefereed, posted 20 Nov 2026 |

---

## 5. Live competition (who is visibly working on each open problem now)

| problem | visible activity (evidence) |
|---|---|
| P1 barrier for locality-based simulations | None found. Related: Li–Tell (TR26-233, Oct 2026); Cruz's relativization remark (Nov 2026) |
| P2 QBF superlinear / multitape t^{1/2−ε} | OpenAI (one-tape T^{2/5}, Sep 2026); Sibgatullin–Williams (TR26-223, Oct 2026); Williams' MFCS 2026 talk announces further generalizations |
| P3 Lean time–space lower bounds | cslib-frontier #2896 (S. Schlesinger; agent "worker w30-tisp"; fork commits by "orbitingflea", 8 Nov 2026); #4225 quasi-linear Cook–Levin open |
| P4 NTIME in less space | C. Cruz (paper revised 22 Nov 2026); R. Yang with T. Pitassi; S. McGuire (both via [Cru26]); cslib-frontier #2226 (S. Schlesinger, draft PR #2231) |
| P5 lower bounds for problems in P | A. R. Balasubramanian, R. Majumdar (with GPT-6.1-Sol, Nov 2026); M. Wehar (DFA intersection, 2025–26); OpenAI (WL, Sep 2026) |
| P6 time–space tradeoff of Williams' simulation | None found |
| P7 quasi-linear Cook–Levin | C. Strassle, B. Subercaseaux (Nov 2026); cslib-frontier #4225 |
| P8 RAM simulation | D. Sibgatullin, R. Williams; L. Chen, Y. Wang (relativized) |
| P9 DTIME vs NTIME | None found |
| P10 BP n^{1+Ω(1)} | None found since [YZ23] (2023) |
| P11 OV / CNF-SAT | N. Chukhin (constant depth, Nov 2026); T. Choudhury, N. Limaye, K. Sreenivasaiah, S. Srinivasan (ECCC TR26-121, OV formula lower bounds); H. Lin (ECCC TR26-139, AC⁰ k-OV); no algorithmic attack found |
| P12 SAT without space bound | None found |
| P13 Weak ETH / SH | MIT Hardness Group (framework, v2 16 Nov 2026); P. Manurangsi ("Almost-ETH"); users: Karthik C. S., D. Minzer (arXiv:2611.14892); S. Bartlmae (survey 01 C16) |
| P14 randomized SAT bounds | None found |
| P15 TreeEval ∈ L / √t | A. Henzinger, E. Pyne, S. Ragavan (catalytic, v3 8 Nov 2026); V. R. Asadi, R. Cleve ("intend to revise" after withdrawal); cslib-frontier #2855 (Cook–Mertz refinements, no owner as of 13 Nov 2026) |
| P16, P17 | None found |
| V1–V3 | cslib-frontier #2226 (formalizing Cruz natively); nobody else visibly auditing [BM26] or OpenAI's one-tape/WL artifacts |

---

## 6. Known traps

1. **Nye's "TIME[t] ⊆ SPACE[O(√t)]" is wrong by the author's own statement.** arXiv:2508.14831 v4 (1 Jan 2026):
   "The proof of the main theorem is incorrect", because its height-compression framework "does not correctly model
   the Tree Evaluation instances/dependencies arising in Williams's simulation". The companion "holographic" paper
   (arXiv:2512.00607) builds on the same construction. Do not cite either as progress.
2. **Asadi–Cleve's polynomial-time O(log^{1+ε} n)-space TreeEval is withdrawn** (arXiv:2604.02606 v2, 7 Apr 2026:
   "an error in the calculation of the polynomial degree for each subtree"); the ECCC version TR26-044 is still listed.
3. **Santhi–Vardy's "quadratic time–space tradeoff for unrestricted deterministic decision branching programs" is
   withdrawn** (arXiv:cs/0608085 v2, 2010). Quadratic BP bounds for decision problems remain open (B7).
4. **Trying to beat n^{1.8019} with more speedup/slowdown steps.** Rules R0–R2 provably stop at 2cos(π/7), and the
   computer search is exhaustive for each (c, ε) in Fig. 8.2 [BW15]. A new non-relativizing ingredient is required
   [vM07 Ch. 9].
5. **Expecting indirect diagonalization to give time bounds without space bounds.** It relativizes, and relative to
   a TQBF oracle all these models are quasi-linear-time equivalent [vM07 Ch. 9]; also U12.
6. **Pebbling-based improvements of HPV.** Pebbling lower bounds block anything below t/log t; Williams' improvement
   needed the non-pebbling Cook–Mertz procedure [Wil25 §5].
7. **Naive recursion of Williams' simulation** (to get t^ε space): the Cook–Mertz step needs low-degree extensions of
   block computations, not just simulations [Wil25 §5].
8. **Mixing models.** Williams' theorem is for multitape (and d-dimensional) TMs, not RAMs (Remark 1.6). SAT
   time–space bounds are for random-access machines with small space. PPST/Santhanam and Cruz are multitape. OpenAI's
   T^{2/5} is for one writable tape only. WL and multiplication claims each fix their own model. State the model with
   every bound.
9. **Misreading the QBF call to arms.** Since 2025 there are n^{2−ε} multitape lower bounds for linear-space
   PSPACE-complete problems (L1, L2), but not for QBF itself: SPACE[n] reduces to QBF only with quadratic blow-up
   (lead-scout inference, L11), and Williams still lists QBF as open [Wil25 §5].
10. **"Lean-checked" ≠ reviewed ≠ correct statement.** Cruz's, OpenAI's and Anthropic's Lean checks are the authors'
    own; Cruz's Theorem 7.1 uses locally defined ⊕TIME/Mod_qTIME/C₌TIME (CSLib Frontier lacks them, lean/README); the
    cslib issue and the paper state different bounds (N6, N7). Never upgrade these to lab status `lean-verified`
    without V1-style audits.
11. **Relativizing arguments cannot separate P from Σ₂^p or PSPACE**: relative to a PSPACE-complete oracle,
    P = PSPACE [BGS75]. Unrefereed diagonalization/union-theorem claims of P ≠ Σ₂^p (e.g. arXiv:1602.04781) fall under
    this unless they say exactly which step does not relativize. I found no evidence that this claim is accepted.
12. **Conjectured lower bounds keep falling.** Schönhage–Strassen n log n optimality on multitape TMs (L13, claimed),
    the Ω(N log N) intuition for multitape sorting (L12, claimed), Subset Sum 2^{n/2} (F6), 3SUM/APSP (F4), ETH itself.
    Williams' essay already warned that lower-bound conjectures fail more often than upper-bound ones (00-director-sources).
    Treat any "natural" lower-bound conjecture as a hypothesis.
13. **Lipton's conjecture is false relative to random oracles** [SS26 §1.1]: "true relative to a random oracle" is not
    evidence for uniform statements in this area.
14. **Unrefereed new hypotheses** (e.g. SRK-ESH, F12) proliferate after ETH's fall; check whether a hypothesis
    is standard before building on it. Survey 01 trap 5 covers the "Weak ETH" naming confusion.

---

## 7. People and groups (names seen on the recent papers cited here)

- **Time vs space, tree evaluation, catalytic:** R. Williams (MIT) [Wil25, SiW26, MSW26, Wil26m]; D. Sibgatullin
  [SiW26]; J. Cook, I. Mertz [CM24]; A. Henzinger, E. Pyne, S. Ragavan [HPR26]; Y. Shalunov [Sha25]; A. Morrison
  Orozco, N. Sheffield [MSW26]; V. R. Asadi, R. Cleve [AC26, withdrawn]; S. Bhardwaj (TR26-252); W. Hoza (TR26-323).
- **Conditional simulations:** Z. Li, R. Tell [LiT26]. RAM vs TM: L. Chen, Y. Wang [ChW26].
- **Lower bounds for explicit problems:** A. R. Balasubramanian, R. Majumdar (MPI-SWS) [BM26]; M. Wehar [Weh25];
  Y. Tal [Tal26]; OpenAI (one-tape, WL, multiplication, Subset Sum, L = BPL catalogue entries).
- **NTIME vs DTIME/SPACE:** C. Strassle (Stanford), B. Subercaseaux (CMU) [SS26]; C. Cruz (Rice) [Cru26]; R. Yang,
  T. Pitassi, S. McGuire (reported in [Cru26]); N. Chukhin (blog comment).
- **Fine-grained:** J. Alman, V. Vassilevska Williams; S. R. Karingula, S. Lovett; T. Chan, R. Itakura, Z. Ma, Y. Yu;
  B. Li, L. Ye; B. Cui, S. C. Liu, Y. Yu; T. Jiang, S. Cai; Z. Chen, H. Yao; G. Zhou; MIT Hardness Group.
- **Formalization:** S. Schlesinger (cslib-frontier counting simulation, Williams follow-ups, Cruz issue);
  C. Reitwiessner (Williams module, TISP); account "chris-ai1" and other agent accounts on #888; "orbitingflea".
- **Classical anchors (for context, not 2024–26):** S. Buss, D. van Melkebeek, L. Fortnow, P. Beame, R. Santhanam.
- **Commentary:** S. Aaronson [Aar26]; L. Fortnow [For26r].

---

## 8. Formalization status (Lean / Coq / Isabelle)

**cslib-frontier** (local clone, commit 1435284b, 23 Nov 2026; Lean v4.36.0-rc2; I read sources, did not build):
- `Classes/TimeSpace/Williams.lean`: `Cslib.Complexity.DTIME_subset_DSPACE_sqrt` — for every injective encoding and
  t(n) ≥ n, DTIME(t) ⊆ DSPACE(Nat.sqrt(t·(Nat.log2 t + 1))), no constructibility (Williams Thm 1.1, v1). Registered as
  `williams-square-root-space` in `CslibFrontierResults/Entries.lean`. Issue #888 closed 6 Nov 2026.
- `Classes/TimeSpace/WilliamsSeparation.lean`: `DTIME_rpow_sub_ssubset_DSPACE_id` (DTIME(n^{2−ε}) ⊊ DSPACE(n)),
  `DSPACE_id_not_subset_DTIME_rpow_sub`, `DTIME_sq_div_log2_sq_ssubset_DSPACE_id`, `DTIME_pow_ssubset_DSPACE_pow`
  (a < 2b), general `…_of_sqrt`/`…_of_isLittleO` forms. Issue #2855 (open, last activity 14 Nov) keeps Cook–Mertz
  malformed-input handling and the refined O(ℓ + H log(ℓ + 2)) bound open; current bound O((ℓ + H + 1)·log(ℓ + 2)).
- `Computability/TreeEval/CookMertz.lean`, `TreeEval/Ary/CookMertz.lean`: Cook–Mertz Tree Evaluation.
- `Classes/TimeSpace/Basic.lean` (TISP), `Speedup.lean` (`TISP_subset_SigmaTwoTIME`,
  `TISP_pow_twelve_subset_SigmaTwoTIME`: TISP(n¹², n²) ⊆ Σ₂TIME(n⁸)), `Slowdown.lean` (`SigmaTwoTIME_subset_NTIME`).
  The headline NTIME(n) ⊄ TISP(n^{1.2}, n^{0.2}) is **not** done (issue #2896 M3 open, last activity 8 Nov 2026);
  golden-ratio, 2cos(π/7) and the SAT transfer are listed as remaining work.
- `Classes/CountingSimulation/*` (S. Schlesinger): NTIME/BPTIME/PPTIME/#TIME in 2^{O(T/√log T)} time and poly space
  (`NTIME_subset_iUnion_DTIME_two_pow_div_sqrt_log_two`), strict separations from DTIME[2^T]
  (`NTIME_mul_sqrt_sqrt_log_two_ssubset_DTIME_two_pow`). Uses `fastContractionAlgorithm` (OpenAI Thm D.1), a
  `noncomputable def` with proofs; no `sorry` in these directories by grep.
- One-tape lower bounds: `SingleTape/Palindrome.lean` (`palindrome_lower_bound`), `SingleTape/NLogNGap.lean`
  (`isRegular_of_isLittleO`).
- Also present: hierarchy theorems (#3553 closed: P ⊊ EXP, L ⊊ PSPACE), TQBF PSPACE-completeness
  (`Classes/Space/TQBF.lean`, `TQBF_pspaceComplete`), Savitch, Immerman–Szelepcsényi, Chandra–Kozen–Stockmeyer parts,
  fine-grained items (Schöning, PPZ, Williams' OV→SAT split-and-list transfer `decidableInExpTime_SAT`, native
  sparsification consequence, ¬ETH/¬SETH in `FineGrained/CountingNativeEndpoint.lean`).
- Open roadmap items in this area: #2226 (Cruz), #4225 (quasi-linear Cook–Levin), #800 (O(t log t) universal machine),
  #4728 (alternating counting simulation in ATIME O(n + t/√log t)), #4086 (alternating classes), #3037 (OV
  reductions), #3076 (APSP class), #4667 (CIMY 3SUM), #894 (exponential-time SAT), #2521 (catalytic space).

**External Lean artifacts (authors' checks only; I built none):**
- Cruz, github.com/SeniorMars/ntime.dspace: Thm 1.1, Cor 1.2, Thm 7.1, Cor 7.2, Props 8.1–8.2, Remark 8.3, on CSLib
  Frontier definitions, standard axioms, Comparator (main names `NtimeDspace.Crossing.ntime_decidable_sqrtLog_general`,
  `NtimeDspace.Crossing.ntime_ssubset_dspace`).
- OpenAI math release: Comparator statements for one-tape T^{2/5} (`ComparatorChallenges/OneTapeSpace.lean`), WL
  lower bounds (`ParityLifts.lean`, `WLIdentification.lean`, …), L = RL = BPL (`LogspaceEquality.lean`). No Lean scope
  doc found for integer multiplication (109) or Subset Sum (138) (HTTP 404).
- Anthropic `formal-math/3sum-apsp/` (Lean v4.33.1): 3SUM O(n^{1.9992}), APSP O(n^{2.99942}) on word RAMs.

**Coq / Isabelle:** none found for time–space lower bounds, Williams' simulation or NTIME/DTIME separations (searched
only through web search and the cslib-frontier roadmap; not exhaustive).

---

## 9. Known-results registry entries (for research/KNOWN_RESULTS.md)

Format: `- [area] statement — Authors (Year), venue/arXiv — checked:yes/no`. Entries already in KNOWN_RESULTS are not
repeated unless a verified detail is added.

- [time-space-SAT] ∀ε>0 SAT ∉ DTISP(n^{1+o(1)}, n^{1−ε}) on (co-non)deterministic RAMs (stronger: not both a time-n^{1+o(1)} and a poly-time space-n^{1−ε} algorithm) — Fortnow (2000), JCSS 60 — checked:yes (via van Melkebeek survey Thm 1.1)
- [time-space-SAT] SAT ∉ DTS(n^{√2−o(1)}) — Lipton, Viglas (1999), FOCS — checked:yes (via survey)
- [time-space-SAT] ∀c<φ∃d>0: no deterministic RAM solves SAT in time n^c, space n^d (d→1 as c→1); co-nondeterministic: c<√2; applies to NTIME(n) — Fortnow, Lipton, van Melkebeek, Viglas (2005), J. ACM 52 — checked:yes
- [time-space-SAT] SAT, MOD₆-SAT, MOD_m-SAT (m composite, not a prime power) and MOD_p-SAT for all but ≤1 prime ∉ RAM time n^c, space n^{o(1)} whenever c³−c²−2c+1<0, i.e. c<2cos(π/7)≈1.8019 (current record) — Williams (2007/2008), CCC 2007 / Comput. Complex. 17(2) / ECCC TR07-036 — checked:yes
- [time-space-SAT] Master theorem: (c−1)d<1 or cd(d−1)−2d+1<0 ⇒ SAT not solvable by both a co-nondeterministic RAM in time n^c and a deterministic RAM in time n^d, space n^e (some e>0) — van Melkebeek (2007), FnT TCS 2(3) Thm 1.3 — checked:yes
- [barrier] Alternation-trading proofs (rules R0–R2) yield SAT ∉ DTS(n^c) only for c<2cos(π/7); max provable c at space n^ε: 1.80083 (ε=0.001), 1.69618 (0.1), 1.55242 (0.25), 1.34070 (0.5), 1.15765 (0.75), 1.06011 (0.9), 1.00583 (0.99) — Buss, Williams (2012/2015), CCC 2012 / Comput. Complex. 24(3) / ECCC TR11-031 — checked:yes
- [barrier] Indirect-diagonalization time–space arguments relativize; relative to a TQBF oracle the models are quasi-linear-time equivalent, so they give nothing without a space bound — van Melkebeek (2007), FnT TCS Ch. 9 — checked:yes
- [time-space-SAT] No superlinear time lower bound for SAT on unrestricted RAMs (stated 2004; none found through Nov 2026) — Fortnow, Lipton, van Melkebeek, Viglas (2005) §1 — checked:yes
- [time-space-SAT] TAUT on nondeterministic RAMs needs time n^{∛4−o(1)} at space n^{o(1)}; nondeterministic master theorem (c²−1)d<c or c²d<4 — Diehl, van Melkebeek, Williams (2007), UW TR 1601, via van Melkebeek (2007) Thm 1.4–1.5 — checked:yes (via survey)
- [time-space-SAT] Σ₂SAT ∉ two-sided-error randomized RAM time n^d, space n^e for every d<2; Σ_kSAT for d<k (k≥3); no nontrivial two-sided-error bound for SAT — Diehl, van Melkebeek (2006), SICOMP 36 — checked:yes (via survey)
- [time-space-SAT] MajMajSAT: ∀ε>0∃d>1 no two-sided-error quantum algorithm in time n^d, space n^{1−ε} — van Melkebeek, Watson (2007) — checked:yes (via survey)
- [time-space-route] Proving "SAT ∈ TIMESPACE[n^{O(1)}, log n] ⇒ SAT ∈ TIMESPACE[n^{1.1}, n^{0.7}]" would give NP ≠ L — Lipton, Williams (2013), Comput. Complex. 22(2) §1 — checked:yes
- [branching-programs] ∀k, small ε: no Boolean BP of size <2^{εn} computes in time kn the parity of #{x<y∈X : x+y∈X} (function in P) — Ajtai (2005), Theory of Computing 1(8) — checked:yes
- [branching-programs] Randomized Boolean BPs for Ajtai's functions: T=Ω(n√(log(n/S)/log log(n/S))); S=O(n^{1−ε}) ⇒ T=Ω(n√(log n/log log n)) — Beame, Saks, Sun, Vee (2000/2003), FOCS 2000 / J. ACM 50(2) — checked:yes
- [branching-programs] Largest known multi-way BP lower bound for any single-output problem in P: T∈Ω(n log((n log n)/S)) (2013); ED has a randomized BP with T∈Õ(n^{3/2}/S^{1/2}) — Beame, Clifford (2013), arXiv:1309.3690 — checked:yes
- [branching-programs] n^{1+Ω(1)} time lower bound for a decision problem with polylog space is open; T²S=Ω(n^{2.5}/log n) for deterministic oblivious BPs on a multi-output function — Yu, Zhan (2023), arXiv:2306.15817 — checked:yes (abstract)
- [branching-programs][withdrawn] Claimed quadratic TS tradeoff for unrestricted deterministic decision BPs — Santhi, Vardy (2006), arXiv:cs/0608085 (withdrawn) — checked:yes (abstract page)
- [catalytic] With O(log n) free and poly(n) catalytic space: sorting, DFT in n^{1+o(1)} time, matrix multiplication in n^{ω+o(1)}, beating the non-catalytic Ω(n²)/Ω(n³) TS products — Morrison Orozco, Sheffield, Williams (2026), arXiv:2610.24377 — checked:yes (abstract)
- [time-vs-space] TIME[t] ⊆ SPACE[O(t/log t)] (multitape) — Hopcroft, Paul, Valiant (1977), J. ACM 24(2) — checked:yes (via Williams 2025)
- [time-vs-space] TIME[t] ⊆ ATIME[t/log t] is the best alternation speedup; TIME[t] ⊆ ATIME[t^{1−ε}] would give a superlinear QBF lower bound — Dymond, Tompa (1985), JCSS 30(2), via Williams (2025) §5 — checked:yes (via Williams)
- [time-vs-space] Tree Evaluation in space O(log n·log log n) and time n^{O(log log n)} — Cook, Mertz (2024), STOC 2024 / ECCC TR23-174 — checked:yes
- [time-vs-space] ∀t(n)≥n: TIME[t] ⊆ SPACE[√(t log t)]; SPACE[s] ⊄ TIME[s^{2−ε}] (s space-constructible ≥ n); bounded-space halting needs n^{2−ε} multitape time; size-s circuits have BPs of size 2^{k√s log^k s}; d-dim TMs in SPACE[(t log t)^{1−1/(d+1)}]; TreeEval ∈ L ⇒ TIME[t] ⊆ SPACE[√t]; length-restricted relativization holds; not known for random-access models — Williams (2025), arXiv:2502.17779 / STOC 2025 — checked:yes
- [time-vs-space] Circuit value for size-s circuits in O(√(s log s)) space — Shalunov (2025), arXiv:2504.20950 / ECCC TR25-078 — checked:yes (abstract)
- [time-vs-space] Lex-First 2SAT in Õ(√n) space; unbounded fan-in {NOT,AND,OR,XOR} circuits with n gates in O(√(n log n)) space; d-dim cellular automata in O((t log t)^{1−1/(d+1)}) space — Sibgatullin, Williams (2026), ECCC TR26-223 — checked:yes (abstract)
- [time-vs-space] Catalytic TreeEval: O(log n) free space, poly time, 2^{O(log^ε n)} catalytic space ∀ε>0 — Henzinger, Pyne, Ragavan (2026), arXiv:2602.14320 / ECCC TR26-022 — checked:yes (abstract)
- [time-vs-space][conditional] Under average-case hardness of (low-space) Range Avoidance: t-time algorithms in space t^ε on average, and in linear time with enough alternations on average; an assumption is necessary (conclusion ⇒ P ≠ PSPACE) — Li, Tell (2026), ECCC TR26-233 — checked:yes (abstract)
- [time-vs-space][claimed][AI] One writable tape: time T in O(T^{2/5} polylog T) space (answers Williams' one-tape question; not multitape) — OpenAI (2026), OpenAI Math Release family 137, 25 Sep 2026 — checked:yes (paper §1; Lean not built)
- [time-vs-space] Relative to a random oracle with O(log n)-bit answers, an O(n)-time RAM function needs n²/polylog n multitape time — Chen, Wang (2026), ECCC TR26-006 — checked:yes (abstract)
- [time-vs-space][retracted] TIME[t] ⊆ SPACE[O(√t)] claim retracted by its author ("The proof of the main theorem is incorrect") — Nye (2025), arXiv:2508.14831 v4 — checked:yes
- [time-vs-space][withdrawn] Poly-time O(log^{1+ε} n)-space (O(log n) free) TreeEval withdrawn (polynomial-degree error) — Asadi, Cleve (2026), arXiv:2604.02606 v2 / ECCC TR26-044 — checked:yes
- [explicit-lower-bounds] DFA intersection non-emptiness requires Ω(n²/(log³ n (log log n)²)) time (via Williams 2025) — Wehar (2025/26), arXiv:2512.00297 — checked:yes (abstract)
- [explicit-lower-bounds][claimed][AI] Pushdown reachability ∉ multitape DTIME(N^{3/2−ε}) even for sparse instances; one PDA ∩ (k−1) NFAs ∉ DTIME(N^{3k/2−ε}) — Balasubramanian, Majumdar (2026), arXiv:2611.27814 — checked:yes
- [explicit-lower-bounds][claimed][AI] For large fixed k, k-WL equivalence needs n^{Ω(k)} deterministic time (multitape TMs, log-word RAMs); EXPTIME-complete with k in binary — OpenAI (2026), Math Release family 133 — checked:yes (catalogue + Lean scope doc)
- [explicit-lower-bounds] Succinct QBF requires non-linear time on multitape TMs, RAM-TMs, tree computers, log-cost RAMs — Williams (2008), ECCC TR08-076 — checked:yes (abstract)
- [explicit-lower-bounds] QBF has no n^c-time uniform NC circuits for c<2; either QBF ∉ TIME[n^c] or CircEval ∉ SIZE-DEPTH[n^d, n^e] when c<(1−e+d)/d — Lipton, Williams (2013), Comput. Complex. 22(2) — checked:yes
- [explicit-lower-bounds] A superlinear time lower bound for (ordinary) QBF is open — Williams (2025), arXiv:2502.17779 §5 — checked:yes
- [multitape-algorithms][claimed] Multitape sorting of N bits in O(N log n/(log log log n)^η) — Y. Tal (2026), ECCC TR26-331 — checked:yes (abstract)
- [multitape-algorithms][claimed][AI] n-bit integer multiplication in O(n(log n)^{1−κ}), κ=2^{−182}, on a multitape TM — OpenAI (2026), Math Release family 109 — checked:yes (catalogue)
- [NTIME-DTIME] DTIME(n) ≠ NTIME(n) (multitape); DTIME(f) ⊆ Σ₄TIME(f/log* f) for time-constructible f ≥ n log* n — Paul, Pippenger, Szemerédi, Trotter (1983), FOCS — checked:yes
- [NTIME-DTIME] DTIME(n√(log* n)) ≠ NTIME(n√(log* n)); P ≠ L or (∀ constructible t: DTIME(t) ≠ NTIME(t)) — Santhanam (2001), CCC / ECCC TR01-022 — checked:yes (abstract)
- [NTIME-DTIME] Lipton's conjecture (∀ε: NTIME[t] ⊆ DTIME[2^{εt}]) false relative to some oracles and relative to a random oracle; open until [SS26]; KLRS improved the constant c in 2^{ct} — Strassle, Subercaseaux (2026) §1.1 citing Lipton (2009), Kalyanasundaram–Lipton–Regan–Shokrieh (2012), Moran (1981), Doty (2010) — checked:yes (via SS26)
- [NTIME-DTIME] Transfer: circuit-CSP (arity k(n), density ≤2) in 2^{O(n/s(n))} ⇒ NTIME[t] ⊆ DTIME[2^{O(t/k(t))+O(t/s(t))}]; 3-SAT in 2^{O(n/s(n))} ⇒ NTIME[t] ⊆ DTIME[2^{O(t log s(t)/s(t))}]; generalized Cook–Levin to 2^{O(t/b)} CSPs with O(t) variables — Strassle, Subercaseaux (2026), arXiv:2611.11832 Thm 2, 3, Lemma 2.1 — checked:yes
- [NTIME-SPACE][claimed] NTIME[t] ⊆ SPACE[O(t/√log t)] ∀t≥n; hence NTIME[n] ⊊ DSPACE[n], NTIME[t] ⊊ NSPACE[t], NTIME[t√log t] ⊆ SPACE[t], PPTIME[n] ⊊ SPACE[n], and a SPACE[n] language needing c·n√log n nondeterministic time; non-relativizing; author's Lean proof on CSLib Frontier definitions — Cruz (2026), github.com/SeniorMars/ntime.dspace (paper 10 Nov, PDF 22 Nov 2026) — checked:yes (paper; Lean not built)
- [NTIME-SPACE][claimed] Earlier form NTIME(T) ⊆ DSPACE(T(log log T)²/√log T) — Cruz as recorded in cslib-frontier issue #2226 (1 Nov 2026); Yang with Pitassi per Cruz §1.2 — checked:yes (issue) / no (Yang)
- [NTIME-SPACE][method-limit] Counting-based evaluators in space D(s) give #3-SAT in time 2^{O(D(O(m)))}; Boolean (OR/AND) pieces cannot cancel (r_i+c_i ≥ 4λ−2 log N); integer pieces need min(r_i,c_i) ≥ a−log N — Cruz (2026), Props 8.1–8.2, §8 (Lean-proved per author) — checked:yes (paper)
- [formalization] DTIME(t) ⊆ DSPACE(√(t(log₂t+1))) and DSPACE(n)-vs-DTIME(n^{2−ε}) separations; TISP(n¹²,n²) ⊆ Σ₂TIME(n⁸); NTIME/BPTIME/PPTIME ⊆ DTIME[2^{O(T/√log T)}] with poly space; NTIME[T(log T)^{1/4}] ⊊ DTIME[2^T]; NTIME(n) ⊄ TISP(n^{1.2},n^{0.2}) NOT yet done — cslib-frontier (2026), commit 1435284b (Williams.lean, WilliamsSeparation.lean, Speedup.lean, CountingSimulation/*; issues #888, #2896, #1833, #2050) — checked:yes (source read; not built)
- [fine-grained] APSP exponent discrepancy: O(n^{2.9995}) in the arXiv abstract vs O(n^{2.99942}) in the Anthropic Lean README — Alman, Vassilevska Williams (2026), arXiv:2610.06783; anthropics/formal-math 3sum-apsp — checked:yes
- [fine-grained] Simplified truly subquadratic 3SUM / subcubic APSP via selected-entry matrix multiplication (weaker exponents) — Karingula, Lovett (2026), ECCC TR26-247 / arXiv:2610.15663 — checked:yes (abstract)
- [fine-grained][claimed] Subset Sum in randomized O(2^{0.49999977n}) — Li, Ye (2026), arXiv:2610.10446; and [AI] in O(2^{0.49n}) word-RAM time, plus poly(n)2^{n/2} time with O(2^{n/5}) space — OpenAI (2026), Math Release family 138 — checked:yes (abstracts)
- [SAT-algorithms] Deterministic 3-SAT in 1.32736^n — Cui, Liu, Yu (2026), arXiv:2611.16814 — checked:yes (abstract)
- [SAT-algorithms] PPSZ: Unique-3-SAT O*(1.306969598^n), 3-SAT O*(1.307031578^n) — Jiang, Cai (2026), arXiv:2607.10697 v2 — checked:yes (abstract)
- [QBF-algorithms] QBF in 1.685^m·poly(n) (previous 1.709^m) — Chen, Yao (2026), arXiv:2611.10633 — checked:yes (abstract)
- [QBF-algorithms] 2-block quantified 3-CNF in 2^{n−Ω(√n)} poly(m) deterministic; q-block poly-size CNF QBF in 2^{n−n^{1/(q+1)}} poly(n); 2^{n−n^{ω_q(1/q)}} for q-block CNF QBF ⇒ NEXP ⊄ poly-size O(log n)-depth circuits — Santhanam, Williams (2015), SODA / ECCC TR13-108 — checked:yes (abstract)
- [space-context][claimed][AI] L = RL = BPL (Lean via Comparator) — OpenAI (2026), Math Release family 103 — checked:yes (catalogue + Lean scope doc)
- [space-context][claimed] NL = UL — Hoza (2026), ECCC TR26-323 — checked:yes (abstract)
- [context] Aaronson moved P=NP from 3% to 5% after the ETH news; 20–30% if subexponential CircuitSAT or Weak ETH fell — Aaronson (2026), Shtetl-Optimized ?p=10239 comments #4, #18, #31 — checked:yes
- [context] Fortnow (Jun 2026): does not expect a P vs NP proof in his lifetime "by man or machine"; advises against a Lean approach — Fortnow (2026), Computational Complexity blog — checked:yes
- [context] Williams (2019): L ≠ NP 95%, P ≠ PSPACE 90%; no n^{1.0001} time lower bound for QBF — Williams (2019), LNCS essay Table 1, §2.6 — checked:yes

---

## 10. Bibliography (for research/BIB.md)

Format follows BIB.md. Keys already in BIB.md are reused: `BGS75`, `AW09`, `AB09`, `SS26`, `Wil19`, `Aar26`,
`MITHG26`, `OAI26`, `Ant26`.

Time–space lower bounds for SAT:
- `For00` — L. Fortnow. "Time-space tradeoffs for satisfiability." J. Comput. Syst. Sci. 60:337–353, 2000 (CCC 1997). — checked: no (cited via vM07)
- `LV99` — R. Lipton, A. Viglas. "On the complexity of SAT." FOCS 1999, 459–464. — checked: no (via vM07)
- `FLvMV05` — L. Fortnow, R. Lipton, D. van Melkebeek, A. Viglas. "Time-space lower bounds for satisfiability." J. ACM 52:835–865, 2005. https://lance.fortnow.com/papers/files/tst.pdf — checked: yes
- `Wil05` — R. Williams. "Better time-space lower bounds for SAT and related problems." CCC 2005, 40–49. — checked: no
- `Wil07` — R. Williams. "Time-space tradeoffs for counting NP solutions modulo integers." CCC 2007, 70–82; Comput. Complex. 17(2):179–219, 2008. https://eccc.weizmann.ac.il/report/2007/036/ — checked: yes (abstract)
- `Wil10` — R. Williams. "Alternation-Trading Proofs, Linear Programming, and Lower Bounds." STACS 2010. arXiv:1001.0746 — checked: yes (abstract)
- `BW15` — S. Buss, R. Williams. "Limits on Alternation-Trading Proofs for Time-Space Lower Bounds." CCC 2012; Comput. Complex. 24(3):533–600, 2015. doi:10.1007/s00037-015-0104-9; ECCC TR11-031; https://mathweb.ucsd.edu/~sbuss/ResearchWeb/npProofLimits/paper-journal.pdf — checked: yes
- `vM07` — D. van Melkebeek. "A Survey of Lower Bounds for Satisfiability and Related Problems." Found. Trends Theor. Comput. Sci. 2(3):197–303, 2006/2007. doi:10.1561/0400000012; https://pages.cs.wisc.edu/~dieter/Papers/sat-lb-survey-fttcs.pdf; ECCC TR07-099 — checked: yes
- `DvM06` — S. Diehl, D. van Melkebeek. "Time-space lower bounds for the polynomial-time hierarchy on randomized machines." SIAM J. Comput. 36:563–594, 2006. — checked: no (via vM07)
- `DvMW` — S. Diehl, D. van Melkebeek, R. Williams. "A new time-space lower bound for nondeterministic algorithms solving tautologies." UW-Madison TR 1601, 2007. — checked: no (via vM07)
- `vMW07` — D. van Melkebeek, T. Watson. "A quantum time-space lower bound for the counting hierarchy." UW-Madison TR 1600, 2007; arXiv:0712.2545. — checked: no (via vM07)
- `Kan84` — R. Kannan. "Towards separating nondeterminism from determinism." Math. Systems Theory 17:29–45, 1984. — checked: no (via vM07, PPST83)
- `LW13` — R. Lipton, R. Williams. "Amplifying circuit lower bounds against polynomial time, with applications." Comput. Complex. 22(2):311–343, 2013 (CCC 2012). https://people.csail.mit.edu/rrw/qbf-nc-journal-rev.pdf — checked: yes

Branching programs and catalytic:
- `Ajt05` — M. Ajtai. "A Non-linear Time Lower Bound for Boolean Branching Programs." Theory of Computing 1(8):149–176, 2005 (FOCS 1999). https://theoryofcomputing.org/articles/v001a008/ — checked: yes
- `BSSV03` — P. Beame, M. Saks, X. Sun, E. Vee. "Time-space trade-off lower bounds for randomized computation of decision problems." J. ACM 50(2):154–195, 2003; FOCS 2000, 169–179; ECCC TR00-025. https://homes.cs.washington.edu/~beame/papers/superlinear.pdf — checked: yes (FOCS version)
- `BJS01` — P. Beame, T. S. Jayram, M. Saks. "Time-space tradeoffs for branching programs." J. Comput. Syst. Sci. 63(4):542–572, 2001. — checked: no
- `BV02` — P. Beame, E. Vee. "Time-space tradeoffs, multiparty communication complexity, and nearest-neighbor problems." STOC 2002, 688–697. — checked: no
- `BC13` — P. Beame, R. Clifford. "Element Distinctness, Frequency Moments, and Sliding Windows." arXiv:1309.3690, 2013. — checked: yes
- `YZ23` — H. Yu, W. Zhan. "Randomized vs. Deterministic Separation in Time-Space Tradeoffs of Multi-Output Functions." arXiv:2306.15817, 2023. — checked: yes (abstract)
- `SV06` — N. Santhi, A. Vardy. "A Quadratic Time-Space Tradeoff for Unrestricted Deterministic Decision Branching Programs." arXiv:cs/0608085 (withdrawn). — checked: yes (abstract page)
- `MSW26` — A. Morrison Orozco, N. Sheffield, R. Williams. "Computing faster with a full memory: Catalytic algorithms break time-space lower bounds." arXiv:2610.24377, 17 Oct 2026. — checked: yes (abstract)

Time versus space:
- `HPV77` — J. Hopcroft, W. Paul, L. Valiant. "On time versus space." J. ACM 24(2):332–337, 1977 (FOCS 1975). doi:10.1145/322003.322015 — checked: no (via Wil25)
- `PR81` — W. Paul, R. Reischuk. "On time versus space II." J. Comput. Syst. Sci. 22(3):312–327, 1981. — checked: no (via Wil25)
- `HLMW86` — J. Halpern, M. Loui, A. Meyer, D. Weise. "On time versus space III." Math. Syst. Theory 19(1):13–28, 1986. — checked: no (via Wil25)
- `DT85` — P. Dymond, M. Tompa. "Speedups of deterministic machines by synchronous parallel machines." J. Comput. Syst. Sci. 30(2):149–161, 1985. — checked: no (via Wil25)
- `HU68` — J. Hopcroft, J. Ullman. "Relations between time and tape complexities." J. ACM 15(3):414–427, 1968. — checked: no (via Wil25, SS26)
- `CM24` — J. Cook, I. Mertz. "Tree Evaluation is in Space O(log n · log log n)." STOC 2024, 1268–1278. doi:10.1145/3618260.3649664; ECCC TR23-174 — checked: yes (abstract)
- `Wil25` — R. Williams. "Simulating Time With Square-Root Space." arXiv:2502.17779v1 (25 Feb 2025); STOC 2025, doi:10.1145/3717823.3718225; ECCC TR25-017; J. ACM 2026, doi:10.1145/3798104 (journal not opened). — checked: yes (arXiv v1)
- `Wil26m` — R. Williams. "Some Recent Developments in Space Complexity (Invited Talk)." MFCS 2026, LIPIcs 386, doi:10.4230/LIPIcs.MFCS.2026.3 — checked: yes (abstract)
- `Sha25` — Y. Shalunov. "Improved Bounds on the Space Complexity of Circuit Evaluation." arXiv:2504.20950; ECCC TR25-078. — checked: yes (abstract)
- `SiW26` — D. Sibgatullin, R. Williams. "Space-Efficient Simulations Beyond Multitape Turing Machines." ECCC TR26-223, 2 Oct 2026. https://eccc.weizmann.ac.il/report/2026/223/ — checked: yes (abstract)
- `HPR26` — A. Henzinger, E. Pyne, S. Ragavan. "Catalytic Tree Evaluation From Matching Vectors." arXiv:2602.14320 (v3 8 Nov 2026); ECCC TR26-022. — checked: yes (abstract)
- `LiT26` — Z. Li, R. Tell. "Trading Time, Space, and Alternations: General Plasticity for Algorithms from Hardness of Range Avoidance." ECCC TR26-233, 7 Oct 2026. — checked: yes (abstract)
- `ChW26` — L. Chen, Y. Wang. "Separating RAM and Multitape Turing Machines with Short Random Oracles." ECCC TR26-006, Jan 2026. — checked: yes (abstract)
- `OAI26t` — OpenAI. "Simulating One-Tape Time in Two-Fifths-Power Space." OpenAI Math Release, 25 Sep 2026. https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026 ; lean/docs/137.md — checked: yes (§1; Lean not built)
- `Nye25` — L. Nye. "TIME[t] ⊆ SPACE[O(√t)] via Tree Height Compression." arXiv:2508.14831 (v4 1 Jan 2026, author states the proof is incorrect). — checked: yes (abstract and comment)
- `AC26` — V. R. Asadi, R. Cleve. "Polynomial-Time Almost Log-Space Tree Evaluation by Catalytic Pebbling." arXiv:2604.02606 (withdrawn v2); ECCC TR26-044. — checked: yes (abstract and withdrawal note)

Explicit lower bounds and QBF:
- `Weh25` — M. Wehar. "Unconditional Time and Space Complexity Lower Bounds for Intersection Non-Emptiness." arXiv:2512.00297 (v2 23 Mar 2026). — checked: yes (abstract)
- `BM26` — A. R. Balasubramanian, R. Majumdar. "Pushdown Reachability Requires N^{3/2} Time on Multitape Turing Machines." arXiv:2611.27814, 20 Nov 2026. — checked: yes
- `SwW15` — J. Swernofsky, M. Wehar. "On the complexity of intersecting regular, context-free, and tree languages." ICALP 2015, LNCS 9135:414–426. — checked: no (via BM26)
- `OAI26w` — OpenAI. "Unconditional time lower bounds for Weisfeiler–Leman equivalence" (with companions). OpenAI Math Release family 133, 25 Sep 2026; lean/docs/133.md — checked: yes (catalogue abstract, Lean scope doc)
- `OAI26m` — OpenAI. "Integer multiplication below n log n." OpenAI Math Release family 109, 23 Sep 2026. — checked: yes (catalogue abstract)
- `Tal26` — Y. Tal. "Sorting in o(N log N) Time on a Multitape Turing Machine." ECCC TR26-331, 22 Nov 2026. — checked: yes (abstract)
- `Wil08q` — R. Williams. "Non-Linear Time Lower Bound for (Succinct) Quantified Boolean Formulas." ECCC TR08-076, 2008. — checked: yes (abstract)
- `SaW15` — R. Santhanam, R. Williams. "Beating exhaustive search for quantified Boolean formulas and connections to circuit complexity." SODA 2015; ECCC TR13-108. — checked: yes (abstract)
- `CY26` — Z. Chen, H. Yao. "An Improved Algorithm for Quantified Boolean Formulas." arXiv:2611.10633, 7 Nov 2026. — checked: yes (abstract)

Nondeterministic vs deterministic:
- `PPST83` — W. Paul, N. Pippenger, E. Szemerédi, W. Trotter. "On determinism versus non-determinism and related problems." FOCS 1983, 429–438. https://trotter.math.gatech.edu/papers/34.pdf — checked: yes
- `San01` — R. Santhanam. "On separators, segregators and time versus space." CCC 2001, 286–294; ECCC TR01-022. — checked: yes (abstract)
- `Lip09` — R. Lipton. "Simulation of nondeterministic machines." Gödel's Lost Letter blog, May 2009. https://rjlipton.com/2009/05/11/simulation-of-nondeterministic-machines/ — checked: no (via SS26)
- `KLRS12` — S. Kalyanasundaram, R. Lipton, K. Regan, F. Shokrieh. "Improved Simulation of Nondeterministic Turing Machines." Theor. Comput. Sci. 417:66–73, 2012. — checked: no (via SS26)
- `Mor81` — S. Moran. "Some results on relativized deterministic and nondeterministic time hierarchies." J. Comput. Syst. Sci. 22(1):1–8, 1981. — checked: no (via SS26)
- `Dot10` — D. Doty. "An Oracle Strongly Separating Deterministic Time from Nondeterministic Time, via Kolmogorov Complexity." arXiv:1004.3993, 2010. — checked: no (via SS26)
- `Hau16` — M. Hauptmann. "On Alternation and the Union Theorem." arXiv:1602.04781, 2016 (unrefereed claim P ≠ Σ₂^p; cited only for its statement of Gupta's DTIME(t) ⊊ Σ₂(t)). — checked: yes (abstract)
- `Cru26` — C. Cruz. "Separating Nondeterministic Time from Deterministic Space." Preprint and Lean development, https://github.com/SeniorMars/ntime.dspace (paper dated 10 Nov 2026; PDF built 22 Nov 2026). — checked: yes (paper, READMEs; Lean not built)
- `cslib2226` — cslib-community/cslib-frontier issue #2226, "Formalize Cruz's sublinear-space simulation of nondeterministic time" (opened 1 Nov 2026). https://github.com/cslib-community/cslib-frontier/issues/2226 — checked: yes (WebFetch)

Fine-grained and algorithms:
- `AVW26` — J. Alman, V. Vassilevska Williams. "Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs." arXiv:2610.06783, 5 Oct 2026. — checked: yes (abstract)
- `AntAPSP` — Anthropic. formal-math `3sum-apsp/` README (Lean v4.33.1). https://github.com/anthropics/formal-math — checked: yes (README summary)
- `KL26` — S. R. Karingula, S. Lovett. "A simplified proof of polynomial improvements for 3SUM and APSP." ECCC TR26-247; arXiv:2610.15663. — checked: yes (abstract)
- `CIMY26b` — T. Chan, R. Itakura, Z. Ma, Y. Yu. "3SUM Made Simpler (Without Matrix Multiplication), k-SUM Hypothesis Refuted for Odd k, and Real 3SUM/APSP Derandomized." arXiv:2610.42012 (v2 14 Nov 2026). — checked: yes (abstract)
- `LiYe26` — B. Li, L. Ye. "Subset Sum via Partial Match." arXiv:2610.10446 (v2 2 Nov 2026). — checked: yes (abstract)
- `OAI26ss` — OpenAI. "Subset Sum in Time O(2^{0.49n})" (4 Oct 2026) and "A Low-Space Algorithm for Worst-Case Subset Sum" (26 Sep 2026). OpenAI Math Release family 138. — checked: yes (catalogue abstracts)
- `CLY26` — B. Cui, S. C. Liu, Y. Yu. "Improved Deterministic Algorithms for k-SAT: Generalization of Chains and Recurrence Proof." arXiv:2611.16814, 12 Nov 2026. — checked: yes (abstract)
- `JC26` — T. Jiang, S. Cai. "A Better Analysis For PPSZ For 3-SAT." arXiv:2607.10697 (v2 27 Oct 2026). — checked: yes (abstract)
- `Zho26` — G. Zhou. "Quadratic-Time Barriers from Self-Referential SAT." arXiv:2611.07308, 5 Nov 2026. — checked: yes (abstract)
- `CIP06` — C. Calabro, R. Impagliazzo, R. Paturi. "A Duality between Clause Width and Clause Density for SAT." CCC 2006. https://cseweb.ucsd.edu/~paturi/myPapers/pubs/CalabroImpagliazzoPaturi_2006_ccc.pdf — checked: no (bound not legible in extraction)
- `AWY15` — A. Abboud, R. Williams, H. Yu. "More Applications of the Polynomial Method to Algorithm Design." SODA 2015, 218–230. — checked: no

Space-complexity context:
- `OAI26L` — OpenAI. "Exact derandomization of logarithmic space: L = RL = BPL." OpenAI Math Release family 103, 23 Sep 2026; lean/docs/103.md — checked: yes (catalogue, Lean scope doc)
- `Hoz26` — W. Hoza. "NL = UL." ECCC TR26-323, 20 Nov 2026. — checked: yes (abstract)
- `Bha26` — S. Bhardwaj. "Unconditional Separation between LL and CLL." ECCC TR26-252; arXiv:2610.15554. — checked: yes (abstract)

Commentary:
- `For26r` — L. Fortnow. "Respect the P v NP Problem." Computational Complexity blog, 10 Jun 2026. https://blog.computationalcomplexity.org/2026/06/respect-p-v-np-problem.html — checked: yes
- `OAIcat` — L. Fortnow. Catalogue of the OpenAI math TCS results. https://lance.fortnow.com/openai-math-tcs.htm — checked: yes (WebFetch, partial)
- `Gas19` — W. Gasarch. "The third P =? NP poll." SIGACT News 50(1), 2019. https://www.cs.umd.edu/users/gasarch/papers/poll3.pdf — checked: no

---

## 11. Search log

Lab context read first: `CLAUDE.md`, `research/KNOWN_RESULTS.md`, `survey/00-director-sources.md`, `survey/01-…` (§1–6),
`survey/02-…` (§4–5), `reviews/survey-01-…crosscheck.md` (relevant parts), `LOG.md`, `DIRECTIONS.md`.

cslib-frontier (local clone `/tmp/claude-0/ext/cslib-frontier`, commit 1435284b): `ROADMAP.md`, `results/README.md`,
`roadmap/complexity.md` (sections on time–space, catalytic, fine-grained), `roadmap/machines.md`; grep for TISP, QBF,
Williams, TreeEval, NTIME, DSPACE, OneTape, Pebbling; read `Classes/TimeSpace/*.lean`,
`Classes/CountingSimulation/{FastSimulation,CountingClasses,Separation}.lean`, `SingleTape/{Palindrome,NLogNGap}.lean`,
`Classes/Space/TQBF.lean`, the NTIME definition in `Classes/Time.lean`, `CslibFrontierResults/Entries.lean`.
GitHub issues via WebFetch (the `gh` API returned "access … not enabled"): #888, #2855, #2896, #2226; issue searches
`q=Pippenger`, `q=NTIME SPACE`.

arXiv (API worked for the first few queries, then returned "Rate exceeded"; then used arxiv.org/abs and listing pages):
- API: `id_list=2502.17779,2611.11832`; `all:"tree evaluation"`; `all:"square-root space"`; `abs:"Cook-Mertz"`;
  `id_list=2508.14831,2504.20950,2602.14320,2604.02606,2512.00607`; `id_list=1602.04781,2011.02428,1012.2034,1001.0746`;
  `abs:"alternation-trading"`; `abs:"quantified Boolean formulas" AND abs:"lower bound" AND cat:cs.CC`.
- Listings (WebFetch, title scan): https://arxiv.org/list/cs.CC/2026-11 (both halves), https://arxiv.org/list/cs.CC/2026-10
  (both halves), https://arxiv.org/list/cs.DS/2026-11 (three parts).
- Abstract pages: 2610.24377, 2611.27814 (+ PDF), 2512.00297, 2610.06783, 2610.42012, 2611.07308, 2611.10633, 2611.16814,
  2607.10697, 2610.10446, 2306.15817, cs/0608085; PDFs: 2502.17779v1, 2611.11832v1, 1309.3690.
ECCC (curl got "Empty reply"; WebFetch worked; PDF download worked with a browser user agent): year pages 2026 and 2025;
reports 2026/223, 2026/233, 2026/331, 2026/006, 2026/323, 2026/252, 2026/247, 2023/174, 2008/076, 2007/036, 2001/022 (PDF
text unreadable: Type-3 fonts), 2013/108.
Other primary sources: Buss–Williams journal PDF (mathweb.ucsd.edu); van Melkebeek survey PDF (pages.cs.wisc.edu);
FLvMV PDF (lance.fortnow.com; first attempt HTTP 406, retried with headers); PPST83 PDF (trotter.math.gatech.edu, via
epubs.html); Ajtai (theoryofcomputing.org); BSSV FOCS PDF (homes.cs.washington.edu); Lipton–Williams PDF
(people.csail.mit.edu); Williams likelihoods PDF; Cruz repository (raw.githubusercontent.com: README, PDF, lean/README);
OpenAI math `CONTENTS.md` and `lean/docs/{103,133,137}.md` (109 and 138: HTTP 404) and the one-tape PDF; Anthropic
formal-math README; Fortnow's OpenAI-TCS catalogue; ethdiscussion.blog home, "New Results Related to ETH", "Links To
Other Work"; Shtetl-Optimized ?p=10239; Computational Complexity blog 2026/06; MFCS 2026 talk page (drops.dagstuhl.de).
Web searches (WebSearch): Buss–Williams limits; Williams counting modulo integers; van Melkebeek survey; Cruz NTIME
DSPACE; Santhanam separators; PPST Σ₄; Beame–Saks–Sun–Vee; Beame–Vee; Lipton–Williams QBF; Santhanam–Williams QBF;
Calabro–Impagliazzo–Paturi; Abboud–Williams–Yu; Gasarch poll; Fortnow "Respect the P v NP Problem"; Williams 2026
thread (not found); "ETH Repository" McGuire (not found); OMv refutation 2026 (none found); new time–space SAT bounds
2026 (none found); improved BP tradeoffs 2023–2026 (none found).

Could not open / not used:
- DBLP API (bot-protection page), Semantic Scholar API (HTTP 429).
- J. ACM page for Williams 2025 (dl.acm.org HTTP 403); Beame's site page for Beame–Vee (404); Santhanam's 2001 PDF
  (unreadable fonts; abstract used); CIP06 PDF (symbols lost).
- McGuire's note and any Yang–Pitassi preprint (no public copy found); Williams' 23 Nov 2026 thread (no public copy
  found; director's screenshots not reopened, per CLAUDE.md's instruction to leave root-level files alone).
- Not exhaustive: arXiv cs.CC Oct 2026 listing entries beyond those returned; ECCC 2025 entries after TR25-174 were
  scanned only by title in a second pass; no Google Scholar, MathOverflow or cstheory search.
