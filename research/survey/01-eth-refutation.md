# 01 — The claimed refutation of the Exponential Time Hypothesis (Oct 2026)

Lit-scout survey, area 01 "eth-refutation". Written 2026-11-23. Single author: lit-scout (Claude). Not yet
cross-checked by a second agent.

**How to read the labels.**
- `checked: yes` means I opened the primary source on 2026-11-23 (paper PDF, arXiv abstract, Lean file or README)
  and the statement in the row matches it. `checked: yes (abstract)` means only the abstract was read.
- `checked: no` means the statement comes from a secondary source (another paper citing it, a blog comment, a news
  story) or from memory. Do not build on these without opening the source.
- "claimed" means the authors claim it and no completed independent review exists. **No result in this file has
  the lab status `lean-verified`.** The external Lean checks described below are the authors' own, plus
  third-party re-runs. They are evidence, not the lab's own verification.
- "Lead-scout inference" marks my own reasoning. Its status is `informal-argument` and nobody has red-teamed it.

---

## 1. Plain-language summary

In October 2026 two AI labs released papers, each with a computer-checked (Lean 4) proof. OpenAI's paper is
"The Exponential Time Hypothesis is False". Anthropic's is "A 2^{o(n)} Time Algorithm for 3-SAT", with author line
"Claude, Anthropic". Both claim that a widely used assumption in computer science, the Exponential Time Hypothesis
(ETH), is false.

ETH said that 3-SAT needs running time c^n for some fixed c > 1. 3-SAT is the classic puzzle "can this logical
formula over n true/false variables be made true?". In other words, ETH said you cannot do fundamentally better than
trying all 2^n assignments. Both papers give deterministic algorithms that even **count** all solutions in time
about 2^{n/√(log n)}. That grows more slowly than any c^n, so ETH fails, and so do the stronger assumptions built on
it (SETH, NSETH, Gap-ETH, #ETH).

The algorithms are "galactic". By the authors' own analysis they beat brute force only on inputs astronomically
larger than anything that could ever be written down, for example more than 10^(10^8) variables.

As of 23 Nov 2026, nobody has reported a flaw:
- Several people have independently re-run both Lean proofs.
- O'Donnell, Sellke, Kintali and Porat have written simpler explanations of them, and Nederlof has announced one.
- The review organised by Impagliazzo, Paturi and R. Williams says explicitly that it is "not certification", and
  I found no published verdict.

The result does **not** settle P vs NP. The speed-up is lost under the usual reductions between NP problems: all of
NP would need about 2^{n^{o(1)}}, not 2^{n/√log n}. It also does not speed up satisfiability for general circuits or
for CNF formulas with long clauses.

It does give a small new circuit lower bound through Williams' "algorithms imply lower bounds" method. Some problem
in the class E^NP needs circuits with more than about n·√(log n) gates.

Many follow-ups appeared within four weeks. Several re-use the shared algebraic trick: rewriting "equality / swap"
constraints as a low-rank part plus a structured part. Examples are subexponential simulation of nondeterministic
Turing machines and refutations of the k-Clique and hyperclique hypotheses.

The lab can realistically contribute in three places:
1. Re-using and finishing the Lean artifacts for our formalization track.
2. Computer-assisted search for better algebraic decompositions, which would sharpen the circuit lower bound.
3. The proof-complexity side of the new algorithms.

---

## 2. Frontier table

Notation: n is the number of variables, m the number of clauses, k the clause width (fixed unless stated). In
[OAI26] "log" is the natural logarithm. In [Ant26] "log" is log₂. Inside O(·) in the exponent the base does not
matter.

### 2.1 The two primary claims (released 26 Oct 2026)

| id | precise statement (model, problem, bound) | reference | checked |
|---|---|---|---|
| F1 | **Deterministic #k-SAT, every fixed k ≥ 2** (n ≥ 20 declared variables, m clauses). Time: (n+m)^{O_k(1)}·2^{O_k(n log log n/√log n)} bit operations. Space: (n+m)^{O_k(1)} bits. For m ≤ Dn (fixed D): (n+m)^{O_{k,D}(1)}·2^{O_{k,D}(n/√log n)}. Proved in App. D by Boolean tensor contraction. | OpenAI, *The Exponential Time Hypothesis is False*, preprint dated 17 Oct 2026, rev. 25 Oct 2026, 67 pp., Theorem 1.1 [OAI26] | yes |
| F2 | Weaker body version ("interpolation algorithm"): #k-SAT in (n+m)^{O_k(1)}·2^{O_k(ρ(n))} bit ops and poly space, with ρ(n) = n(log log n)²/√log n = n/(log n)^{1/2+o(1)} | [OAI26] Prop. 6.4; Thm 1.1 remark | yes |
| F3 | Common zeros of sparse F₂ systems: m_test ≤ cn polynomials, each a list of ≤ (log n)^c monomials of degree ≤ k. The number of common zeros is computed deterministically in 2^{O_{k,c}(n(log log n)²/√log n)} bit ops and n^{O_{k,c}(1)} space | [OAI26] Theorem 2.2 | yes |
| F4 | **Boolean tensor contraction:** a bipartite tensor network with ≤ Cs edges, max degree ≤ ⌈s^{9/10}⌉ and entries in (Z/2^{P₀}Z)[V]/(V^ℓ) (P₀, ℓ ≤ Cs) is contracted deterministically in (s+L)^{O(1)}·2^{O(s/√log s)} bit ops and (s+L)^{O(1)} space | [OAI26] Theorem D.1 | yes |
| F5 | **OpenAI Lean statement** `exact_count_and_sat` (Lean v4.34.1). For each k ≥ 2: one "PrimitiveMachine" (multitape TM over Option Bool), constants C, A, S, d, e > 0. For every width-≤k CNF F (a Finset of Finset-clauses) it outputs #F and the decision bit within C·(L+1)^d·2^{A·n(ln ln(n+16))²/√ln(n+16)} steps. Visited cells ≤ S·(L+1)^e at every prefix. L is the bit length of a **unary** variable-index encoding. Matches F2, **not** F1. | `openai/math` `lean/ComparatorChallenges/SubexponentialSAT.lean`; scope note `lean/docs/378.md` | yes |
| F6 | **Deterministic #k-SAT, one algorithm uniform in k** (word RAM). Input: a k-CNF with m clauses in which n variables occur. Time 2^{O(min{k²·n·log log n/√log n, k·m/√log m})}, with an absolute constant. Sparse inputs: 2^{O(kn/√log n)} (footnote 1). | Claude (Anthropic), *A 2^{o(n)} Time Algorithm for 3-SAT*, 26 Oct 2026, Theorem 1 [Ant26] | yes |
| F7 | Simplified version: ∀δ > 0 there is a deterministic algorithm counting the solutions of a 3-CNF (any m) in O(2^{δn}) | [Ant26] Theorem 2 | yes |
| F8 | Decision only, no log log factor: 3-SAT in 2^{O(n/(log n)^{α′/10})} with α′ = log(1/ρ) = 1/2, i.e. 2^{O(n/(log n)^{1/20})} | [Ant26] Theorem A(d), App. A | yes |
| F9 | **Anthropic Lean statements** `MainResults.mainTheorem` and `MainResults.ethIsFalse`. Lean v4.33.1, Mathlib v4.33.1, machine `Turing.FinTM2` with all stack alphabets finite. One machine and one constant C for all k ≥ 1, n ≥ 4, m ≥ 2, all variables occurring and no repeated clause. It counts within ⌊2^{C·min{km/√log m, k²n log log n/√log n}}⌋ steps. ETH is defined as 0 < s₃. | `anthropics/formal-math` @16a5ce4 `eth/MainResults.lean`, `Challenge.lean` | yes |
| F10 | Corollaries claimed by both papers. ETH, SETH, NSETH and #ETH are false. Gap-ETH and the bounded-error randomized versions of ETH, SETH and Gap-ETH are also false ([OAI26] §1.1.1). OpenAI: "Theorem 1.1 refutes ETH, SETH, Gap-ETH, and NSETH". Anthropic Cor. 5: "s_k = 0 for every k ≥ 3. Hence s∞ = 0, and both ETH and SETH are false". Anthropic §7 adds that NSETH is false and Cor. 6 that #ETH is false. | [OAI26] §1.1.1–1.1.2; [Ant26] Cor. 5, 6, §7 | yes |
| F11 | Graph counting. Independent sets and proper q-colourings in 2^{o(v)} time with poly_q(v,e) space. Perfect matchings in 2^{o(v+e)} ([OAI26] Cor 1.3). Independent sets, cliques, vertex covers and dominating sets of size s, and proper k-colourings, in O(2^{δn}) for all δ > 0 ([Ant26] Cor 7) | [OAI26] Cor 1.3; [Ant26] Cor 7 | yes |
| F12 | Max-k-SAT: randomized, finds an assignment satisfying ≥ OPT − εm clauses w.p. 1 − 2^{−Ω(n)} in (n+m)^{O_{k,ε}(1)}·2^{O_{k,ε}(ρ(n))} | [OAI26] Cor 1.2 | yes |
| F13 | Inverting maps with constant output locality d. Exact preimage count and a preimage in deterministic (n+m)^{O_d(1)}·2^{O_d(ρ(n))} time, poly space. Covers constant-locality Goldreich one-way function candidates, but "does not rule out one-wayness against polynomial-time algorithms" | [OAI26] Cor C.2 | yes |
| F14 | **Circuit lower bounds.** (a) E^NP ⊄ SIZE(O(n)): Cor C.1 applies [Wil10, Thm 6.1] to F1/F6. (b) Quantitative: there exist L ∈ E^NP and c > 0 with C_L(n) > c·n·√(log n) for infinitely many n. C_L counts non-input gates, any fan-in-2 Boolean gates, unrestricted fan-out. Uses the fixed-density bound of F1 and the local reductions of Jahanjou–Miles–Viola. | [OAI26] Cor 1.4, Cor C.1, App. C.1; [Ant26] §7 | yes |
| F15 | Williams' implication used in F14: "Theorem 6.1. If the Exponential Time Hypothesis is false, then E^NP does not have linear size circuits." Footnote 5: "To the best of our knowledge, linear size circuit lower bounds are not known for this class." | R. Williams, *Improving Exhaustive Search Implies Superpolynomial Lower Bounds*, STOC 2010 / SICOMP 42(3) 2013; manuscript at people.csail.mit.edu/rrw/improved-algs-lbs2.pdf | yes |

Verbatim anchors (for the red-team):
- [OAI26] abstract: "For every fixed k ⩾ 2, on a formula with n variables and m clauses, our algorithm uses
  poly_k(n, m) space and runs in time (n + m)^{O_k(1)} 2^{n/(log n)^{1/2+o(1)}}."
- [OAI26] §1: "Note that runtime bounds of the form 2^{o(n)} do not transfer under general polynomial-time
  reductions (2^{n^{o(1)}} would be needed for this), so our result does not imply that general NP problems admit
  subexponential time algorithms."
- [OAI26] App. C.1: "The corollary gives a language in E^NP without a linear-size circuit family; it does not assert
  a superpolynomial circuit lower bound for NP."
- OpenAI Lean scope note (378.md): "For fixed k≥2, Lean proves that a deterministic machine exactly counts satisfying
  assignments of a canonically encoded k-CNF on n variables in time (L+1)^{O_k(1)}2^{O_k(n(log log n)^2/√log n)}".
- [Ant26] §1: "Our main theorem refutes the exponential time hypothesis … However, our result does not bear on the
  P vs NP question directly, nor does it yield any practical algorithms for NP-complete problems." And: "Theorem 1
  does *not* refute the Orthogonal Vectors hypothesis".
- [Ant26] §1: "for arbitrary 3-CNF formulas with m = 5n clauses, the bound we prove does not improve on the 2^n of
  exhaustive search unless n > 10^{10 000}, and the bound in n alone … does not unless n > 10^{10^8} … Our general
  approach seems unlikely to yield any general improvement unless n > 10^7". (Read from the rendered PDF page 2.)
- [Ant26] Provenance: "The core algorithm was found on October 16 by an internal Claude research model with 14M
  output tokens and no human input."
- OpenAI announcement (26 Oct 2026): "Our AI found its natural language disproof for the ETH on October 16th,
  2026" and "formalized the result in Lean on October 17th, 2026" (quoted via WebFetch of the page).
- [Ant26] §1: Claude's literature search found "more than 800 papers that prove at least one result of their own
  only under ETH or under a hypothesis that implies it, such as SETH or Gap-ETH".
- OpenAI's prompt, released by Paturi on 12 Nov 2026, asked the model to "Research an unconditional refutation of
  the deterministic Strong Exponential Time Hypothesis (SETH)". This is quoted via WebFetch of the ethdiscussion
  post.

### 2.2 Independent expositions, simplifications and re-derivations (evidence that experts understand the proofs)

| id | statement | reference | checked |
|---|---|---|---|
| E1 | **Permanent formulation of OpenAI's proof.** Deterministic exact permanent of an n×n rational matrix with O(1) nonzeros per row and column in 2^{O(n(log log n)²/√log n)} (Thm 6.1). Sparse #3-SAT follows via Valiant / Ben-Dor–Halevi reductions. Poly space (App. A). Randomized #3SAT for arbitrary 3-CNFs: always returns an upper bound, exact w.p. ≥ 3/4, time 2^{O(n(log log n)³/√log n)}, poly space (Thm B.1). Also NTIME(T) ⊆ DTIME(2^{O(T(log log T)³/√log T)}) via Subercaseaux's encoding. The author notes the text was "Produced by odonnell@cs.cmu.edu through interaction with LLMs". | R. O'Donnell, *Some exposition of "The Exponential Time Hypothesis Is False"*, 30 Oct 2026, cs.cmu.edu/~odonnell/some_eth_false_exposition.pdf | yes |
| E2 | Simplified OpenAI route, decision only: ∀ε > 0, 3-SAT in C_ε·(n+m+1)^{c_ε}·2^{εn} bit operations | S. Kintali, *A simplified proof of ETH is false*, 26 Oct 2026, shivakintali.github.io/papers/ETH.pdf | yes |
| E3 | Slides: *An Outline of OpenAI's Algorithm for k-SAT in 2^{o(n)} Time* | M. Sellke, 28 Oct 2026, msellke.com/Files/ETH-False-Slides.pdf | yes (title only) |
| E4 | Exposition of Anthropic's algorithm: "an algebraic identity that rewrites two such crossing connections as connections within columns minus connections within rows", plus a Gram–Schmidt low-rank decomposition. Gives O_{k,δ}(2^{δn}) for #k-SAT | E. Porat, *Digesting the Subexponential Algorithm for #k-SAT*, draft 12 Nov 2026, eitanporat.github.io/papers/ksat.pdf | yes (abstract + intro) |
| E5 | Interview: O'Donnell covered the proof "more or less completely in two lectures"; he says "I have actually never looked at the OpenAI proof" (he worked from it via LLM conversation) | V. Rozhoň, *Ryan O'Donnell on the Exponential Time Hypothesis*, Substack, 13 Nov 2026 | yes (via WebFetch summary) |
| E6 | Lean: ∀ε > 0, 3-SAT decided in C·(ℓ+1)^d·2^{εn} steps on OpenAI's primitive multitape machine. Three proofs ("Uncrossing Wires" builds on Claude's proof). README claims only standard axioms. | S. Zhuang, github.com/suquark/NotETHSimplified (Nov 2026) | yes (README only; not built) |
| E7 | J. Nederlof: Anthropic's improvement comes from a "crossing inequality" plus "clever (though perhaps somewhat non-standard) recursion"; exposition in progress. J. Nelson shared an exposition of Anthropic's proof. | ethdiscussion.blog comment, 5 Nov 2026; Shtetl-Optimized comment #75 | no (reported) |

### 2.3 Follow-ups, 16 Oct – 23 Nov 2026 (using the result or its technique)

| id | statement | reference | checked |
|---|---|---|---|
| C1 | **NTIME[t] ⊆ DTIME[2^{O(t log log t/√log t)}]** from the published 3-SAT algorithms, and **NTIME[t] ⊆ DTIME[2^{O(t/√log t)}]** from "a stronger consequence of their proof" (multitape TMs). Any subexponential algorithm for circuit-CSPs transfers to NTIME with the same savings. | C. Strassle, B. Subercaseaux, arXiv:2611.11832 (9 Nov 2026) | yes (abstract) |
| C2 | Anthropic's recursion made explicit and its crossover points lowered: at clause density 1, from 2^{33858} to ≈2^{420} clauses; for general 3-SAT in n, from 2^{2.2·10^{12}} to ≈2^{8.6·10^9}. Counting assignments satisfying exactly j clauses in 2^{O(m/√log m)}, which refutes the **Sparse Max-3-SAT Hypothesis** (Alman–Vassilevska Williams). Defines a "rewrite-and-merge" class: no grid algorithm in it gains for general 3-SAT below ≈2^{6000} variables. For two balanced homogeneous merges, the exponent is ≥ (log₂K)^{−3} per edge bit (via quantum functionals), "which excludes running times 2^{n^{1−c}}". On the 4-node complete graph, the "Signed Network Sums" model contracts in N^{23/6} if ω = 2. | R. Majdoddin, arXiv:2610.41622 (30 Oct 2026) | yes (abstract) |
| C3 | Constants and limits of OpenAI's preprint. Treating the hidden constant C as a parameter, the general bound beats 2^n only for n ≳ 10^{32} (C=2), 10^{126} (C=3), 10^{3517} (C=10). Using the constants extracted from the tensor-contraction proof, the bound stays above 2^n at bounded density unless log₂(n+m) > 10^9. For the clause-product interpolation scheme in their cost model: 2^{Ω(√tw)}, 2^{Ω(√n)} w.h.p. on random 3-CNF above density 3, and 2^{Ω(n^{1/3})} on path formulas. They "explain why the preprint's sharper routes escape these limits". | F. Dias, Y. Lima, arXiv:2611.00517 (31 Oct 2026) | yes (abstract) |
| C4 | #3SAT in 2^{O(n/f(n))} implies #PPM (permutation pattern matching) in 2^{O(n√(log f(n)/f(n)))}. Hence #PPM becomes subexponential. | L. Kozma, arXiv:2610.41048 (29 Oct 2026) | yes (abstract) |
| C5 | Exact-One Hitting Set (Karp's 21), counting, deterministic poly space, 2^{O(r log log(r+16)/√log(r+16))}·poly(L+1), with unrestricted set widths | S. Chen, T. Jiang, Y. Zhu, arXiv:2611.00994 (31 Oct 2026) | yes (abstract) |
| C6 | Conditional on [OAI26] Thm D.1: full size distribution of feedback vertex sets in poly(n+m)·2^{O(n(log log n)²/√log n)} | M. Wu, M. Wang, arXiv:2611.02548 (2 Nov 2026) | yes (abstract) |
| C7 | **E^NP lower bounds for extended bases.** From [Ant26]'s counting theorem: an E^NP language needing Ω(m√log m/log log m) gates over unbounded AND/OR plus binary XOR, i.o. From [OAI26]'s contraction theorem: a bounded binary basis with a linear budget of arbitrary XOR and symmetric gates needs Ω(m√log m) gates i.o. | M. Wu, M. Wang, arXiv:2611.02560 (2 Nov 2026) | yes (abstract) |
| C8 | Stearns–Hunt Satisfiability Hypothesis (SH, 1990) ⇔ **Weak ETH**, defined as: ∀ε > 0, 3SAT on n variables is not in O(2^{n^{1−ε}}). Also #SH ⇔ Weak #ETH. Under SH, a reduction from 3SAT size s to N ≤ s^{b+o(1)} rules out O(2^{N^{1/b−ε}}). Under #SH there is no O(2^{s^{1−ε}}) for #2SAT of size s. | MIT Hardness Group, J. Brunner, E. Demaine, F. Frei, T. Gomez, M. Hecher, J. Li, J. Lynch, *ETH is Dead, Long Live SH*, arXiv:2611.02650v2 (2 Nov, v2 16 Nov 2026) | yes (abstract + intro) |
| C9 | k-Clique in n^{(ω/3−c)k} for all large k, with c > 0 independent of ω and k (weighted counting). The proof "makes central use of an algebraic decomposition lemma that we distilled, with a publicly available AI model's assistance, out of the recent ETH refutation of OpenAI" | V. Vassilevska Williams, O. Zamir, arXiv:2611.09764 (6 Nov 2026) | yes (abstract + intro) |
| C10 | k-hypercliques in (k−1)-uniform hypergraphs are counted in O(n^{k−ε_k}). Max-kSAT in 2^{(1−ε)n}·poly(m,n). k-AP detection in n^{2−ε}. Remark 1: a decomposition of the identity "(writing I as the sum of a 'low rank' matrix and a very sparse and structured matrix) also appears in the recently-announced OpenAI algorithm" | J. Alman, B. Li, N. Pant, K. Pratt, R. Williams, arXiv:2611.05082 (3 Nov 2026) | yes (abstract + intro) |
| C11 | k-cliques in h-uniform hypergraphs in O(n^{(1−ε_h)k}), which refutes the Hyperclique and k-AP hypotheses. "This result is almost entirely due to AI." | N. Fischer, arXiv:2611.03880 (2 Nov 2026) | yes (abstract) |
| C12 | Truly subquartic 4-hyperclique in 3-uniform hypergraphs, giving faster Max-3-SAT | T. Chan, R. Itakura, Z. Ma, Y. Yu, arXiv:2611.06813 (4 Nov 2026) | yes (abstract) |
| C13 | Counting 6-cliques in O(n^{5.97}) time and O(log n) space, and Max Cut in O(1.994^n) with poly space. Uses "a decomposition of an equality indicator function underlying … the refutations of ETH by OpenAI and Anthropic" | A. Jabal Ameli, N. Mohrin, J. Nederlof, arXiv:2611.24750 (18 Nov 2026) | yes (abstract) |
| C14 | Depth-h circuits for hyperclique need m^{Ω(ℓ)} gates for ℓ ≤ m^{1/h−ε}. This proves the **k-OV conjecture for constant-depth circuits** in polylog dimension. Depth-3 circuits for 2-OV need Ω(n²) wires, answering a question of Kane–Williams. | N. Chukhin, arXiv:2611.06231 (4 Nov 2026) | yes (abstract) |
| C15 | Twelve running-time lower bounds historically based on ETH, recovered under FPT ≠ W[1] | H. Molter, arXiv:2611.26080 (19 Nov 2026) | yes (abstract) |
| C16 | New work already uses weakened hypotheses. Euclidean Steiner Tree uses "weak ETH: no 2^{n^γ}-time algorithm … for any constant γ<1". k-means uses Almost-ETH. | S. Bartlmae, arXiv:2611.24611; Karthik C. S., D. Minzer, arXiv:2611.14892 | yes (abstract) |
| C17 | Lean replications and bridges are in §7. Replicators: T. Busnello, N. Jose, C. Toledo; bridge authors: D. Hawkley, C. Toledo. | ethdiscussion.blog "Lean Replications" thread; carlostoledo.co/eth | yes (WebFetch of pages) |

**Claims seen only in blog comments (unverified; listed so the lab does not re-derive them blindly).** All are from
comments on ethdiscussion.blog "New Results Related to ETH" (1–16 Nov 2026). checked: no for every item.
- N. Chukhin. Fan-in-2 circuits of size s are "equivalent to AC⁰[q] circuits (q odd)". Constant depth gives size
  2^{εn}; depth O(log log s) gives size 2^{O(s/log^{0.125} s)}. Also NTIME_RA[t] ⊆ DTIME[2^{O(t/√log t)}]
  (Google Drive notes).
- A. Gheorghiu, A. Gupte. Exact classical sampling from quantum circuits: O(n) gates from a finite gate set in
  poly(n)·exp(n/√log n). O(n) Hadamards plus O(n·exp(o(√log n))) diagonal gates in exp(o(n)).
- S. Szeider (Zenodo notes):
  - every weighted model count of a 3-CNF has an arithmetic circuit of size 2^{o(n)};
  - every unsatisfiable 3-CNF has an **IPS refutation of size 2^{o(n)}**;
  - proposes a "k×k Clique Hypothesis" (no 2^{o(k log k)}); 20 of 29 ETH lower bounds he checked survive verbatim;
  - OpenAI's construction is exhaustive search until n > 2^{10^{10}}, and its App. D algorithm until
    n + m > 2^{131071}.
- J. T. Straub (audit, not an error claim). A packing lemma forces u₀ ≤ (log₂ s)/480 + O(1) in OpenAI's mode
  enumeration. A conditional calculation suggests exponents up to c < 3/5 with better mode-matching.
- C. Cruz. The ETH refutation implies NTIME(n) ⊊ DSPACE(n) (GitHub repository). **A red-team target; see O10.**
- D. P. Sukruth. Parameterized consequences: Vertex Cover in 2^{O(k log log k/√log k)}, Max-Cut in 2^{O(k/√log k)}
  (via Cai–Juedes).
- Y. Tal. Factorials mod p in 2^{O_d(log p/√log log p)} via [OAI26] Thm D.1.

### 2.4 Known limits and obstacles for the new methods

| id | statement | reference | checked |
|---|---|---|---|
| L1 | In the "single tensor network along one contraction tree" model of Austrin–Kaski–Kubjas: "no algorithm for the problem on which we recurse (§2.2) has an exponent below about 4/9 of that of brute force". Anthropic's algorithm escapes this model by "a signed sum of tensor networks" contracted in different orders. | [Ant26] §1.2 and App. G (citing AKK22, ToC 18(16) 2022) | yes ([Ant26] statement; AKK22 not opened) |
| L2 | Rewrite-and-merge class: exponent ≥ (log₂K)^{−3} per edge bit for two balanced homogeneous merges, which excludes 2^{n^{1−c}}. No grid algorithm in the class gains below ≈2^{6000} variables. | [Maj26] = C2 | yes (abstract) |
| L3 | Clause-product interpolation cost model: 2^{Ω(√n)} on random 3-CNF, 2^{Ω(√tw)} in general (C3) | [DL26] = C3 | yes (abstract) |
| L4 | Polynomial-time reductions lose the gain. All of NP in subexponential time would need 3-SAT in 2^{n^{o(1)}}. | [OAI26] §1; Fortnow blog 28 Oct 2026 | yes |
| L5 | "no Sparsification Lemma is known for Max-kSAT for any k". So ¬ETH "evidently says nothing about the full Max-kSAT Hypothesis", which [ALPPW26] refute by other means. | [ALPPW26] §1 | yes |
| L6 | Clause width growing with n. In [Ant26] the n-bound is useful only for k ≤ (log n)^{1/4}: "for larger k that bound is so large that trying all assignments is within it". The CNF-SAT hypothesis with unbounded width is not touched ([OAI26] §1.1.3). | [Ant26] §2.7; [OAI26] §1.1.3 | yes |
| L7 | Regular resolution: "Strong ETH holds for regular resolution" (Beck–Impagliazzo 2013). This is unaffected: [OAI26] says Theorem 1.1 "does not conflict with unconditional exponential lower bounds for restricted proof systems such as regular resolution". | [OAI26] §1.1.1 citing [BI13] | yes ([OAI26]); BI13 not opened |
| L8 | Galactic thresholds. [Ant26]: n > 10^{10^8} for the n-bound. [Ant26] App. A: log m > 8000 is needed at density 1 and log m > 1.3·10^5 at density 5 (necessary conditions). [Maj26] computes 2^{33858} for density 1 from the main term. Sources disagree because they compute different quantities; see §5. | [Ant26] §1, App. A, App. D; [Maj26]; [DL26] | yes |

### 2.5 Hypothesis ledger as of 2026-11-23 (what fell, what stands)

| hypothesis | status per sources found | reference | checked |
|---|---|---|---|
| ETH (deterministic and randomized), #ETH, SETH, NSETH, Gap-ETH | **claimed refuted** (both papers; deterministic algorithm) | [OAI26] §1.1.1–1.1.2; [Ant26] Cor 5–6, §7 | yes |
| MA-SETH | refuted 2016: k-CNF unsatisfiability certified in 2^{n/2}·poly(n,m) | [Wil16] Thm 3.3 as cited in [OAI26] | no (Wil16 not opened) |
| Sparse Max-3-SAT hypothesis (Alman–Vassilevska Williams 2020) | claimed refuted | [Maj26]; [ALPPW26] §1 | yes (abstracts) |
| Max-kSAT hypothesis, Hyperclique hypothesis, k-AP hypothesis | claimed refuted, **not** via ¬ETH | [ALPPW26]; [Fis26]; [CIMY26a] | yes (abstracts) |
| k-Clique hypothesis (n^{ωk/3}) | claimed refuted: n^{(ω/3−c)k} | [VWZ26] | yes (abstract) |
| 3SUM, APSP, Exact Triangle, Zero-Weight k-Clique, rectangular hinted OMv | claimed refuted (Anthropic; 3SUM O(n^{1.9992}), APSP O(n^{2.9995})) | J. Alman, V. Vassilevska Williams, arXiv:2610.06783 | yes (abstract) |
| k-SUM hypothesis for odd k | claimed refuted (randomized O(n^{⌈k/2⌉−ε_k})) | [CIMY26b] arXiv:2610.42012 | yes (abstract) |
| **Orthogonal Vectors (OV) hypothesis** | **stands**. "Theorem 1 does *not* refute the Orthogonal Vectors hypothesis". The k-OV conjecture is proved only for constant-depth circuits. | [Ant26] §1; [Chu26] | yes |
| **CNF-SAT hypothesis (unbounded width): no 2^{(1−δ)n}·poly(n,m)** | **stands** (no refutation found). [OAI26]: "this hypothesis allows the width to grow with n". | [OAI26] §1.1.3 | yes |
| **SH ⇔ Weak ETH ⇔ Almost-ETH**: ∀ε > 0, no 2^{n^{1−ε}} for 3-SAT | **stands**, called "plausible". Manurangsi introduced the same hypothesis as "Almost-ETH" (arXiv v3, 27 Oct 2026). | [MITHG26] §1 and footnote 3 | yes |
| Lokshtanov-style weak ETH: ∃c > 0, 3SAT needs 2^{Ω(n^c)}. Gasarch's proposal: ∃c < 1, no O(2^{n^c}). | stands; weaker than SH | [MITHG26] fn. 3; Gasarch blog 1 Nov 2026 | yes |
| f(k)·n^{o(k)} lower bound for k-Clique (was "under ETH") | **basis lost, not refuted**. Szeider proposes the "k×k Clique Hypothesis"; Lampis notes weakened-ETH forms do not preserve such results. | [MITHG26] §1 (citing Szeider, Lampis); [VWZ26] | yes ([MITHG26]) |
| P ≠ NP, NP ⊄ SUBEXP | unaffected | [OAI26] §1; [Ant26] §1 | yes |

Neighbouring AI-produced results from the same weeks, out of scope but listed for completeness:
- ω ≤ 9/4 for matrix multiplication. OpenAI preprint, 2 Oct 2026, as cited in [ALPPW26]. Constructive proof:
  R. Pass, arXiv:2610.28627. Exposition: Doğan–Lysikov–Sakabe–Walter, arXiv:2611.09716. checked: yes (abstracts).
- "The Unique Games Theorem". OpenAI preprint, 23 Sep 2026, cited in [OAI26] §1. checked: no.

### 2.6 Consequences and non-consequences (what the lab may and may not use)

- **P vs NP: no direct consequence.** Both papers say so ([OAI26] §1; [Ant26] §1). Fortnow: "the OpenAI algorithm
  applies to k-SAT but not to NP problems in general" (blog, 28 Oct 2026). Aaronson, in a blog comment (secondary,
  checked: no; paraphrased by a WebFetch summary), said a subexponential CircuitSAT algorithm would move his own
  P=NP estimate to about 20–30%. As context,
  Williams (2019) estimated ETH 70%, SETH 25%, NSETH 15%, P ≠ NP 80% (likelihoods.pdf, Table 1; checked: yes).
- **Circuit lower bounds via the algorithmic method.**
  - What is new: E^NP ⊄ SIZE(O(n)), and the quantitative bound c·n·√log n i.o. (F14). C7 extends this to other
    gate bases.
  - Before this, [Ant26] §1.2 states: "The best lower bound known before for a language in E^NP, over the full
    binary basis, was 3.1n − o(n) [LY22]; the class S₂E, which contains E^NP, requires circuits of near-maximum
    size [CHR24, Li24]". LY22, CHR24 and Li24 themselves not opened (checked: no).
  - Why it stops at about n·√log n: the technique gives SAT algorithms whose cost is exponential in
    **variables + gates**. It is therefore non-trivial only for circuits of size O(n·√log n). Nothing is gained for
    size n^{1+ε}, for formulas, or for ACC-type classes beyond what is already known (O'Donnell interview; [OAI26]
    App. C).
  - Lead-scout inference (informal-argument): the [OAI26] Cor 1.4 argument needs sparse 3-SAT in
    2^{O(V/a(V))} and returns a lower bound of about η·n·a(n). So:
    1. Anthropic's **Lean-checked** km/√log m bound (F9) already supports the c·n·√log n bound. The Williams /
       Jahanjou–Miles–Viola part of the argument is not formalized.
    2. Any improvement of the sparse exponent saving a(n) improves the E^NP bound in lock-step (see O2).
- **NTIME simulation.** NTIME[t] ⊆ DTIME[2^{O(t/√log t)}] for multitape TMs (C1; also E1).
- **Cryptography.**
  - Constant-locality Goldreich-type one-way function candidates lose 2^{Ω(n)} inversion hardness. Polynomial-time
    one-wayness is untouched (F13, quoting [OAI26] Cor C.2).
  - HackerNoon (secondary, checked: no) quotes Williams via TechCrunch as "reasonably confident" the result does
    not break cryptosystems. It quotes Lokshtanov via WIRED: it "should definitely scare some cryptosystem
    designers".
  - An Oct 29 elliptic-curve preprint mentioned by HackerNoon could **not be found**.
  - A spreadsheet of cryptographic consequences is maintained by A. Gupte (linked in a blog comment; not opened).
  - Lead-scout inference: a key-recovery circuit with k key bits and s ≫ k·√log k gates gains nothing. Fine-grained
    cryptography resting on OV is untouched because OV stands.
- **ETH-conditional lower bounds (hundreds of papers).** These lose their stated basis but are not refuted.
  - [MITHG26]: most survive under SH with an arbitrarily small constant loss in the exponent.
  - Szeider: 20 of 29 checked bounds survive verbatim under the k×k Clique hypothesis.
  - Molter: 12 bounds re-derived under FPT ≠ W[1].
  - Bounds that follow from OV or the CNF-SAT hypothesis survive as stated ([OAI26] §1.1.3 lists LCS, regex
    matching, Fréchet distance, diameter approximation, and treewidth-IS/DS).
- **Proof complexity.** No conflict with regular-resolution SETH (L7). Szeider claims 2^{o(n)} IPS refutations
  (unverified). See O3.

---

## 3. Key techniques and their barrier status

### 3.1 OpenAI: deformed clause inputs, measurements, Taylor/Hermite interpolation ([OAI26] §2–6)

1. **Reduce to bounded occurrence.** Use count-preserving sparsification with σ → 0 (Lemma 6.3: a tree with
   poly_k(n,σ⁻¹)·2^{σn} nodes; each leaf has ≤ B = O_k((σ⁻¹log(2/σ))^{k−1}) occurrences per variable, and the leaf
   counts add up to the input count). Then make variable copies with Tovey cycles.
   For the sharp bound, apply **parity tests**: expander/Tanner-code checks and greedy test selection (Lemma 6.1)
   turn each leaf into O(n) sparse F₂ equations on the original variables.
2. **Polynomial for the count.** #F = Σ_x Π_e Φ_e(x), where the total degree is ≤ 3n under bounded occurrence. For
   parity tests, use the Beigel–Tarui modulus-amplifying polynomials p_ℓ(Y) = Σ_j e_j(Y)·h(Y)^j with
   h = Y(Y−1) (Lemma 5.1). These are truncated across tests to keep the degree O(n).
3. **Deform.** Replace each occurrence of X_v in clause e by a linear form ⟨P_{e,v}(T), X⟩ with P_{e,v}(0) = δ_v and
   degree ≤ R. Then H(T) := Σ_x Π_e Φ_e(⟨P_{e,v}(T),x⟩) satisfies H(0) = #F and deg H ≤ 3nR.
4. **Easy points.** At T = t ∈ [Q] an (r,τ,D)-design holds:
   - groups of size ≤ 2n/r;
   - each clause depends on its own group plus ≤ 2τn integer "measurements" C_g x_g with ℓ₁-row-norm ≤ D.
   Enumerate the (2D+1)^{2τn} measurement tuples and multiply the group sums, at cost r·2^{2n/r} per tuple.
5. **Taylor data.** At each t, compute the coefficients up to order q = ⌊3nR/Q⌋ by inclusion–exclusion over sets
   |E| ≤ q (cost Σ_j C(n,j)2^j). Then use Hermite interpolation to recover H(0).
6. **Construction (the "alien" part).** Use auxiliary coordinates B = ([r]×[r])^Q and commuting swaps Π_s. Set
   V₀ = ΠΠ_s, W₀ = ½Σ(I−Π_s), and M₀ = V₀·f(W₀), where f(j) = (−1)^j is interpolated on R consecutive integers
   near Qp. By binomial concentration, M₀ fixes most eigenvectors; the exceptional ones become the measurement
   rows. The factors φ_{u,w}(T) = Π_{s∈E_{u,w}}(1−T/s) kill cross-group terms at the bad points.
   Parameters: r = Θ(√log n/(log log n)²), Q = Θ(log n/log log n), R = Θ(√log n), τ = Θ(1/(r log n)),
   D = r^{2Q} ≤ (2n)^{1/128}.
7. **Sharper bound (App. D).** Boolean tensor-network contraction by recursion on wires (Theorem D.1), using
   two-adic valuation tapering, which removes one log log n factor.

The paper itself links step 6 to matrix rigidity: "In [AW17, Section 3], a low-degree polynomial matches (−1)^j on
an interval of integer inner products j … low-rank matrices agreeing with Walsh–Hadamard matrices in most entries".
That is the Alman–Williams non-rigidity trick.

O'Donnell's re-formulation (E1) makes this clean. A(t) = L(I_C ⊗ J(t))R′ with
J(t) = X^{⊗ℓ} + p(Σ_j(1−t/j)X_j) − p(Σ_j X_j), where p agrees with parity outside an ℓ^{−100} fraction of the cube
and has degree O(√(ℓ log ℓ)). At t = i, A(i) is block-diagonal (blocks ≤ 3n/q) plus rank ≤ M/ℓ^{100}. The permanent
of each square submatrix is computed by the colour-count DP, derivatives come from the permanent addition formula,
and the value at 0 from Hermite interpolation.

### 3.2 Anthropic: signed crossing rewrite plus row/column merging ([Ant26] §2–6, App. A–D)

1. #k-SAT becomes a "network" sum Z = Σ_z Π_a W_a(z_a)·Π_{a,b} Ψ_{a,b}. Nodes are clauses (or groups); edges are
   equality tests on shared variables, costing c bits ("factors through c bits" means matrix rank ≤ 2^c).
2. The recursion acts on (K,λ)-cliques. Put g² nodes on a g×g grid. Each rectangle's two diagonals form a
   **crossing** [x=v][y=u], rewritten by the **eight-square (Degen–Graves) identity** on 3-bit blocks:
   2[x=v][y=u] = [x⊕y⊕u⊕v=0]·(σ(x,y)σ(v,u) + σ(x,u)σ(v,y)).
3. Group the 2^t block expansions by the number of column choices (A₀…A_t), giving (t+1)^{|R|} terms, which is
   polynomial in λ. In each term, merge rows or columns, whichever is cheaper. The costs add up to 11t against 12t,
   so the edge bits drop to ≤ 11/12 (Lemma 2).
4. Balance into K groups. The exponent recursion is e_ℓ = (ρ + 2/K)e_{ℓ−1} + 2/K with ρ = 11/12, and e_ℓ → 0.
5. Sharpening:
   - Hoeffding balancing, plus App. B "pieces" with ρ = 1/√2 (operators on a polynomial ring; Hardy–Ramanujan
     partition counts), give e = Θ(1/√log K), hence 2^{O(km/√log m)}.
   - **Theorem A(c)** turns any pieces with parameters (ρ,c) into time 2^{O(km/(log m)^{α′})}, α′ = log₂(1/ρ).
   - App. D (variable nodes; inclusion–exclusion over violated clause sets cut at ≈ n/log Δ; O(n) sparse parity
     checks) gives the n-bound with k² and log log n.

### 3.3 Common core

Both proofs evaluate a sum of products after **splitting an identity/equality/swap operator into a low-rank (or
few-measurement) part and a structured, locally separable part, with signed (cancelling) terms**. Three independent
groups say this:
- [ALPPW26] Remark 1: a "decomposition of the identity matrix";
- [JMN26]: a "decomposition of an equality indicator function";
- [VWZ26]: an "algebraic decomposition lemma … distilled … out of the recent ETH refutation".

The same core then refuted the k-Clique and hyperclique hypotheses. The algebra is old (Hurwitz sums of squares,
octonions, Hadamard non-rigidity). [Ant26] App. G says the new ingredient is "an exact signed low-rank expansion of
crossings, a separate choice of direction for each term, combined with recursion".

### 3.4 Barrier audit for these techniques

| technique / use | barrier | status and source |
|---|---|---|
| The algorithms themselves (upper bounds) | Relativization, natural proofs, algebrization, locality, GCT no-go | **Not applicable.** These barriers constrain lower-bound proofs, and the ETH refutations are algorithms. No source claims otherwise. |
| E^NP ⊄ SIZE(c·n·√log n) (F14) via Williams' method | Natural proofs [RR97] | The argument is a diagonalization against a nondeterministic time hierarchy ([Wil10] Thm 6.1 proof sketch, checked: yes). It does not obviously yield a "natural property", but **I found no source analysing this specific bound**. Folklore that the algorithmic method is non-naturalizing: checked: no. |
| same | Relativization [BGS75] | The SAT algorithm needs the circuit's gate structure, which an oracle gate breaks. Whether an oracle exists relative to which E^NP has O(n)-size circuits: **not found / not checked**. Do not assume either way. |
| same | Algebrization [AW09], locality [CHOPRS20], GCT [BIP19] | No source found that discusses them for this result. Not used by the argument (no magnification, no GCT). |
| Pushing the same methods toward 2^{n^{1−ε}} | Method-specific limits | L1 (single contraction tree ≥ ≈4/9 of brute force), L2 (rewrite-and-merge ≥ (log K)^{−3} per edge bit), L3 (clause-product interpolation 2^{Ω(√n)} on random 3-CNF). Resolution-type approaches: L7. |
| Transfer to NP-wide statements | Reduction blow-up | L4: 2^{o(n)} does not survive polynomial reductions. |
| Extension to wide clauses / dense Max-SAT | Sparsification limits | L5, L6. |

---

## 4. Open sub-problems ranked by tractability × impact

Scores: T = tractability for *this lab*, I = impact on the lab's mission. Each is 1–5. "Still open" means my
searches found no solution: arXiv up to submissions of 2026-11-19, ECCC up to TR26-336, ethdiscussion.blog through
its 12 Nov post, plus the expert blogs listed in §10.

| # | problem | T | I | T×I | why these scores | stated open in | latest progress found |
|---|---|---|---|---|---|---|---|
| O1 | **Close the machine-model and statement gaps in Lean on the lab's toolchain.** Port Anthropic's `MainResults` (Mathlib `Turing.FinTM2`, `TM2OutputsInTime`) from v4.33.1 to the lab's v4.36.0. Machine-check the word-RAM ↔ TM simulations that both labs leave as prose. Reuse the definitions in the lab's P/NP/Cook–Levin formalization. Adopt Toledo's existing bridge rather than redoing it. | 4 | 3 | 12 | Engineering against compiled artifacts. Directly serves mission item 4. Does not attack P vs NP itself. | [Ant26] App. E: "Two steps from the Lean statements to the printed ones are not part of the Lean proof". Toledo: "cross-model simulation steps B1, B1′, B2 and B2′ … are prose" | Toledo, 5–6 Nov 2026: ported to Lean v4.36.0-rc2 / cslib multitape TM; cslib PRs #2509/#2510 reported merged 6 Nov (PR page returned 404; unverified) |
| O2 | **Find "pieces" with ρ < 1/√2** (Anthropic Def. 7). These are decompositions of a multiple of the crossing [x=v][y=u] into poly(λ) functions with fewer row-plus-column bits. By [Ant26] Thm A(c) this gives #k-SAT in 2^{O(km/(log m)^{log₂(1/ρ)})}. By the [OAI26] Cor 1.4 argument (lead-scout inference) it gives E^NP ⊄ SIZE(c·n·(log n)^{log₂(1/ρ)}) i.o. | 3 | 3 | 9 | A small, concrete algebraic object that computer search can attack ([Ant26] App. H describes how the search found the eight-square identity). [Maj26]'s class bound (log K)^{−3} leaves room. Moves an explicit circuit lower bound. | [Ant26] App. G: Naslund's Problem 12, whether P(N) ≥ N^{1+ε}; Hrubeš's P(N) = O(N^{1.62}) is "only sketched, and we have not checked whether his construction provides such factorizations" | [Maj26], 30 Oct 2026 (explicit recursion, class lower bounds) |
| O3 | **Proof-complexity shadow.** Do unsatisfiable n-variable 3-CNFs have 2^{o(n)}-size refutations in Extended Frege, or in IPS, extracted from the counting identities? This needs the algorithms' correctness to be cheaply provable. A yes would rule out 2^{Ω(n)} lower bounds, measured in variables, for those systems. | 3 | 3 | 9 | Bridges to the lab's proof-complexity area. The IPS case is claimed (unverified). The EF case needs bounded-arithmetic work. | IPS: Szeider, Zenodo note, 16 Nov 2026 (claim). **EF: no source found stating it; novelty check required.** | Szeider, 16 Nov 2026 |
| O4 | **Red-team the claimed uniform consequence NTIME(n) ⊊ DSPACE(n)** (C. Cruz, GitHub), and work out what C1 gives for uniform separations | 4 | 2 | 8 | Checking a short argument is cheap. If correct and new it is a clean uniform separation. I could not reconstruct an argument myself. | Claim only (blog comment, 2 Nov 2026). C1 does not state it. | [SS26], 9 Nov 2026 |
| O5 | **Dense permanent / #PM below 2^{n−o(n)}.** The new methods need O(1) nonzeros per row and column. Is the 0/1 permanent of a dense n×n matrix computable in 2^{o(n)}? | 2 | 3 | 6 | It is the natural next step of E1. It would be a major counting result, but no known route exists. | O'Donnell (interview, 13 Nov 2026; transcript via WebFetch): "we only get a subexponential-time algorithm when the matrix is sparse" | [ODo26], 30 Oct 2026 |
| O6 | **CNF-SAT with unbounded width in 2^{(1−δ)n}·poly(m), or OV in N^{2−ε}·poly(d).** | 1 | 5 | 5 | It would collapse the surviving fine-grained base and, per Williams 2010 open problem 1, may give "interesting non-uniform lower bounds". No technique is known; sparsification fails (L6). | [Ant26] §1 (OV not refuted); [OAI26] §1.1.3; [Wil10] §6 item 1 | [Chu26], 4 Nov 2026 (k-OV only for constant depth) |
| O7 | **Non-trivial Circuit-SAT for n^{1+ε}-size circuits (or formulas), with the saving measured in inputs**, aimed at superlinear or superpolynomial lower bounds beyond c·n·√log n | 1 | 5 | 5 | It is the real bridge to P vs NP via Williams' method. Current costs scale with gates (§2.6). | [OAI26] App. C.1; O'Donnell interview; E. Hirsch comment on Fortnow's blog (fixed-linear-size CircuitSAT) | [WW26b], 2 Nov 2026 (bases extended, still ≈ n·√log n) |
| O8 | **Weak ETH / SH.** Is 3-SAT in 2^{n^{1−ε}} for some ε? (2^{n^{ε}} for every ε would give NP ⊆ SUBEXP.) | 1 | 4 | 4 | Blocked for the known method classes (L2, L3). Experts doubt it: per a WebFetch summary of the transcript, O'Donnell called a 2^{√n} algorithm "amazing" but said he personally does not believe it exists. | [MITHG26] (SH "remains plausible") | [MITHG26] v2, 16 Nov 2026 |
| O9 | **Sparsification lemma for Max-kSAT** | 2 | 2 | 4 | Would carry the new algorithms to dense Max-kSAT. Mostly fine-grained interest. | [ALPPW26] §1 | [ALPPW26], 3 Nov 2026 |
| O10 | **Remove the log log n factor** for dense k-CNF in the n-bound | 3 | 1 | 3 | Cosmetic for the lab. | [Ant26] §2.7: "we do not know whether the factor log log n can be removed" | [OAI26] App. D (only for m ≤ Dn) |
| O11 | **k-Clique in f(k)·n^{o(k)}?** The ETH-based lower bound's basis is gone. | 1 | 2 | 2 | Parameterized-complexity question, far from P vs NP. | Szeider's k×k Clique Hypothesis (via [MITHG26]); Lampis (via [MITHG26]) | [VWZ26], 6 Nov 2026: n^{(ω/3−c)k} |

Recommendation (lead-scout opinion, not a lab decision):
- O1 is a safe formalization-track task.
- O2 is the best "realistic-publishable" candidate that touches circuit lower bounds. It needs a novelty check
  against Majdoddin's and Hrubeš's work first.
- O3 should go to the proof-complexity scout or batch for cross-checking.
- None of O1–O11 is a credible route to P ≠ NP or P = NP on its own.

---

## 5. Known traps

1. **"Lean-checked" ≠ "the paper is right" ≠ "ETH is false in the textbook sense".**
   - [Ant26] README: "Lean checks the proofs, but no machine checks that this file says what the paper says".
   - [Ant26] App. E: "The Lean development was written by AI models and reviewed by other instances of the same
     models; at the time of writing no person is known to have checked it; its constant is not explicit." Also:
     "AI models, not a mechanical check, compared the Lean proof with the printed one".
   - OpenAI's Lean proves only F2, not the headline F1 (378.md). OpenAI's Lean files define no ETH (Toledo). Toledo
     also reports, paraphrased, that 8 of the 151 constants named by the OpenAI statement differ between the two
     Mathlib versions he used, so the two statements are not shown to be the same term.
   - Never cite F1 as Lean-verified.
2. **Assuming the speed-up transfers through NP reductions.** It does not (L4).
3. **Assuming general Circuit-SAT or CNF-SAT is now fast.** Only linear-size circuits and fixed width are covered
   (L6; O'Donnell interview, transcript via WebFetch: "if m, the number of gates, is quite close to n, this result
   does imply faster algorithms").
4. **Assuming every SETH-based lower bound is dead.** OV-based and CNF-SAT-based bounds stand (§2.5). Fortnow, in a
   reply to a blog comment (paraphrased by WebFetch), made the logical point that a false hypothesis does not make
   the statements it implied either true or false.
5. **"Weak ETH" means different things.**
   - [MITHG26] fn. 3: Lokshtanov (2017) used it for "3SAT requires 2^{Ω(n^c)} time for some c > 0"; Carmosino et
     al. used it for an MCSP hypothesis. The paper recommends "using SH".
   - Gasarch's proposal is an ∃c version.
   - Always state the quantifiers.
6. **Thinking the algorithms matter in practice.** They are galactic (L8). Fortnow: "It will never beat CDCL".
7. **Mixing up threshold numbers.**
   - [Ant26] App. A gives *necessary* conditions: log m > 8000 at density 1 and log m > 1.3·10^5 at density 5.
     §1 quotes n > 10^{10 000} at m = 5n and n > 10^{10^8} for the n-bound.
   - [Maj26] computes main-term crossovers instead: 2^{33858} reduced to ≈2^{420} clauses at density 1, and
     2^{2.2·10^{12}} reduced to ≈2^{8.6·10^9} variables for general 3-SAT.
   - Szeider gives 2^{10^{10}} and 2^{131071} for OpenAI's constructions (unverified). [DL26] gives
     log₂(n+m) > 10^9.
   - These are different quantities; report the source with every number.
8. **Pursuing 2^{n^{1−ε}} with the same machinery.** It is blocked inside the rewrite-and-merge class (L2) and the
   clause-product interpolation model (L3). A single contraction tree cannot go below ≈4/9 of brute force (L1).
9. **Resolution, DPLL or CDCL-style proof search for 2^{o(n)}.** Exponential resolution-type lower bounds exist
   (L7). The new algorithms are algebraic and signed, and that is essential: [Ant26] says its algorithm "lies outside
   the model, because it expands the sum into a signed sum of tensor networks".
10. **Secondary sources misstate details.**
    - A WebFetch rendering of the Wikipedia ETH page gave the bound as 2^{O(n(log log n)/log n)}. The primary
      sources have √log n; this may be a rendering artifact.
    - Media mix "found Oct 16" with "released Oct 26", and "counting" with "decision".
    - Use §2.1 only.
11. **OpenAI's math repository has had errors in other papers.** Its history.md (Oct 7) withdrew three Hodge-type
    manuscripts over "a sign error". The README calls the manuscripts "raw research data" and warns "Some of the
    unformalized results could have issues". The ETH paper has **no** recorded revision or withdrawal (history.md
    latest entry, Oct 29).
12. **#ETH in Anthropic's Lean is restricted.** It covers only formulas with ≥ 2 clauses, ≥ 4 variables and every
    variable occurring. ETH → #ETH is not proved in either Lean model (Toledo).

---

## 6. People and groups (names seen on the papers, posts and threads cited here)

- **Review organisers:** R. Impagliazzo, R. Paturi (UC San Diego), R. Williams (MIT), kickoff post, 26 Oct 2026.
  F. Zane posted "Links to Other Work" and "Lean Replications". "ETH Group, UC San Diego" is cited in [MITHG26].
- **Expositions:** R. O'Donnell (CMU) [ODo26]; M. Sellke (slides); S. Kintali [Kin26]; E. Porat [Por26];
  J. Nederlof (blog comment); J. Nelson (blog comment); S. Lovett, N. Lindzey (blog comments proposing a
  polymath-style effort).
- **Follow-up authors:**
  - C. Strassle, B. Subercaseaux [SS26]; R. Majdoddin [Maj26]; F. Dias, Y. Lima [DL26]; L. Kozma [Koz26];
    S. Chen, T. Jiang, Y. Zhu [CJZ26]; M. Wu, M. Wang [WW26a, WW26b].
  - MIT Hardness Group with J. Brunner, E. Demaine, F. Frei, T. Gomez, M. Hecher, J. Li, J. Lynch [MITHG26].
  - V. Vassilevska Williams, O. Zamir [VWZ26]; J. Alman, B. Li, N. Pant, K. Pratt, R. Williams [ALPPW26];
    N. Fischer [Fis26]; T. Chan, R. Itakura, Z. Ma, Y. Yu [CIMY26a, b]; A. Jabal Ameli, N. Mohrin, J. Nederlof
    [JMN26].
  - N. Chukhin [Chu26]; H. Molter [Mol26]; S. Bartlmae [Bar26]; Karthik C. S., D. Minzer [KM26].
- **Hypothesis repair:** S. Szeider (Zenodo notes), M. Lampis, P. Manurangsi (all cited in [MITHG26]).
- **Lean replication:** C. Toledo, T. Busnello, N. Jose, S. Zhuang, D. Hawkley (ethdiscussion.blog; GitHub).
- **Commentary:** L. Fortnow, W. Gasarch (Computational Complexity blog); S. Aaronson (Shtetl-Optimized).
- I found no post on the ETH refutation at Gödel's Lost Letter; its latest post seen was dated 3 May 2026.

---

## 7. Formalization status

**Anthropic** (`github.com/anthropics/formal-math`, folder `eth`, commit 16a5ce41304fcdaea4e0be7c132e1c361dc26da5;
identical to `main` on 2026-11-23). checked: yes.

Toolchain and checks:
- Lean `v4.33.1`, Mathlib `v4.33.1`. The paper names Mathlib commit 0df444a360eaa60ab8c11dca51a86af692955474.
- 1,050 modules. Build "about 8 minutes on 24 virtual CPUs", ≈7 GB.
- `#print axioms` gives `[propext, Classical.choice, Quot.sound]` for both theorems.
- CI runs Comparator (statement vs `Challenge.lean`) plus the independent kernel `nanoda`; `leanchecker` also replayed.

Statement file `MainResults.lean` (Mathlib-only, definitions only). The key definitions, verbatim:

```lean
def IsKCNF (k : ℕ) {n : ℕ} (φ : CNF n) : Prop := (∀ C ∈ φ, C.length ≤ k) ∧ φ.Nodup
def InTime (k : ℕ) (δ : ℝ≥0) : Prop :=
  ∃ (M : TM2ComputableAux Bool Bool) (c : ℕ), (∀ i, Finite (M.tm.Γ i)) ∧
    DecidesKSat k M fun n => ⌊(c : ℝ) * (2 : ℝ) ^ ((δ : ℝ) * n)⌋₊
noncomputable def s (k : ℕ) : ℝ≥0∞ := ⨅ (δ : ℝ≥0) (_ : InTime k δ), (δ : ℝ≥0∞)
def ETH : Prop := 0 < s 3
def ETHIsFalse : Prop := ¬ ETH
def MainTheorem : Prop :=
  ∃ (M : TM2ComputableAux Bool Bool) (C : ℕ), (∀ i, Finite (M.tm.Γ i)) ∧
    ∀ (k n : ℕ) (φ : CNF n), 1 ≤ k → IsKCNF k φ → 2 ≤ φ.length → 4 ≤ n → AllOccur φ →
      CountsWithin M k φ (timeMin C k φ.length n)
```

Here `CNF n = List (List (Fin n × Bool))`. Satisfiability is ∃ a, ∀ C ∈ φ, ∃ l ∈ C, a l.1 = l.2. The input is n in
unary, then k fixed-width binary slots per clause; for `MainTheorem`, 1^k 0 comes first. Output: the count in n+1
bits, LSB first.

Paper ↔ Lean differences, as listed by the authors in App. E:
- the constant is named but not given;
- explicit ranges k ≥ 1, m ≥ 2, n ≥ 4;
- word-RAM time in the paper vs FinTM2 steps in Lean;
- clauses are lists in Lean (may be empty, repeat literals, or differ only by order) vs sets in the paper;
- the RAM ↔ TM simulation and the input-rewriting step are **not** formalized.

**OpenAI** (`github.com/openai/math`, `lean/`, toolchain `leanprover/lean4:v4.34.1`; challenge file
`lean/ComparatorChallenges/SubexponentialSAT.lean`). checked: yes (statement file and toolchain; not built).
- The theorem `exact_count_and_sat` is stated over a custom `PrimitiveMachine`: a multitape TM built from Mathlib's
  `Turing.Tape` and `Turing.TM0.Stmt`, with one head action per step.
- CNF = `Finset (Finset (Literal V))`. The encoding is unary (`encodeNat n = replicate n true ++ [false]`).
- Time bound: `C * (L+1)^d * 2^(A * n * (log (log (n+16)))^2 / sqrt (log (n+16)))` with natural log, plus a
  polynomial visited-space bound.
- The machine depends on k (∃ machine for each k ≥ 2).
- It proves the weaker F2 bound, not F1, as OpenAI's 378.md says.
- OpenAI's shipped Comparator config disables nanoda (N. Jose; C. Toledo). Busnello reports that the 19
  axiom-printing declarations use only the standard three axioms. Neither the config file nor the axiom output was
  opened by me (checked: no).

**Independent replications and bridges.** All from blog comments and personal pages; secondary; checked: no unless
marked.
- T. Busnello (31 Oct): both developments re-run under Comparator/landrun. OpenAI took 3 h 47 min; Anthropic took
  42 min including nanoda. Only standard axioms.
- N. Jose (5 Nov): both suites pass on macOS. A stock nanoda run on OpenAI's development overflowed the stack, so
  its result is unknown.
- C. Toledo (28 Oct – 6 Nov; carlostoledo.co/eth, WebFetch-read):
  - Both developments "CERTIFIED" under Comparator, nanoda and `leanchecker --fresh`.
  - 51 bridge theorems, including `not_eth_of_claim` (OpenAI) and `not_eth_of_ethIsFalse` (Anthropic), against a
    textbook-style ETH (s_k > 0 ∀k ≥ 3).
  - Anthropic's statement ported to Lean v4.36.0-rc2. It implies ETH is false on **cslib's** multitape TM with
    binary encoding, time c·2^{δn}·(L+1)^e + c. A word-RAM version is in "complexitylib".
  - Still prose: whether the multitape statement *is* textbook ETH ("a reading"); the cross-model simulation
    steps.
- D. Hawkley (formalize.now/378): a kernel-checked `¬PositiveRateETH → MainResults.ETHIsFalse` (Lean 4.34.1).
- S. Zhuang: NotETHSimplified (E6).

**Relevance to the lab** (CLAUDE.md, mission item 4):
- Mathlib still has no P/NP classes (LOG.md, Stage 0). However, `Turing.TM2ComputableAux`, `TM2OutputsInTime` and
  `FinTM2` have now been used at scale for a time-bounded complexity statement with explicit step counts, including
  composition and alternation of machines.
- The lab should **reuse this vocabulary** for P/NP and Cook–Levin, and check cslib (multitape TMs, ETH definitions)
  before writing its own.
- The lab pins v4.36.0; Anthropic pins v4.33.1; Toledo reports a v4.36.0-rc2 port.
- Comparator plus an independent kernel (nanoda, lean4lean) is a stronger check than `#print axioms` alone. Consider
  adding it to `scripts/lean_audit.sh` (lead's decision).

---

## 8. Known-results registry entries (for research/KNOWN_RESULTS.md)

- [eth-refutation] Deterministic #k-SAT (fixed k ≥ 2) in (n+m)^{O_k(1)}·2^{O_k(n log log n/√log n)} time and poly space; 2^{O_{k,D}(n/√log n)} when m ≤ Dn; claimed, not peer reviewed — OpenAI (2026), "The Exponential Time Hypothesis is False", github.com/openai/math preprint (rev. 25 Oct 2026), Thm 1.1 — checked:yes
- [eth-refutation] Weaker interpolation version 2^{O_k(n(log log n)²/√log n)} is Lean-checked by OpenAI (custom multitape TM, Lean v4.34.1, `exact_count_and_sat`) — OpenAI (2026), lean/docs/378.md — checked:yes
- [eth-refutation] One deterministic algorithm uniform in k counts k-CNF solutions in 2^{O(min{k²n log log n/√log n, km/√log m})} (word RAM); Lean-checked on Mathlib FinTM2 with standard axioms + nanoda; claimed, not peer reviewed — Claude/Anthropic (2026), "A 2^{o(n)} Time Algorithm for 3-SAT", github.com/anthropics/formal-math/eth — checked:yes
- [eth-refutation] Decision 3-SAT in 2^{O(n/(log n)^{1/20})} (no log log factor) — Claude/Anthropic (2026), Thm A(d) — checked:yes
- [eth-refutation] Any "pieces" for the crossing with parameters (ρ,c) give #k-SAT in 2^{O(km/(log m)^{log₂(1/ρ)})}; known ρ = 11/12 (eight-square identity) and ρ = 1/√2 (App. B) — Claude/Anthropic (2026), Thm A, Thm B — checked:yes
- [eth-refutation] Boolean tensor networks (≤ Cs edges, degree ≤ s^{9/10}) contract in (s+L)^{O(1)}·2^{O(s/√log s)} — OpenAI (2026), Thm D.1 — checked:yes
- [eth-refutation] ETH, SETH, NSETH, #ETH, Gap-ETH (and randomized ETH/SETH/Gap-ETH) are false if the above are correct; OV hypothesis and unbounded-width CNF-SAT hypothesis are NOT refuted — OpenAI (2026) §1.1; Anthropic (2026) Cor 5–6, §1 — checked:yes
- [eth-refutation] Sparse permanent (O(1) nonzeros per row/col) exactly and deterministically in 2^{O(n(log log n)²/√log n)}, poly space; randomized #3SAT for arbitrary 3-CNF in 2^{O(n(log log n)³/√log n)} — O'Donnell (2026), exposition of [OAI26] (30 Oct 2026) — checked:yes
- [circuit-lb] If ETH is false then E^NP does not have linear-size circuits — Williams (2010), STOC 2010 / SICOMP 2013, Thm 6.1 — checked:yes
- [circuit-lb] ∃ L ∈ E^NP, c > 0: L needs > c·n·√log n fan-in-2 gates for infinitely many n (conditional on [OAI26] Thm 1.1 sparse bound) — OpenAI (2026), Cor 1.4 — checked:yes
- [circuit-lb] E^NP language needing Ω(m√log m/log log m) gates over unbounded AND/OR + binary XOR i.o.; bounded basis with linear budget of XOR/symmetric gates needs Ω(m√log m) i.o. — Wu, Wang (2026), arXiv:2611.02560 — checked:yes (abstract)
- [circuit-lb] Prior best explicit lower bound for E^NP over the full binary basis was 3.1n − o(n); S₂E needs near-maximum circuits — Li–Yang (2022); Chen–Hirahara–Ren (2024); Li (2024), as stated in Anthropic (2026) §1.2 — checked:no
- [uniform] NTIME[t] ⊆ DTIME[2^{O(t log log t/√log t)}] from the published algorithms; NTIME[t] ⊆ DTIME[2^{O(t/√log t)}] from the proofs (multitape TMs) — Strassle, Subercaseaux (2026), arXiv:2611.11832 — checked:yes (abstract)
- [fine-grained] SH (Stearns–Hunt 1990) ⇔ Weak ETH (∀ε, 3SAT ∉ O(2^{n^{1−ε}})) ⇔ fixed-width versions; #SH ⇔ Weak #ETH; SH-based reduction framework — MIT Hardness Group et al. (2026), arXiv:2611.02650 — checked:yes
- [fine-grained] Sparse Max-3-SAT hypothesis refuted; Anthropic recursion counts assignments satisfying exactly j clauses in 2^{O(m/√log m)}; crossover ≈2^{420} clauses at density 1 — Majdoddin (2026), arXiv:2610.41622 — checked:yes (abstract)
- [fine-grained] k-Clique in n^{(ω/3−c)k} (refutes k-Clique hypothesis), using a decomposition lemma distilled from [OAI26] — Vassilevska Williams, Zamir (2026), arXiv:2611.09764 — checked:yes (abstract)
- [fine-grained] k-hyperclique counting in O(n^{k−ε_k}); Max-kSAT in 2^{(1−ε)n}poly; k-AP in n^{2−ε} — Alman, Li, Pant, Pratt, Williams (2026), arXiv:2611.05082 — checked:yes (abstract)
- [fine-grained] Hyperclique and k-AP hypotheses false: O(n^{(1−ε_h)k}) — Fischer (2026), arXiv:2611.03880 — checked:yes (abstract)
- [fine-grained] Truly subquartic 4-hyperclique in 3-uniform hypergraphs — Chan, Itakura, Ma, Yu (2026), arXiv:2611.06813 — checked:yes (abstract)
- [fine-grained] 3SUM in O(n^{1.9992}), APSP in O(n^{2.9995}) (Anthropic), refuting 3SUM/APSP/Exact-Triangle hypotheses — Alman, Vassilevska Williams (2026), arXiv:2610.06783 — checked:yes (abstract)
- [fine-grained] k-SUM hypothesis refuted for odd k (randomized O(n^{⌈k/2⌉−ε_k})) — Chan, Itakura, Ma, Yu (2026), arXiv:2610.42012 — checked:yes (abstract)
- [fine-grained] Counting 6-cliques in O(n^{5.97}) time, O(log n) space; Max Cut in O(1.994^n) poly space — Jabal Ameli, Mohrin, Nederlof (2026), arXiv:2611.24750 — checked:yes (abstract)
- [fine-grained] #3SAT in 2^{O(n/f(n))} ⇒ #PPM in 2^{O(n√(log f/f))}; #PPM subexponential — Kozma (2026), arXiv:2610.41048 — checked:yes (abstract)
- [fine-grained] Exact-One Hitting Set counting in 2^{O(r log log r/√log r)}·poly(L) — Chen, Jiang, Zhu (2026), arXiv:2611.00994 — checked:yes (abstract)
- [method-limits] Rewrite-and-merge class: exponent ≥ (log₂K)^{−3} per edge bit (two balanced homogeneous merges), excluding 2^{n^{1−c}}; no grid algorithm in the class gains below ≈2^{6000} variables — Majdoddin (2026), arXiv:2610.41622 — checked:yes (abstract)
- [method-limits] Clause-product interpolation (OpenAI body scheme) costs 2^{Ω(√tw)}, 2^{Ω(√n)} on random 3-CNF above density 3, 2^{Ω(n^{1/3})} on path formulas in a matching cost model; OpenAI's general bound beats 2^n only for n ≳ 10^{32} (C=2) — Dias, Lima (2026), arXiv:2611.00517 — checked:yes (abstract)
- [method-limits] Single-contraction-tree tensor networks cannot go below ≈4/9 of brute force on Anthropic's recursed problem — Anthropic (2026) App. G via Austrin–Kaski–Kubjas (2022) — checked:yes ([Ant26]); AKK22 checked:no
- [method-limits] No sparsification lemma is known for Max-kSAT for any k — Alman et al. (2026), arXiv:2611.05082 §1 — checked:yes
- [circuit-lb-restricted] k-OV conjecture holds for constant-depth circuits in polylog dimension; depth-3 2-OV needs Ω(n²) wires — Chukhin (2026), arXiv:2611.06231 — checked:yes (abstract)
- [parameterized] Twelve historically-ETH-based running-time lower bounds recovered under FPT ≠ W[1] — Molter (2026), arXiv:2611.26080 — checked:yes (abstract)
- [formalization] ¬ETH stated and checked on Mathlib `Turing.FinTM2` (Lean 4.33.1) with `TM2OutputsInTime` time model — Anthropic (2026), formal-math/eth/MainResults.lean — checked:yes
- [formalization] Bridges from both labs' statements to a textbook-style ¬ETH on cslib multitape TMs (Lean v4.36.0-rc2), 51 theorems, multiple kernels — Toledo (2026), carlostoledo.co/eth — checked:no (secondary page, not built)
- [context] Williams' 2019 estimates: ETH 70%, SETH 25%, NSETH 15% — Williams (2019), "Some Estimated Likelihoods for Computational Complexity" — checked:yes
- [prior-baseline] Pre-Oct-2026 3-SAT records: deterministic O(1.32793^n) (Liu 2018); randomized O(1.308^n) (Hertli 2014), O*(1.307031578^n) (Jiang–Cai, arXiv:2607.10697, 2026). #3-SAT: O*(1.637^n) (Kutzkov, IJCAI 2026) per [OAI26] vs O(1.6423^n) (Kutzkov 2007) per [Ant26]. #k-SAT 2^{n−Ω(n/k)} (Impagliazzo–Matthews–Paturi 2012; Chan–Williams) — as cited in [OAI26] §1.1 and [Ant26] §1.2 — checked:no

---

## 9. Bibliography (for research/BIB.md)

Primary claims and artifacts:
- `OAI26` — OpenAI. "The Exponential Time Hypothesis is False." Preprint dated 17 Oct 2026, revised 25 Oct 2026, released 26 Oct 2026, 67 pp. https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf. Lean: https://github.com/openai/math/blob/main/lean/docs/378.md and lean/ComparatorChallenges/SubexponentialSAT.lean — checked: yes
- `Ant26` — Claude (Anthropic). "A 2^{o(n)} Time Algorithm for 3-SAT." 26 Oct 2026. https://github.com/anthropics/formal-math/tree/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth (paper.pdf, MainResults.lean, Challenge.lean, proof/PaperIndex.lean) — checked: yes
- `OAI26blog` — OpenAI. "Building scientific understanding with academic communities." 26 Oct 2026. https://openai.com/index/building-scientific-understanding-with-academic-communities/ — checked: yes (WebFetch)
- `IPW26` — R. Impagliazzo, R. Paturi, R. Williams. "ETH Refutation: Examination and Discussion." ethdiscussion.blog, 26 Oct 2026. https://ethdiscussion.blog/2026/10/26/eth-refutation-examination-and-discussion/ — checked: yes (WebFetch)
- `ETHblog` — ethdiscussion.blog posts: "Links To Other Work" (Zane, 29 Oct), "Lean Replications" (Zane, 30 Oct), "New Results Related to ETH" (Paturi, 1 Nov), "OpenAI prompt that led to the ETH refutation" (Paturi, 12 Nov), and background page ?page_id=119 — checked: yes (WebFetch)

Expositions and commentary:
- `ODo26` — R. O'Donnell. "Some exposition of 'The Exponential Time Hypothesis Is False'." 30 Oct 2026. https://www.cs.cmu.edu/~odonnell/some_eth_false_exposition.pdf — checked: yes
- `Kin26` — S. Kintali. "A simplified proof of ETH is false." 26 Oct 2026. https://shivakintali.github.io/papers/ETH.pdf — checked: yes
- `Sel26` — M. Sellke. "An Outline of OpenAI's Algorithm for k-SAT in 2^{o(n)} Time" (slides). 28 Oct 2026. https://msellke.com/Files/ETH-False-Slides.pdf — checked: yes (title only)
- `Por26` — E. Porat. "Digesting the Subexponential Algorithm for #k-SAT." Draft 12 Nov 2026. https://eitanporat.github.io/papers/ksat.pdf — checked: yes (abstract/intro)
- `Roz26` — V. Rozhoň. "Ryan O'Donnell on the Exponential Time Hypothesis." Substack, 13 Nov 2026. https://vasekrozhon.substack.com/p/ryan-odonnell-on-the-exponential — checked: yes (WebFetch)
- `For26` — L. Fortnow. "The Exponential Time Refutation." Computational Complexity blog, 28 Oct 2026. https://blog.computationalcomplexity.org/2026/10/the-exponential-time-refutation.html — checked: yes (WebFetch)
- `Gas26` — W. Gasarch. "3SUM and APSP and ETH, Oh My!" 1 Nov 2026. https://blog.computationalcomplexity.org/2026/11/3sum-and-apsp-and-eth-oh-my.html — checked: yes (WebFetch)
- `Aar26` — S. Aaronson. "Podcasts about the Topic: Part II" (with comments). Shtetl-Optimized, 26 Oct 2026. https://scottaaronson.blog/?p=10239 — checked: yes (WebFetch, first 100k chars)
- `Tol26` — C. Toledo. ETH Lean replication and bridge records. https://carlostoledo.co/eth/ (Nov 2026) — checked: yes (WebFetch; not built)
- `Zhu26` — S. Zhuang. NotETHSimplified. https://github.com/suquark/NotETHSimplified — checked: yes (README)
- `HN26` — D. Saunders. "OpenAI and Anthropic Claim AI Has Disproved a 27-Year-Old Computer Science Hypothesis." HackerNoon, 4 Nov 2026 (status as of 29 Oct). Secondary. https://hackernoon.com/openai-and-anthropic-claim-ai-has-disproved-a-27-year-old-computer-science-hypothesis — checked: yes (secondary)

Follow-ups (arXiv, Oct–Nov 2026):
- `SS26` — C. Strassle, B. Subercaseaux. "Simulating Nondeterministic Turing Machines in Subexponential Deterministic Time." arXiv:2611.11832 — checked: yes (abstract)
- `Maj26` — R. Majdoddin. "Lowered crossover points of Anthropic's subexponential 3-SAT algorithm." arXiv:2610.41622 — checked: yes (abstract)
- `DL26` — F. Dias, Y. Lima. "Limits and Constants of OpenAI's Claimed ETH Refutation." arXiv:2611.00517 — checked: yes (abstract)
- `Koz26` — L. Kozma. "Faster #PPM from faster #3SAT." arXiv:2610.41048 — checked: yes (abstract)
- `CJZ26` — S. Chen, T. Jiang, Y. Zhu. "Subexponential-Time Exact-One Hitting Set." arXiv:2611.00994 — checked: yes (abstract)
- `WW26a` — M. Wu, M. Wang. "Counting Feedback Vertex Sets of All Sizes in Subexponential Time, Conditionally." arXiv:2611.02548 — checked: yes (abstract)
- `WW26b` — M. Wu, M. Wang. "Circuit Lower Bounds for Extended Gate Bases from Subexponential Counting." arXiv:2611.02560 — checked: yes (abstract)
- `MITHG26` — MIT Hardness Group, J. Brunner, E. D. Demaine, F. Frei, T. Gomez, M. Hecher, J. Li, J. Lynch. "ETH is Dead, Long Live SH." arXiv:2611.02650v2 — checked: yes
- `VWZ26` — V. Vassilevska Williams, O. Zamir. "The k-Clique hypothesis is dead, for good." arXiv:2611.09764 — checked: yes (abstract, intro)
- `ALPPW26` — J. Alman, B. Li, N. Pant, K. Pratt, R. Williams. "Finding Hypercliques Faster Than Brute Force." arXiv:2611.05082 — checked: yes (abstract, intro)
- `Fis26` — N. Fischer. "The Hyperclique Hypothesis is False." arXiv:2611.03880 — checked: yes (abstract)
- `CIMY26a` — T. M. Chan, R. Itakura, Z. Ma, Y. Yu. "The 3-Uniform Hyperclique Hypothesis is False." arXiv:2611.06813 — checked: yes (abstract)
- `CIMY26b` — T. M. Chan, R. Itakura, Z. Ma, Y. Yu. "3SUM Made Simpler (Without Matrix Multiplication), k-SUM Hypothesis Refuted for Odd k, and Real 3SUM/APSP Derandomized." arXiv:2610.42012 — checked: yes (abstract)
- `AVW26` — J. Alman, V. Vassilevska Williams. "Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs." arXiv:2610.06783 — checked: yes (abstract)
- `JMN26` — A. Jabal Ameli, N. Mohrin, J. Nederlof. "Counting 6-Cliques in O(n^{5.97}) time and O(log n) space." arXiv:2611.24750 — checked: yes (abstract)
- `Chu26` — N. Chukhin. "Exhaustive Search Is Hard to Beat in Constant Depth for Hyperclique and Orthogonal Vectors." arXiv:2611.06231 — checked: yes (abstract)
- `Mol26` — H. Molter. "Running-Time Lower Bounds under FPT ≠ W[1]." arXiv:2611.26080 — checked: yes (abstract)
- `Bar26` — S. Bartlmae. "Inapproximability of Euclidean Steiner Tree." arXiv:2611.24611 — checked: yes (abstract)
- `KM26` — Karthik C. S., D. Minzer. "Almost Optimal Lower Bounds under Almost ETH for Approximating Euclidean k-means." arXiv:2611.14892 — checked: yes (abstract)
- `Pas26` — R. Pass. "Matrix Multiplication from Polynomial Packings: A Constructive and Elementary Proof of ω ≤ 9/4." arXiv:2610.28627 — checked: yes (abstract)
- `DLSW26` — M. L. Doğan, V. Lysikov, K. Sakabe, M. Walter. "Tensor value and the 9/4 bound for matrix multiplication." arXiv:2611.09716 — checked: yes (abstract)

Classical (cited; most not opened by me):
- `Wil10` — R. Williams. "Improving Exhaustive Search Implies Superpolynomial Lower Bounds." STOC 2010; SIAM J. Comput. 42(3):1218–1244, 2013. https://people.csail.mit.edu/rrw/improved-algs-lbs2.pdf — checked: yes (Thm 6.1)
- `Wil19` — R. Williams. "Some Estimated Likelihoods for Computational Complexity." LNCS volume (2019). https://people.csail.mit.edu/rrw/likelihoods.pdf — checked: yes
- `IP01` — R. Impagliazzo, R. Paturi. "On the Complexity of k-SAT." JCSS 62(2):367–375, 2001. doi:10.1006/jcss.2000.1727 — checked: no
- `IPZ01` — R. Impagliazzo, R. Paturi, F. Zane. "Which Problems Have Strongly Exponential Complexity?" JCSS 63(4):512–530, 2001. doi:10.1006/jcss.2001.1774 — checked: no
- `CIP06` — C. Calabro, R. Impagliazzo, R. Paturi. "A Duality between Clause Width and Clause Density for SAT." CCC 2006 — checked: no
- `DHMTW14` — H. Dell, T. Husfeldt, D. Marx, N. Taslaman, M. Wahlén. "Exponential Time Complexity of the Permanent and the Tutte Polynomial." ACM TALG 10(4), 2014. arXiv:1206.1775 — checked: no
- `CGIMPS16` — M. Carmosino, J. Gao, R. Impagliazzo, I. Mihajlin, R. Paturi, S. Schneider. "Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility." ITCS 2016 — checked: no
- `Wil16` — R. Williams. "Strong ETH Breaks With Merlin and Arthur." CCC 2016, LIPIcs 50 — checked: no
- `JMV15` — H. Jahanjou, E. Miles, E. Viola. "Local Reductions." ICALP 2015. arXiv:1311.3171 — checked: no
- `LY22` — J. Li, T. Yang. "3.1n − o(n) Circuit Lower Bounds for Explicit Functions." STOC 2022 — checked: no
- `CHR24` — L. Chen, S. Hirahara, H. Ren. "Symmetric Exponential Time Requires Near-Maximum Circuit Size." STOC 2024. arXiv:2309.12912 — checked: no
- `Li24` — Z. Li. "Symmetric Exponential Time Requires Near-Maximum Circuit Size: Simplified, Truly Uniform." STOC 2024. arXiv:2310.17762 — checked: no
- `AKK22` — P. Austrin, P. Kaski, K. Kubjas. "Tensor Network Complexity of Multilinear Maps." Theory of Computing 18(16), 2022. arXiv:1712.09630 — checked: no
- `HWY11` — P. Hrubeš, A. Wigderson, A. Yehudayoff. "Non-commutative circuits and the sum-of-squares problem." JAMS 24(3), 2011 — checked: no
- `Hru24` — P. Hrubeš. "A subquadratic upper bound on sum-of-squares composition formulas." CCC 2024 — checked: no
- `Nas20` — E. Naslund. "The partition rank of a tensor and k-right corners in F_q^n." JCTA 174, 2020 (Problem 12) — checked: no
- `AW17` — J. Alman, R. Williams. "Probabilistic Rank and Matrix Rigidity." STOC 2017 — checked: no
- `SH90` — R. E. Stearns, H. B. Hunt III. "Power indices and easier hard problems." Math. Systems Theory 23(4), 1990 — checked: no
- `BI13` — C. Beck, R. Impagliazzo. "Strong ETH Holds for Regular Resolution." STOC 2013 — checked: no

---

## 10. Search log

Everything was accessed on 2026-11-23.

**Opened (primary):**
- OpenAI paper PDF (raw.githubusercontent.com/openai/math/main/preprints/...October-25-2026/paper.pdf; pdftotext,
  67 pp.).
- OpenAI files: `lean/docs/378.md`, `lean/ComparatorChallenges/SubexponentialSAT.lean`, `lean/lean-toolchain`,
  `history.md`, `CONTENTS.md` (entry 378).
- Anthropic files at commit 16a5ce4: README.md, paper.pdf (pdftotext; pp. 2–3 rendered as images to read
  exponents), MainResults.lean, Challenge.lean, comparator.json, lean-toolchain, proof/PaperIndex.lean (downloaded,
  not read). All are byte-identical to `main`. Also the formal-math root README.
- O'Donnell, Kintali and Porat PDFs; Sellke slides (title only).
- Williams improved-algs-lbs2.pdf (Thm 6.1) and likelihoods.pdf.
- MIT Hardness Group paper PDF (intro). VW–Z and Alman et al. PDFs (grep for ETH links).
- The arXiv abstracts listed in §9.

**Queries:**
- arXiv API (export.arxiv.org, sorted by date, filtered to ≥ 2026-10-01 or ≥ 2026-10-16):
  - `all:"exponential time hypothesis"`, `abs:ETH`, `abs:"exponential time hypothesis"`, `abs:ETH AND abs:refut*`;
  - `abs:SETH`, `all:subexponential AND all:SAT`, `abs:ETH AND abs:OpenAI`, `abs:Anthropic AND abs:SAT`;
  - `abs:"Weak ETH"`, `abs:"Satisfiability Hypothesis"`, `abs:hyperclique`, `abs:"k-Clique"`, `abs:"eight-square"`;
  - `abs:"tensor contraction"`, `abs:"tensor network" AND abs:satisfiability`, `abs:NTIME AND abs:DTIME`,
    `abs:permanent AND abs:subexponential`;
  - `abs:"satisfying assignments"`, `abs:"k-SAT"`, `abs:"3-SAT"`, `abs:"CNF-SAT"`, `abs:"Circuit-SAT"`,
    `abs:sparsification`, `abs:"Orthogonal Vectors"`;
  - `abs:"elliptic curve" AND abs:subexponential`, `abs:"discrete logarithm" AND abs:ETH`;
  - `au:Chukhin`, `au:Gheorghiu AND au:Gupte`;
  - id_list fetches for all arXiv ids in §9.
- WebSearch:
  - "Exponential Time Hypothesis is False"; "Shtetl-Optimized Aaronson Exponential Time Hypothesis …";
    "computationalcomplexity.org Fortnow ETH false …";
  - "ETH refutation OpenAI Anthropic proof error OR flaw OR gap OR erratum …" (extended mode);
  - "eprint.iacr.org 2026 subexponential exponential time hypothesis … elliptic curve";
    "Ruhr University Bochum Max Planck … elliptic curve … ETH";
  - "Impagliazzo Paturi Williams ETH refutation review status November 2026";
  - "Williams 'Improving Exhaustive Search Implies Superpolynomial Lower Bounds' pdf".
- WebFetch:
  - hackernoon article; en.wikipedia.org/wiki/Exponential_time_hypothesis; openai.com announcement;
  - ethdiscussion.blog (home, five posts, background page); github.com/anthropics/formal-math tree;
    github.com/openai/math (README, preprints listing);
  - blog.computationalcomplexity.org (home and three posts); scottaaronson.blog (home, ?p=10283, ?p=10239);
  - rjlipton.com; vasekrozhon.substack.com post; carlostoledo.co/eth; github.com/suquark/NotETHSimplified;
  - eccc.weizmann.ac.il/year/2026 (TR26-297…336 scanned: no ETH-specific report).

**Could not open or did not open:**
- github.com/leanprover/cslib/pull/2509 (HTTP 404), so the cslib PRs are unverified. `gh api` access to openai/math
  was blocked for this session; I used raw.githubusercontent.com instead.
- The Oct 29 Ruhr-Bochum/MPI-SP elliptic-curve preprint mentioned by HackerNoon: not found.
- Not opened (secondary or private hosting): WIRED, TechCrunch, The Verge, New Scientist, Business Insider,
  Washington Times, Gizmodo and Economic Times stories; Google Drive notes (Chukhin; Gheorghiu–Gupte; Y. Tal);
  Zenodo notes (Szeider); the claude.ai artifact (Straub); formalize.now/378 (Hawkley); A. Gupte's spreadsheet;
  O'Donnell's YouTube lectures; J. Nelson's and J. Nederlof's expositions.
- Not opened (papers): OpenAI's "Unique Games Theorem" preprint; Manurangsi's Almost-ETH arXiv v3.
- Original classical papers in §9 marked checked: no.
- Remaining 15k characters of the Aaronson comment thread.
- Gödel's Lost Letter: no relevant post (latest seen 3 May 2026).

**Seen, out of scope, flag to the lead for other scouts:**
- ECCC TR26-323 "NL = UL" (W. Hoza, 20 Nov 2026).
- ECCC TR26-328 "The Ultimate Karp–Lipton Collapse" (E. Hirsch, I. Volkovich, 7 Nov 2026).
- ECCC TR26-313 / arXiv:2611.07972: Chukhin–Gajulapalli–Golovnev–Mihajlin, "either NE needs 2^n/(2n) circuits or
  VP⁰_Z ≠ VNP⁰_Z" (unconditional win-win).
- arXiv:2611.16814 (Cui, Liu, Yu): improved deterministic k-SAT (title only).
- arXiv:2611.10139: Gamarnik's exposition of OpenAI's random k-SAT threshold result.
