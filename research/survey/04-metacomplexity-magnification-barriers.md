# Survey 04: Meta-complexity, hardness magnification, and the barriers

- Author: lit-scout (area 04), 2026-11-23. Single agent, no sub-agents.
- Scope: (a) MCSP and its variants, time-bounded Kolmogorov complexity, Hirahara's non-black-box worst-case to
  average-case reductions, one-way functions (OWFs) versus Kolmogorov complexity, NP-hardness of learning;
  (b) hardness magnification and the locality barrier; (c) exact statements of the barriers (relativization, natural
  proofs, algebrization, locality, GCT no-go, and 2015–2026 barriers), and which known results evade each, and why;
  (d) failed attempts at P vs NP and recurring error patterns; (e) a checklist for red-teamers and the barrier-auditor.
- **Conventions.** `checked: yes` means I opened the primary paper, its ECCC/arXiv abstract page, or its PDF on
  2026-11-23, and the statement matches. `checked: no` means I did not. The row then names the secondary source I
  did open, or says "memory". **[PREPRINT]** marks work not yet peer-reviewed, mostly ECCC/arXiv postings from
  2025–2026. **[AI]** marks work whose authors disclose AI generation. Lab inferences carry a CLAUDE.md status label,
  usually `informal-argument`, and are not known results.
- **Cross-references, not repeated here.**
  - `survey/02-circuit-lower-bounds.md` §2.10 (H1–H8) already lists the main magnification theorems, and its
    crosscheck adds Chen–Hu–Ren and Loff–Sherif–Talebanfard–Ugazio. I re-opened those sources. All of 02's
    magnification rows match, and I add their exact parameters, the gap-to-known-bounds table (§2.7) and the
    locality details.
  - `survey/01-eth-refutation.md` §2.4 covers the limits of the Oct-2026 ETH-refuting technique; §2.9 below only
    points to it.
  - KNOWN_RESULTS.md already has OS18, OPS19, MMW19, CJW19, CJW20 (formulas), CLY22, CHOPRS, Atserias–Müller,
    Raz 2026 and Miles–Viola. §8 proposes only new or corrected entries.
- **Recency warning.** In 2025–2026 most of this area's output went to ECCC, not arXiv: the ECCC 2026 listing has about 335 reports, numbered up
  to TR26-336, against 215 in all of 2025. I searched ECCC 2023–2026 title by title and the arXiv cs.CC listings for
  Sep–Nov 2026 (§10). I found no 2026 claim of NP-hardness of MCSP or MINKT, of a magnification threshold being
  crossed, or of a P vs NP resolution that survived scrutiny.

---

## 1. Plain-language summary

"Meta-complexity" asks how hard it is to compute complexity itself, for example whether a given truth table has a
small circuit (the Minimum Circuit Size Problem, MCSP) or whether a string has a short, fast program (time-bounded
Kolmogorov complexity). Since 2018 these problems have become hubs: their average-case hardness is exactly equivalent
to the existence of one-way functions, the basis of cryptography (Liu–Pass 2020 and follow-ups), and Hirahara linked
their worst-case and average-case hardness by "non-black-box" arguments that slip past older impossibility results.
Whether MCSP is NP-hard is still open in Nov 2026; what is known is NP-hardness of variants (partial functions,
multi-output functions, constant-depth formulas) and of a gap version of MCSP under quasi-polynomial-time reductions
and strong assumptions (Hirahara–Ilango, FOCS 2025). "Hardness magnification" shows that tiny-looking lower bounds would
give huge separations: if a gap version of MCSP needs circuits even slightly larger than linear, NP problems cannot be
solved by polynomial-size circuits, and if certain sparse NP problems need more than 2n + O(n/log log n) gates, NP has
no fixed-polynomial-size circuits. Known lower bounds sit just below these thresholds, and the "locality barrier"
(2020) explains why: the known techniques also work against circuits with small "oracle" gates, which the magnified
problems provably have. The classical barriers (relativization 1975, natural proofs 1994/97, algebrization 2008) have
exact formal statements, collected in §2.8 with the newer barriers up to 2026. Williams' ACC0 lower bound is the
standard example of evading all three, by combining a satisfiability algorithm that exploits circuit structure with
diagonalization. The most tractable openings for this lab are formalization gaps (we found no machine-checked
algebrization barrier anywhere) and concrete questions about the new 2026 barriers. The headline questions show no
sign of yielding to known methods. Many claimed P vs NP proofs, including 2026 "Lean-verified" ones that rest on
axioms, fail in the same recurring ways (§5A), and §5B turns these into a checklist.

---

## 2. Frontier table

Notation:
- N = 2^n is the truth-table length; MCSP[s] asks whether the function has circuits of size ≤ s(n).
- Gap-MCSP[s1, s2] distinguishes complexity ≤ s1 from complexity > s2.
- K^t is t-time-bounded Kolmogorov complexity, Kt is Levin's, KT is the Allender et al. measure, and pK^t and rK^t are
  the probabilistic and randomized variants.
- MINKT and MKtP are the corresponding decision problems; MCSP* is MCSP for partial truth tables over {0,1,*}.
- "i.o." means infinitely often.

### 2.1 NP-hardness of meta-complexity problems (positive results)

| # | Problem / model | Best known hardness (precise) | Reference | checked |
|---|---|---|---|---|
| M1 | **MCSP itself** (total functions, general fan-in-2 circuits) | **No unconditional NP-hardness known.** Best conditional result: a constant-factor-gap GapMCSP is NP-hard under deterministic quasi-polynomial-time (non-adaptive) Turing reductions, assuming (1) sub-exponentially secure NIWIs for SAT; (2) coNP needs sub-exponential-size nondeterministic circuits a.e.; (3) P^NP/poly needs circuits of size δ·2^n/n a.e. The reduction is non-Levin, which avoids the Mazor–Pass barrier (N5). Open questions stated there: fewer or no assumptions, polynomial time, many-one | S. Hirahara, R. Ilango, "NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions", FOCS 2025, pp. 1648–1664, doi 10.1109/FOCS63196.2025.00087 | **no**. IEEE full text not accessible. Statement from Goldberg–Juvekar–Kabanets, ECCC TR26-091 §1 and §1.2 (PDF opened), plus a search snippet of the IEEE abstract ("deterministic quasi-polynomial-time nonadaptive reductions"). TR26-091 says "non-adaptive Turing" in §1 and "deterministic quasipolynomial-time Turing" in §1.2; both readings are reported |
| M2 | MCSP with a random oracle O | With probability 1 over O there is a P/poly reduction from the NP-hard problem of approximating hypergraph vertex cover to MCSP^O. The reduction is uniform if given O. It gives near-optimal additive hardness of approximation and extends to K^t. Heuristic instantiation with hash functions gives *candidate* deterministic poly-time many-one reductions SAT → MCSP | R. Ilango, "SAT Reduces to the Minimum Circuit Size Problem with a Random Oracle", ECCC TR23-165; FOCS 2023, pp. 733–742 (per TR26-091 references); rev. 5 Mar 2025 "Fixed bug regarding multi-output Lupanov in Section 6.2" | yes (abstract + revision note) |
| M3 | Approximate meta-complexity via cryptography | (a) Assuming sub-exponentially secure witness encryption: essentially optimal NP-hardness of approximating conditional K^t(x∣y) when t ≫ ∣y∣. Previously only factor ∣x∣^{1/poly(log log ∣x∣)}, and only for t ≪ ∣y∣. (b) **Unconditionally**: near-optimal NP-hardness of approximation for MOCSP (Yes: oracle-circuit complexity ≤ 2^{εn}; No: essentially as hard as random truth tables). (c) With probability 1 over a random oracle O, mvMCSP^O is NP-hard to approximate under quasi-poly reductions with O-access | Y. Huang, R. Ilango, H. Ren, STOC 2023; SIAM J. Comput. 54(4):819–886 (2025); ECCC TR23-046 | yes (abstract; SICOMP data from TR26-091 references) |
| M4 | **Partial MCSP (MCSP\*)** and learning programs | NP-hard under randomized poly-time many-one reductions with one-sided error. Also NP-hardness of learning programs. "Provably non-relativizing", it overcomes Ko's (1991) relativization barrier. "Mildly improving our inapproximability factor is sufficient to exclude Heuristica." The MINKT* (partial-string K^t) case is in the same theorem | S. Hirahara, FOCS 2022, pp. 968–979, ECCC TR22-119 | yes (abstract). MINKT* clause: no (via cslib `MINKTStar/Hardness.lean` docstring) |
| M5 | Multi-output MCSP | NP-hard under randomized poly-time many-one reductions; also single-output MCSP over an extended generator set. "Unless P = NP, no polynomial-time computable function can approximate the deterministic two-party communication complexity of a partial Boolean function up to a polynomial" | R. Ilango, B. Loff, I. C. Oliveira, CCC 2020, ECCC TR20-021 | yes |
| M6 | Depth-d formula MCSP; MCSP\* under ETH | Minimum depth-d formula size is NP-hard under quasi-polynomial-time randomized reductions for every constant d ≥ 2. Some function has a 2^{Ω_d(n)} additive gap between its depth-d and depth-(d+1) formula complexity. MCSP\* ∉ P under ETH; the quantitative form, 2^{o(m log m)} = N^{o(log log N)} ruled out, is the formal statement in cslib. **The ETH premise is claimed false since Oct 2026** (trap T11) | R. Ilango, FOCS 2020, ECCC TR20-183 | yes (abstract). Quantitative form: no (cslib `MCSP/PartialETH.lean`) |
| M7 | MCSP for OR∘AND∘MOD₂ circuits; DNF | OR∘AND∘MOD₂-MCSP is NP-hard under poly-time deterministic many-one reductions, and extends to MOD_m bottom gates over (ℤ/mℤ)^n. DNF-MCSP NP-hardness is due to Masek (1979), as stated in the abstract | S. Hirahara, I. C. Oliveira, R. Santhanam, ECCC TR18-030 (CCC 2018; venue from memory, not checked) | yes (Masek: secondary, via this abstract and TR20-183) |
| M8 | MINcKT^SAT; random strings | NP-hard under poly-time *deterministic* reductions ("the first result that overcomes the non-NP-hardness results of MCSP"). MINKT^SAT is DistNP-hard. EXP^NP ⊆ P^{R_K}, which refutes Allender's conjecture if EXP^NP ≠ NEXP. S₂^p-hardness of K under quasi-poly *non-adaptive* reductions | S. Hirahara, "Unexpected Hardness Results for Kolmogorov Complexity Under Uniform Reductions", STOC 2020, ECCC TR20-050 | yes |
| M9 | Conditional K^t, McK^tP[ζ] (RAM programs) | For every polynomial t(n) ≥ n², some polynomial ζ makes McK^tP[ζ] NP-complete. For t(n) ≥ 1.1n, its mild average-case hardness is equivalent to OWFs. So "basing OWFs on NP ⊄ BPP" is equivalent to a worst-to-average reduction for McK^tP[ζ] | Y. Liu, R. Pass, "On One-way Functions from NP-Complete Problems", ECCC TR21-059 (published venue not checked) | yes (abstract) |
| M10 | Conditional KT, McKTP | NP-complete under randomized poly-time reductions. Average-case hard if and only if logspace-computable OWFs exist | E. Allender, M. Cheraghchi, D. Myrisiotis, H. Tirumala, I. Volkovich, ECCC TR21-009 | yes |
| M11 | Nondeterministic K^t, MINnKT | MINnKT ∈ BPP ⇔ NP ⊆ BPP, "a solution to Ko's question in the setting of nondeterministic" K^t. MINpnKT also captures NP. Extending this to Gap-MINpnKT would exclude PH-Heuristica | J. Hu, Z. Lu, I. C. Oliveira, ECCC TR25-203 (rev. 8 Feb and 5 Jul 2026) [PREPRINT] | yes |
| M12 | Deterministic communication complexity of a given matrix (Yao 1979) | NP-hard to decide CC(f) ≤ k. NP-hard to approximate within every fixed additive error, under deterministic poly-time reductions, also in Yao's alternating model. "Includes a Lean formalization" | S. Hirahara, R. Ilango, B. Loff, ECCC TR25-094 (Jul 2025); S. Gaspers, T. Z. He, S. Mackenzie, arXiv 2508.05597 v6 (3 Nov 2026) [PREPRINT] | yes (both abstracts; Lean claim from the arXiv comments, artifact not opened) |
| M13 | Implicit MCSP (gap) and improper full-support PAC learning (TotL) | NP-hard under randomized poly-time **half-Levin** reductions, and provably *not* under randomized Levin reductions. Assumptions: sub-exponentially secure iO, and no i.o. sub-exponentially-optimal propositional proof systems. Together these imply NP ⊄ io-SIZE[2^{n^{o(1)}}] | H. Goldberg, M. Juvekar, V. Kabanets, ECCC TR26-091 (4 Jun 2026) [PREPRINT] | yes (abstract + PDF §1) |
| M14 | Partial minimum branching-program size (MBPSP\*), read-k BPs, OBDDs | Superpolynomial time under ETH (premise claimed false since Oct 2026). NP-hard to decide whether a BP for a partial function compresses to a given size. Unconditional superpolynomial lower bounds for read-once nondeterministic BPs computing the total versions | L. Glinskih, A. Riazanov, arXiv 2407.04632 (Jul 2024) | yes |
| M15 | Minimum (De Morgan) formula size, MFSP | MFSP ∉ P under ETH (premise claimed false since Oct 2026) | R. Ilango, "The Minimum Formula Size Problem is (ETH) Hard", FOCS 2021 | **no**. Secondary: search summary of the SIAM FOCS-2021 special-section abstract; IAS talk page |
| M16 | n^{1−o(1)}-approximate MCSP and MKTP | NP-intermediate if OWFs exist. MKTP is DET-hard under non-uniform NC⁰ reductions, so MKTP ∉ AC⁰[p] | E. Allender, S. Hirahara, ECCC TR17-073; journal version ACM ToCT 11(4):27 (2019), per TR26-091 references | yes |
| M17 | MOCSP (oracle MCSP with given oracle functions); (AC⁰_d)-MCSP | MOCSP is NP-complete under non-uniform AC⁰ many-one reductions and ZPP truth-table reductions. (AC⁰_d)-MCSP ∉ AC⁰[p] | R. Ilango, ECCC TR19-021. Its published version appears to be ITCS 2020, LIPIcs 34:1–34:26, "Approaching MCSP from Above and Below: Hardness for a Conditional Variant and AC0[p]" (per TR26-091 references and the cslib bibliography); the identity of the two versions was not checked | yes (abstract) |

### 2.2 Barriers to NP-hardness proofs for meta-complexity problems

| # | Statement (precise) | Reference | checked |
|---|---|---|---|
| N1 | Unconditionally, MCSP is not NP-hard under O(n^{1/2−ε})-time projections. NP-hardness under logtime-uniform AC⁰ reductions ⇒ NP ⊄ P/poly and E ⊄ io-SIZE(2^{δn}) (so P = BPP). NP-hardness under poly-time reductions ⇒ EXP ≠ NP ∩ P/poly, hence EXP ≠ ZPP. Σ₂P-hardness of nondeterministic MCSP ⇒ EXP ⊄ P/poly | C. Murray, R. Williams, ECCC TR14-164; Theory of Computing 13 (2017), 1–22 (per TR26-091 references; the CCC 2015 conference version is from memory) | yes |
| N2 | Oracle-independent ("black-box") reductions, which work for MCSP^A for every A: "essentially no language" reduces to MCSP this way by poly-time Turing reductions. One-query randomized black-box reductions only reach AM ∩ coAM. NP-hardness via poly-time *non-adaptive* reductions ⇒ ZPP ≠ EXP; the same holds for approximating circuit complexity under Turing reductions. Approximating Kt is provably not EXP-hard under poly-time Turing reductions | S. Hirahara, O. Watanabe, ECCC TR15-198 (CCC 2016; venue from memory, not checked) | yes |
| N3 | A language with a randomized poly-time non-adaptive honest reduction to ω(log n)-approximating K lies in AM ∩ coAM. NEXP *does* reduce this way to O(log n)-approximation. For every t′ there is a t such that a randomized time-t′ non-adaptive honest reduction from SAT to ω(log n)-approximating K^t ⇒ NE = coNE, or E has sub-exponential nondeterministic circuits i.o. | M. Saks, R. Santhanam, CCC 2022, ECCC TR22-074 | yes |
| N4 | Under a derandomization assumption: if approximating K^t within n^δ additive error is SAT-hard under honest randomized non-adaptive Turing reductions running in time polynomially less than t, then NP = coNP. If exact K^t is SAT-hard this way, Pessiland is excluded. Exact K SAT-hard under randomized many-one reductions with failure ≤ 1/t_R^{16} ⇒ coNP ⊆ NISZK, so NP ⊆ coAM | H. Goldberg, V. Kabanets, ECCC TR24-120 | yes |
| N5 | Assuming iO and sub-exponentially secure OWFs, a Gap version of MCSP is not NP-complete under randomized **Levin** (witness-preserving) reductions. The same holds for Gap-MKTP, additionally assuming injective PRGs | N. Mazor, R. Pass, "Gap MCSP is not (Levin) NP-complete in Obfustopia", ECCC TR24-053 (rev. 4 May 2026); CCC 2024, LIPIcs 36 (per TR26-091 references) | yes |
| N6 | Assume Gap_pMK^tP[s₁,s₂] ∉ P/poly for every polynomial p (+ worst-case derandomization). Then there exist: a hard disjoint NP pair, "a barrier towards showing that Gap_pMK^tP is NP-complete"; ZK proofs for NP with an inefficient prover and a non-uniform simulator; and conditional PRGs | Y. Liu, N. Mazor, R. Pass, ECCC TR26-051 (6 Apr 2026) [PREPRINT] | yes |
| N7 | Relativized worlds show that a relativization barrier covers many meta-complexity questions. In such worlds: MCSP ∈ P but search-MCSP ∉ P (even approximately); MCSP[2^{n/2}] and MCSP[2^{n/4}] differ; Kt is (2+ε)-approximable in P; natural proofs and auxiliary-input OWFs both do not exist; DistNP does not reduce to GapMINKT by "robust" reductions | H. Ren, R. Santhanam, "A Relativization Perspective on Meta-Complexity", ECCC TR21-089 | yes |
| N8 | MCSP^QBF is PSPACE-complete under ZPP reductions but not under logspace reductions, and not even TC⁰-hard under uniform AC⁰ reductions | E. Allender, D. Holden, V. Kabanets, ECCC TR14-176 | yes |
| N9 | MCSP is unlikely to be in P/poly. Proving it NP-complete "would imply proving strong circuit lower bounds for the class E" | V. Kabanets, J.-Y. Cai, STOC 2000, ECCC TR99-045 | yes (qualitative abstract) |

### 2.3 Unconditional lower bounds for meta-complexity problems, and non-trivial algorithms

| # | Statement | Reference | checked |
|---|---|---|---|
| L1 | MCSP ∉ AC⁰[p] for every prime p: depth-d AC⁰[p] circuits need size ≥ exp(N^{0.49/d}). The proof solves the coin problem with bias N^{−0.49}. MAJORITY and all of NC¹ are in non-uniform AC⁰ with MCSP-oracle gates | A. Golovnev, R. Ilango, R. Impagliazzo, V. Kabanets, A. Kolokolova, A. Tal, ECCC TR19-018 (ICALP 2019; venue from memory, not checked) | yes |
| L2 | MCSP needs N^{3−o(1)} De Morgan formulas, N^{2−o(1)} formulas over any basis or general BPs, 2^{Ω(N^{1/(d+2.01)})} depth-d AC⁰ circuits, and 2^{N^{1−o(1)}} at depth 2 | M. Cheraghchi, V. Kabanets, Z. Lu, D. Myrisiotis, ECCC TR19-022 (ICALP 2019; venue from memory, not checked) | yes |
| L3 | MCSP[2^{√n}] ∉ Formula[N^{2−δ}] in the worst case, for every δ > 0 | S. Hirahara, R. Santhanam, CCC 2017, LIPIcs 79:7 | no (secondary: OS18 abstract, Atserias–Müller Thm 2, CKLM19 abstract) |
| L4 | No randomized two-sided-error one-tape TM (with one-way read-only input tape) computes MCSP[2^{μ₂n}] in time N^{1.99}, for some μ₂ > μ₁. Here μ₁ is the constant for which MMW19 "implicitly showed" that MCSP[2^{μ₁n}] ∉ one-tape TIME[N^{1.01}] ⇒ P ≠ NP. Nondeterministic and parity BPs for MKTP need size Ω(N^{1.5}/log N) | M. Cheraghchi, S. Hirahara, D. Myrisiotis, Y. Yoshida, ECCC TR20-103 | yes |
| L5 | For every f, Sum-of-Squares needs degree Ω(s^{1−ε}) to prove that f has no size-s circuits (s > poly(n)), so there are no low-degree SoS proofs of NP ⊄ P/poly | P. Austrin, K. Risse, ECCC TR23-010 | yes |
| L6 | R_{nKt[γn]} ∉ NTIME[2^{o(n)}] ∩ coNTIME[2^{o(n)}] for every 1/2 < γ < 1; the previous bound was ∉ NP ∩ coNP. Estimating rnKt is hard for AMTIME[n^{polylog n}] and SIZE[n^{polylog n}] | H. Goldberg, J. Hu, Z. Lu, J. Lyu, I. C. Oliveira, ECCC TR25-215 [PREPRINT] | yes |
| L7 | Some universal decompressor U makes the Halting problem not poly-time Turing reducible to the random strings R_{C_U}. This answers Allender | A. Milovanov, ECCC TR26-034 (Feb 2026) [PREPRINT] | yes |
| U1 | Every compression problem has circuits of size 2^{4ℓ/5}·poly(t(n)). MCSP for size s(n) has circuits of size 2^{(4/5)w+o(w)}·poly(2^n), w = s·log₂(s+n), beating brute force | S. Hirahara, R. Ilango, R. Williams, ECCC TR23-171 (STOC 2024; venue from memory, not checked) | yes |
| U2 | Non-uniform Perebor is false for K^t: for every polynomial t, circuits of size 2^{4n/5+o(n)} solve the K^t problem. Black-box algorithms cannot be sub-exponential. Every efficiently computable function is invertible by circuits of size 2^{4n/5+o(n)} | N. Mazor, R. Pass, ECCC TR23-175 (ITCS 2024; venue from memory, not checked) | yes |
| U3 | Search-to-decision. GapMINKT: a 2^{εn}-time reduction that queries thresholds s + log∣x∣ (MP24). Poly-time average-case reductions for K^t. Errorless average-case search-to-decision for rK^t, unconditionally; for K^t under "E needs exponential circuits" (HKLO24) | N. Mazor, R. Pass, ECCC TR24-003; S. Hirahara, V. Kabanets, Z. Lu, I. C. Oliveira, ECCC TR24-059 | yes |

### 2.4 Worst-case versus average-case through meta-complexity (Hirahara and follow-ups)

| # | Statement | Reference | checked |
|---|---|---|---|
| W1 | First non-black-box worst-to-average reduction from a problem conjectured outside coNP to DistNP. If average-case MINKT has an errorless heuristic, then a zero-error randomized poly-time algorithm approximates MINKT within additive Õ(√k). Approximate MINKT is Random-3SAT-hard, and harder than avoiding any HSG that stretches n bits by ω̃(√n). Approximating circuit size within factor 2^{(1−ε)n} is in BPP iff its average-case version is easy. NP-hardness of approximate MINKT or MCSP would give average-case ⇔ worst-case for NP ("excluding Heuristica") | S. Hirahara, FOCS 2018, ECCC TR18-138 | yes |
| W2 | DistPH ⊆ AvgP ⇔ GapMINKT^PH ∈ P. GapMINKT^NP ∈ P ⇒ P = BPP | S. Hirahara, ECCC TR20-143 (FOCS 2020; venue from memory, not checked) | yes |
| W3 | UP ⊄ DTIME(2^{O(n/log n)}) ⇒ DistNP ⊄ AvgP. PH ⊄ DTIME(2^{O(n/log n)}) ⇒ DistPH ⊄ AvgP. NP ⊄ DTIME(2^{O(n/log n)}) ⇒ DistNP ⊄ Avg_P P | S. Hirahara, STOC 2021, ECCC TR21-058 | yes |
| W4 | NTIME[n] is not quasi-linear on average if UP ⊄ DTIME[2^{Õ(√n)}]. Under ETH (premise claimed false since Oct 2026), NTIME[n] has no average-case n^{1+ε} algorithm whose running time is estimable | L. Chen, S. Hirahara, N. Vafa, ECCC TR21-166 | yes |
| W5 | Relating average-case and worst-case PH is *equivalent* to the implication "Gap-MINpKT^PH ∈ prBPP ⇒ Mild-Gap-MINpKT^PH ∈ prBPP". The mild gap keeps the YES time bound t and moves NO to t + poly(n). The time gap can be eliminated in the average case. **In the worst case any efficient reduction between the two must be non-relativizing** | Goldberg, Hu, Lu, Lyu, Oliveira, ECCC TR26-253 (13 Oct 2026); TR25-215 §3 [PREPRINT] | yes |
| W6 | Random-noise "recovery reductions" with optimal parameters for SAT, kSAT, kCSP, CLIQUE, and others. The Bogdanov–Trevisan barrier does not apply to this mild relaxation | T. Nareddy, A. Mishra, ECCC TR25-157 [PREPRINT] | yes |

### 2.5 One-way functions versus time-bounded Kolmogorov complexity; symmetry of information; Impagliazzo's worlds

| # | Statement | Reference | checked |
|---|---|---|---|
| O1 | For every polynomial t(n) ≥ (1+ε)n: OWFs exist ⇔ K^t is mildly hard on average, i.e. no PPT algorithm computes K^t on more than a 1 − 1/p(n) fraction of n-bit strings | Y. Liu, R. Pass, FOCS 2020, ECCC TR20-052, arXiv 2009.11514 | yes |
| O2 | MKtP ∉ Heur_pBPP (two-sided mild average-case hardness, i.o.) ⇔ i.o. OWFs. MKtP ∉ Avg_pBPP (errorless) ⇔ EXP ≠ BPP. Any reduction from errorless to two-sided average-case hardness of MKtP ⇒ NP ≠ P, unconditionally | Y. Liu, R. Pass, CRYPTO 2021, ECCC TR21-056 | yes |
| O3 | KT is bounded-error hard on average ⇔ OWFs in NC⁰. A "Strong Perebor Hypothesis" for K^t ⇒ weak OWFs of hardness 2^{n−o(n)}. A Weak Perebor Hypothesis for MCSP ⇒ OWFs | H. Ren, R. Santhanam, CCC 2021, ECCC TR21-057 (rev. 25 Aug 2025) | yes |
| O4 | OWFs ⇔ for some samplable D, approximating (time-unbounded) K on D is hard. Average-case hardness of approximate MCSP on a locally samplable distribution ⇔ OWFs | R. Ilango, H. Ren, R. Santhanam, STOC 2022, ECCC TR21-082 | yes |
| O5 | Zero-error average-case hardness of MCSP[s(O(n))] ⇔ pseudorandom distributions on s(O(n))-describable strings. Under the "Universality Conjecture" the following are equivalent: OWFs; no natural proofs useful against sub-exponential circuits; hardness of learning P/poly with membership queries; MCSP[2^{εn}] zero-error hard on average | R. Santhanam, ITCS 2020, ECCC TR19-155 | yes |
| O6 | OWFs exist ⇔ approximating *distributional* Kolmogorov complexity is NP-hard under randomized poly-time reductions **and** NP is hard in the worst case. Under the "Meta-Complexity Padding Conjecture", worst-case hardness of approximate MCSP characterizes OWFs | S. Hirahara, STOC 2023, ECCC TR23-037 | yes |
| O7 | OWFs ⇔ (probabilistic) time-bounded symmetry of information fails on average. This answers Longpré–Mocas and Longpré–Watanabe. Similar dualities hold for NP ⊄ BPP and DistNP ⊄ HeurBPP | S. Hirahara, R. Ilango, Z. Lu, M. Nanashima, I. C. Oliveira, STOC 2023, ECCC TR23-035 | yes |
| O8 | OWF ⇔ (NP ⊆ CZK and NP worst-case hard) ⇔ (CZK worst-case hard and GapMCSP ∈ CZK) | S. Hirahara, M. Nanashima, STOC 2024, ECCC TR24-063 | yes |
| O9 | The first "OWF-complete" promise problem: MK^tP[s] restricted to instances of small computational depth. Its worst-case hardness against BPP (resp. P/poly) is equivalent to OWFs secure against PPT (resp. nuPPT). Fully black-box constructions from it are impossible | Y. Liu, R. Pass, ECCC TR23-103 | yes |
| O10 | MpK^{poly}P mildly hard on average over *any* samplable D ⇔ over the uniform D ⇔ OWFs | Y. Liu, R. Pass, ECCC TR23-152 | yes |
| O11 | (i.o.) OWFs ⇔ average-case easiness of approximating pKt with two-sided error implies mild average-case easiness with one-sided error | S. Hirahara, Z. Lu, I. C. Oliveira, ECCC TR24-136 | yes |
| O12 | Efficient coding theorem for rK^poly if OWFs do not exist. OWF ⇔ failure of average-case symmetry of information for rK^poly (resolving the HILNO23 question) | S. Hirahara, Z. Lu, M. Nanashima, ECCC TR24-155 | yes |
| O13 | Impagliazzo's worlds via conditional pK^t. NP ⊆ BPP ⇔ conditional pK^t is easy in the worst case for sublinear t. DistNP ⊆ HeurBPP ⇔ easy over samplable distributions for sublinear t. No i.o. OWF ⇔ easy for large polynomial t. **Conditional pK^t is NP-hard for sublinear t; NP-hardness for large polynomial t would eliminate Pessiland** | Z. Lu, R. Santhanam, ECCC TR24-085 | yes |
| O14 | Under "E ⊄ ioNTIME[2^{kn}]/2^{εn}", OWFs ⇔ the *boundary* version of K^t (K^{t₂}(x) ≥ n−1 versus K^{t₁}(x) ≤ n − log n) is not in ioBPP; unconditionally for pK^t. A later paper weakens the assumption to E ⊄ ioSIZE[2^{o(n)}] using randomized K^t. It also gives the first worst-to-average reduction for *exact* K^t | Y. Liu, R. Pass, ECCC TR25-125 (Aug 2025), TR25-202 (Dec 2025) [PREPRINT] | yes |
| O15 | **"Sharp" characterization of Pessiland.** NP is hard on average ⇔ approximating the MDL of programs in agnostic learning on average within ℓ^{1−o(1)} is hard. No OWF ⇔ it is easy within O(ℓ) over every samplable distribution. Pessiland is ruled out iff this small gap is closed. The base result is NP-hardness of approximating CMMSA within ℓ^{1−o(1)}, improving Hirahara's ℓ^{Ω(1)}; this is optimal unless NP ⊆ coAM. **Revision (23 Jun 2026): "technical flaw in the original proof of Lemma 5.10"; the theorem now holds for ℓ a sufficiently large constant rather than small super-constant** | S. Hirahara, M. Nanashima, ECCC TR26-052 [PREPRINT] | yes (abstract + change note) |
| O16 | Two-message arguments with a non-trivial *inefficient* simulator ⇒ errorless average-case hardness of MKtP over the uniform distribution. "The first complexity-theoretic consequence of ZK with even just slightly super-polynomial-time simulation" | G. Arnon, N. Mazor, R. Pass, J. Silbak, ECCC TR26-322 (19 Nov 2026) [PREPRINT] | yes |
| O17 | If an NP language L has no ε-witness-canonicalization, then, under derandomization, constant-round honest-verifier WI proofs for L ⇒ i.o. auxiliary-input OWFs. There are analogous consequences for compressing BARGs and SNARGs | same authors, ECCC TR26-333 (19 Nov 2026) [PREPRINT] | yes |
| O18 | Symmetry of information **fails unconditionally for rKt** and for pKt. This is the first such unconditional result for a randomized measure. There is also a near-optimal lower bound for estimating conditional rKt | J. Hu, Y. Manor, I. C. Oliveira, ECCC TR26-021 (Feb 2026) [PREPRINT] | yes |
| O19 | SoI holds *on average* for randomized extensions of nKt. Its worst-case validity would imply breakthrough separations, including a collapse of exponential time to low levels of PH. Worst-case SoI for pnKt ⇒ coNP ⊄ AM | GHLLO, ECCC TR26-290 (14 Oct 2026), TR25-215 [PREPRINT] | yes |
| O20 | Chain rule for conditional K^t with error o(N) ⇔ (E ⊄ io-SIZE[2^{o(n)}] **and** GapMcK^tP ∈ promise-P). If GapMcK^tP is NP-hard ("true under cryptographic assumptions [Huang et al.]"), this becomes "chain rule ⇔ NP = P", Kolmogorov's 1960s suggestion | V. Kabanets, A. Kolokolova, ECCC TR25-089 (rev. 13 Mar 2026) [PREPRINT] | yes |
| O21 | Parallel time-bounded Kolmogorov complexity KP^t, one variant per AC⁰, AC⁰[p], ACC⁰, TC⁰. Average-case approximation of KP^t ⇔ learnability of that constant-depth class. The natural proofs for AC⁰ and AC⁰[p] give approximation algorithms for KP^t | M. Carmosino, M. Juvekar, ECCC TR26-176 (Sep 2026) [PREPRINT] | yes |
| O22 | Further equivalences, listed without detail. Interactive K^t ⇔ key agreement (Ball–Liu–Mazor–Pass, TR24-055). Worst-case white-box learning on computationally shallow instances ⇔ public-key encryption (Liu–Mazor–Pass, TR24-195). OWF ⇔ almost-optimal compression is hard on average for some efficient distribution (Zimand, TR24-201). OWF ⇔ non-robustness of polynomial-time dimension (Nandakumar et al., TR25-028). EFI pairs ⇔ hardness of a quantum Kolmogorov-like measure (Cavalar et al., TR25-221) | as listed | yes (abstracts) |

### 2.6 NP-hardness of learning; learning ↔ natural proofs

| # | Statement | Reference | checked |
|---|---|---|---|
| P1 | NP-hardness of learning efficient programs under randomized poly-time many-one reductions. "Provably non-relativizing", it overcomes Ko's barrier | Hirahara, FOCS 2022 (= M4) | yes |
| P2 | Witness encryption for L ∈ NP ⇔ a half-Levin reduction from L to Computational Gap Learning (CGL, of Applebaum–Barak–Xiao 2008). Unconditional NP-hardness of "semi-proper" agnostic learning: for some polynomial s, learning size-s(n) circuits by circuits of size s(n)·n^{1/(log log n)^{O(1)}} is NP-hard. NP-hardness of improper learning for circuits with a random-string oracle and for RAM programs (a MINLT variant). Improving ABX08: if improper agnostic PAC learning is NP-hard under randomized non-adaptive reductions (with restrictions), then NP ⊄ BPP ⇒ i.o. OWFs | H. Goldberg, V. Kabanets, ECCC TR25-070 | yes |
| P3 | Under rETH (premise claimed false since Oct 2026): PAC-learning size-n monotone formulas by monotone circuits of size n^{(log n)^{1−ε}} needs time n^{Ω(log n)}; m^{1−δ}-approximating minimum monotone circuit size consistent with m(n) examples needs time m^{Ω(log m)}. Proved by lifting from Atserias–Müller's hardness of automating Resolution | B. P. Cavalar, S. F. de Rezende, M. Gray, R. Santhanam, ECCC TR26-128 / arXiv 2607.12331 (Jul 2026) [PREPRINT] | yes |
| P4 | Natural properties (in the Razborov–Rudich sense) ⇒ randomized learning and compression algorithms. Corollary: quasi-polynomial-time learning of AC⁰[p] (uniform distribution, membership queries) | M. Carmosino, R. Impagliazzo, V. Kabanets, A. Kolokolova, CCC 2016, ECCC TR16-008 | yes |
| P5 | Learning speed-ups. Non-uniform dichotomy: non-trivial learning for C[n^{O(1)}] ⇔ no exponentially secure PRFs in C[n^{O(1)}]. P-natural proofs against C[2^{n^ε}] ⇒ ZPEXP ⊄ C[n^{O(1)}] | I. C. Oliveira, R. Santhanam, CCC 2017, ECCC TR16-197 | yes |
| P6 | Equivalence: hardness of approximate or worst-case MCSP against almost-linear circuits ⇔ hardness of sub-exponential non-adaptive learning ⇔ no Circuit[poly(N)]-natural property useful against Circuit[n^d] ⇔ non-uniform PRFs secure against sub-exponential circuits | CHOPRS, Thm 1 (= H8) | yes |
| P7 | Pessiland is good for learning: universal-extrapolation learners exist if no OWF does. The first characterization of OWFs by worst-case hardness of a promise problem in AM | S. Hirahara, M. Nanashima, ECCC TR23-100 (FOCS 2023; venue from memory, not checked) | yes |
| P8 | If natural proofs ⇒ PAC learning held for every class, standard lattice assumptions would fail: depth-2 majority has a natural proof (Nisan) but is hard to PAC-learn under lattice assumptions (Klivans–Sherstov). Nisan-type natural proofs give distributional PAC learning | A. Karchmer, ECCC TR23-085 | yes |
| P9 | Ko (1991): there is no *relativizing* proof of NP-hardness of learning programs (MINLT) | K. Ko, SICOMP 1991 | no (secondary: Hirahara TR22-119 abstract) |

### 2.7 Hardness magnification: what slightly superlinear bound would imply what, and how far known bounds fall short

**(i) Thresholds that would give NP ⊄ P/poly or P ≠ NP.**

| # | Sufficient lower bound | Consequence | Reference | checked |
|---|---|---|---|---|
| H1 | Gap-MCSP[2^{βn}/(cn), 2^{βn}] ∉ Circuit[N^{1+ε}] for every small enough β > 0 (some ε > 0, universal c) | **NP ⊄ Circuit[poly]** (NP ⊄ P/poly) | I. C. Oliveira, J. Pich, R. Santhanam, CCC 2019, ToC 17(11):1–38 (2021), ECCC TR18-158 (= 02:H2) | yes |
| H2 | search-MCSP[n^c] lacks Õ(N)-size, Õ(1)-depth circuits, for some c ≥ 1 | **NP ⊄ P/poly** | D. McKay, C. Murray, R. Williams, STOC 2019, pp. 1215–1225 (= 02:H3) | yes (PDF) |
| H3 | For some time-constructible s(n) ≥ n and some A ∈ PH, search-MCSP^A[s(n)] has no poly(s(n))-space streaming algorithm with poly(s(n)) update time (MMW Thm 1.3). Example: "SAT-oracle circuits of size 2^{n/log* n}" cannot be synthesized with N^ε update time and N^ε space | **P ≠ NP** | MMW19 Thm 1.3 | yes (PDF) |
| H4 | MCSP[2^{μ₁n}] cannot be computed by a one-tape TM (with a one-way input tape) in time N^{1.01}, for some μ₁ > 0 ("implicit" in MMW19) | **P ≠ NP** | as stated by Cheraghchi–Hirahara–Myrisiotis–Yoshida, ECCC TR20-103 | yes (CHMY abstract); MMW19 implicit form not traced |
| H5 | For every c > 0 there are a schedule s and an n with complexity(MCSP[s] slice of length 2^n) > 2^n·c·(n+s(n)+1)^c (gates, fan-in-2 De Morgan, decision version, no oracle) | NP ⊄ P/poly, and P ≠ NP (`not_NP_subset_PPoly_of_yesSet_hard`, `P_ne_NP_of_yesSet_hard`) | cslib-frontier `CslibFrontier/Computability/MCSP/Magnification.lean` (formal specialization of MMW19 Thm 1.4) | yes (Lean statement read; not built) |
| H6 | A uniform AC⁰[qpoly] Student–Teacher protocol generating truth tables of super-fixed-polynomial circuit complexity | **P ≠ NP** | M. Carmosino, S. Grosser, ECCC TR25-045 [PREPRINT] | yes |
| H7 | n^{−ε}-MCSP[σ] ∉ P-uniform-SIZE[n^{1+ε+o(1)}] for some ε > 0 and some σ(ℓ) ≤ 2^{o(ℓ)} | **P ≠ NP^{⊕P}** (not P ≠ NP) | A. Atserias, M. Müller, arXiv 2503.24061 v2 (Jun 2025), Thm 11 (= 02:H7) | yes (PDF) |

**(ii) Thresholds for fixed-polynomial or NC¹-type consequences (these are the "frontiers").**

| # | Sufficient lower bound | Consequence | Best known lower bound for the same problem or model | Gap | Reference | checked |
|---|---|---|---|---|---|---|
| H8 | Some 2^{n^{o(1)}}-sparse L ∈ NP with L ∉ Circuit[n^{1+ε}]. It even suffices to beat n^{1+ε}-time, n^ε-space algorithms with n^ε advice | NP ⊄ SIZE[n^k] ∀k (analogues for formulas, BPs, AC⁰[6], TC⁰) | No superlinear bound for any explicit function in general circuits. B2: 3.1n − o(n) peer-reviewed, 4n − O(log n) preprint (02:G1–G2) | superlinear growth needed | L. Chen, C. Jin, R. Williams, FOCS 2019, pp. 1240–1255 (venue confirmed via Atserias–Müller references; 02 had "venue not verified"), ECCC TR19-118 | yes |
| H9 | An n^{α(n)}-sparse NP language (α ≤ log n/log log n) with no *probabilistic* circuits of 2n + O(n/log log n) gates | NTIME[2^n] ⊄ SIZE[2^{n^{1/5}}] and NP ⊄ SIZE[n^k] ∀k | An O(n)-sparse P language needs probabilistic circuits of size ≥ 2n − 2 | **sub-linear additive gap** ("even a sub-linear additive improvement ... would imply NEXP ⊄ P/poly") | L. Chen, J. Li, T. Yang, ECCC TR22-086 (= 02:H5) | yes |
| H10 | MCSP[(log n)^c] ∉ probabilistic formulas of size n^{2+ε} | NP ⊄ Formula[n^k] ∀k; #SAT ∉ log-depth circuits | MCSP[(log n)^c] has no n^{2−o(1)}-size probabilistic formulas (same paper) | **sharp: n^{2−o(1)} vs n^{2+ε}** | L. Chen, C. Jin, R. Williams, STOC 2020, pp. 1335–1348, ECCC TR20-065 | yes |
| H11 | n^{−ε}-Q ∉ FML[n^{1+2ε+o(1)}] or n^{−ε}-Q ∉ PFML[n^{2ε+o(1)}], for some 2^{n^{o(1)}}-sparse Q ∈ NP (Thm 9). n^{−ε}-Q: YES = Q, NO = strings at relative Hamming distance ≥ n^{−ε} from Q | NP ⊄ FML[n^c] ∀c | Thm 10: n^{−ε}-MCSP[2^{√ℓ}] ∉ PFML[n^{2ε−δ}] for all 0 < ε, δ ≤ 1 (one-sided error) | **sharp: n^{2ε−δ} vs n^{2ε+o(1)}**. "For small ε the thresholds are well below known lower bounds" | Atserias–Müller 2025, Thms 9–10 | yes (PDF) |
| H12 | MCSP[2^{√n}] cannot be solved on average with zero error by formulas of linear, even sub-linear, size | NP ⊄ Formula[poly] | MCSP[2^{√n}] ∉ Formula[N^{2−δ}] in the worst case (L3) | average-case versus worst-case, and linear versus near-quadratic | I. C. Oliveira, R. Santhanam, FOCS 2018, pp. 65–76, ECCC TR18-139 (= 02:H1) | yes |
| H13 | MKtP[N^ε, N^ε + 5 log N] requires circuits of size N^{1+δ} | EXP ⊄ SIZE(poly) | — | — | OS18 (same abstract) | yes |
| H14 | Gap-MKtP[2^{βn}, 2^{βn}+cn] ∉ TC⁰[N^{1+ε}], ∉ B2-Formula[N^{2+ε}], ∉ U2-Formula[N^{3+ε}], ∉ BP[N^{2+ε}], or ∉ AC⁰[6][N^{1+ε}] | EXP ⊄ TC⁰[poly], Formula[poly], Formula[poly], BP[poly], AC⁰[6] respectively | "lower bounds similar to (3)–(5) hold for various regimes of parameters". Model where the threshold lies below known bounds: U2-formulas with parity leaves | — | OPS19 (abstract) | yes |
| H15 | n-bit TC⁰ circuits of depth d need n^{1+c^{−d}} wires for certain NC¹-complete functions, for every c > 1 and large d | TC⁰ ≠ NC¹ | Known for fixed c ≈ 2.41 | **the constant c** | L. Chen, R. Tell, STOC 2019, ECCC TR18-199 | yes |
| H16 | search-MCSP[2^{βm}] has no De Morgan formulas of size n^{3+ε}, for all β > 0 | ⊕P ⊄ NC¹ | MCSP needs N^{3−o(1)} De Morgan formulas (L2) | n^{3−o(1)} vs n^{3+ε} | CJW19 (abstract) | yes |
| H17 | Constructivizing known lower bounds (streaming, one-tape TMs, query complexity, MCSP) | separations from EXP ≠ BPP up to P ≠ NP. Conversely, any proof of P ≠ NP, P ≠ PSPACE, ZPP ≠ EXP, BPP ≠ NEXP implies a constructive separation. Detecting high t-time Kolmogorov complexity has **no** constructive separation from any class | — | — | L. Chen, C. Jin, R. Santhanam, R. Williams, TheoretiCS 3 (2024), arXiv 2203.14379 | yes |

**(iii) The CHOPRS "magnification frontiers", verbatim structure.** Items 1–4 mean: (1) magnification theorem; (2) hardness under a standard conjecture; (3) lower bound for an easier function; (4) lower bound for Q itself. Source: L. Chen, S. Hirahara, I. C. Oliveira, J. Pich, N. Rajgopal, R. Santhanam, "Beyond Natural Proofs: Hardness Magnification and Locality", ITCS 2020, LIPIcs 151:70; J. ACM 69(4):25 (2022); ECCC TR19-168, §1.1. checked: yes (PDF).

| Frontier | (1) needed | (1) ⇒ | (3) easier function | (4) best known for Q | Where Item 3/4 techniques stand |
|---|---|---|---|---|---|
| A: MKtP[n^c, 2n^c] vs AC⁰-XOR | ∉ AC⁰-XOR[N^{1.01}] | EXP ⊄ NC¹ | Majority ∉ AC⁰-XOR[2^{N^{o(1)}}] (Razborov–Smolensky) | MKtP[n^c, 2n^c] ∉ AC⁰ | localize (Prop. 39) |
| B: MCSP[2^{n^{1/3}}, 2^{n^{2/3}}] vs Formula-XOR | ∉ Formula-XOR[N^{1.01}] | NQP ⊄ NC¹ | InnerProduct ∉ Formula-XOR[N^{1.99}] (via Tal 2017) | ∉ Formula[N^{1.99}] (HS17; OPS19) | localize (Thm 2: B1^O, B3^O, B4^O). Note Formula-XOR[N^{1.01}] ⊆ Formula[N^{3.01}] (CHOPRS fn. 1) |
| C: MCSP[2^{√n}/10n, 2^{√n}] vs almost-formulas | ∉ N^{0.01}-Almost-Formula[N^{1.01}] | NP ⊄ NC¹ | PARITY ∉ N^{0.01}-Almost-Formula[N^{1.01}] | ∉ Formula[N^{1.99}] | localize (§5) |
| D: MCSP[2^{√n}] vs GapAND_{O(N)}-Formula (one-sided randomized formulas) | ∉ GapAND-Formula[N^{2.01}] | NQP ⊄ NC¹ | Andreev ∉ GapAND-Formula[N^{2.99}] (implicit in Håstad 1998); MCSP[2^n/n⁴] ∉ GapAND-Formula[N^{2.99}] (implicit in CKLM19) | **∉ GapAND-Formula[N^{1.99}]** (CJW20, building on HS17, OPS19) | **gap N^{1.99} vs N^{2.01}** ("nearly-tight"); localizes (Thm 47) |
| E: (n−k)-Clique, k = (log n)^C, vs AC⁰ | ∉ AC⁰[m^{1.01}], m = Θ(n²) | NP ⊄ NC¹ | Parity ∉ AC⁰ | (n−k)-Clique ∉ monotone P/poly for some k = (log n)^C ([AJ08] = Andreev–Jukna 2008) | localizes (Prop. 50) |

Comparing columns (1), (3) and (4) gives how far the known bounds fall short. In every frontier, the lower-bound techniques of columns (3) and (4) extend to circuits with small-fan-in oracles (CHOPRS §5), while column (1)'s problems have such oracle circuits (Thm 2 B1^O type statements). That is the locality barrier (B8). [AJ08] is A. E. Andreev, S. Jukna, "Very large cliques are easy to detect", Discrete Math. 308(16):3717–3721, 2008, taken from the CHOPRS reference list (not opened).

**(iv) Related magnification and refutation facts.**

| # | Statement | Reference | checked |
|---|---|---|---|
| H18 | **The Anti-Checker Hypothesis of OPS19 is false.** Thm 59: there is a universal c such that, for all ε > 0 and α > 2, MCSP[n^c, 2^{(ε/α)n}] has no oracle formulas F with SIZE₃(F) ≤ N^{2−ε} and adaptivity o(log N/log log N) | CHOPRS Thm 59, Cor. 61 | yes (PDF) |
| H19 | One lower bound above a magnification threshold is provably *non-localizable*. Thm 49: some L ∈ E has L ∉ GapAND_{O(N)}-Formula[N^{3−ε}] for every ε, yet L ∈ O_{N^{o(1)}}-Formula[N²]. Also, parity has O(n)-wire TC⁰ circuits of depth O(1/ε) with ≤ n^{1−ε} oracle gates of fan-in ≤ n^ε (Allender–Koucký 2010; Chen–Tell 2019), while Parity ∉ TC⁰_d[n^{1+c^{−d}}] (IPS97). So that super-linear bound does not localize | CHOPRS §1.3, Thm 49 | yes (PDF) |
| H20 | The approximation method is localizable in many cases. In particular, "one cannot use the approximation method to derive an extremely strong constant-depth circuit lower bound and then magnify it to an NC¹ lower bound for an explicit function" | J. Pich, arXiv 2212.09285 (Dec 2022) | yes |
| H21 | Assume the witnessing formulas w_n^k(f) are tautologies. Then any super-polynomial lower bound for Extended Frege + w_n^k(f) axioms ⇒ SAT needs super-polynomial circuits. Unconditional: proof-complexity lower bounds for a concrete strong non-uniform proof system ⇔ super-polynomial circuit lower bounds for Discrete Log | J. Pich, R. Santhanam, ECCC TR23-199 | yes |
| H22 | CSH^a_b (the circuit size hierarchy) is provable in T²₂. If it is provable in T¹₂ for some a > b > 1, then P^NP needs circuits of size n^{1+ε} | M. Carmosino, V. Kabanets, A. Kolokolova, I. C. Oliveira, D. Tsintsilidas, ECCC TR24-145 | yes |

### 2.8 The barriers: exact statements from the sources

| # | Barrier | Exact statement | What evades it, and why | Reference | checked |
|---|---|---|---|---|---|
| B1 | **Relativization** | There are oracles A, B with P^A = NP^A and P^B ≠ NP^B. So any proof that relativizes, i.e. holds for all oracles, cannot settle P vs NP. A PSPACE-complete A (e.g. TQBF) gives P^A = NP^A | IP = PSPACE and MIP = NEXP (arithmetization; AW09: they do *not* relativize but *do* algebrize). MA_EXP ⊄ P/poly (Buhrman–Fortnow–Thierauf), PP ⊄ SIZE(n^k) (Vinodchandran), promise-MA ⊄ SIZE(n^k) (Santhanam): non-relativizing but algebrizing (CHR25 abstract). Williams' NEXP ⊄ ACC⁰: there is an oracle with NEXP^A ⊂ ACC^A (Williams 2014 §1, citing Aaronson, personal communication). Hirahara 2022 (M4): "provably non-relativizing". | T. Baker, J. Gill, R. Solovay, SIAM J. Comput. 4(4):431–442, 1975 | **no** for the primary. Statement via AW09 §1 (opened) and cslib `Classes/Oracle/Collapse.lean` (`baker_gill_solovay`, read) |
| B2 | **Natural proofs** | A property C_n of n-variable functions is Γ-natural (density δ_n) if it contains a subproperty that is *large* (≥ 2^{2^n}·δ_n functions) and *constructive* (decidable from the 2^n-bit truth table in Γ). It is *useful* against Λ if no Λ-computable sequence lies in C_n infinitely often. Quantitative form (Chow's Thm 1, "a slightly stronger version ... than the one that appears in their paper"): fix c ≥ 1, d > 1, ε > 0. If a 2^{k^ε}-hard PRG G_k: {0,1}^k → {0,1}^{2k} in SIZE(k^c) exists, then for every e > 1 + cd/ε there is no P/poly-natural property of density > 2^{−n^d} useful against SIZE(n^e). Here "2^{k^ε}-hard" means every circuit with < 2^{k^ε} gates has distinguishing advantage < 2^{−k^ε} | Diagonalization-based lower bounds; Williams: "we circumvent the natural proofs barrier because of the use of diagonalization ... it looks unlikely that one may extract any P-natural or NP-natural properties from the proof". Williams 2016 (B4): for NEXP lower bounds constructivity is *unavoidable*, so these proofs must avoid *largeness*. Some magnification instances: by CHOPRS Thm 1 their lower bounds are *equivalent* to the non-existence of natural properties. Chow 2011 (B3): "almost-natural" properties exist | A. A. Razborov, S. Rudich, J. Comput. Syst. Sci. 55(1):24–35, 1997 (STOC 1994) | **no** for the primary (Rudich's natural.ps is a bitmap-font PostScript, and no converter was available). Statement via T. Chow, arXiv 0805.1385, Defs 2–6 and Thm 1 (PDF opened) |
| B3 | Almost-natural proofs | Under RR's assumption (2^{n^ε}-hard PRG in P/poly) there is a nearly-linear-time constructive property ("discrimination") of density Ω(2^{−q(n)}), q quasi-polynomial, separating NP from P/poly. So slightly weakening largeness breaks the barrier, but this does not by itself give a lower-bound method | — | T. Y. Chow, "Almost-natural proofs", arXiv 0805.1385 (submitted to JCSS; the paper mentions a FOCS 2008 extended abstract; journal year not checked) | yes |
| B4 | Constructivity is unavoidable | For "typical" non-uniform C: NEXP ⊄ C ⇔ some poly-time algorithm distinguishes some function from all C-computable functions, i.e. a constructive (not necessarily large) useful property. "No P-natural properties useful against C" ⇔ randomized exponential time can be derandomized using truth tables of C-circuits as seeds | Shows the ACC-type proofs evade RR through the largeness condition | R. Williams, "Natural Proofs Versus Derandomization", STOC 2013 special issue (per arXiv comment; journal SICOMP from memory), arXiv 1212.1891 | yes |
| B5 | **Algebrization** | Def. 2.3: an inclusion C ⊆ D algebrizes if C^A ⊆ D^Ã for all A and all finite-field extensions Ã of A of multidegree ≤ c. A separation C ⊄ D algebrizes if C^Ã ⊄ D^A for all A, Ã. Known algebrizing results: PSPACE^A ⊆ IP^Ã, NEXP^A ⊆ MIP^Ã, MA_EXP^Ã ⊄ P^A/poly, PromiseMA^Ã ⊄ SIZE^A(n^k). Oracles exist with **NP^Ã ⊆ P^A** (indeed PSPACE^Ã ⊆ P^A), NP^A ⊄ P^Ã, NP^A ⊄ BPP^Ã, P^{NP^A} ⊄ PP^Ã, **NEXP^Ã ⊂ P^A/poly** (Thm 5.6: NTIME^Ã(2^n) ⊂ SIZE^A(n)), EXP^{NP^Ã} ⊂ P^A/poly (Thm 5.7), BPEXP^Ã ⊂ P^A/poly (Thm 5.8), and **NP^Ã ⊂ SIZE^A(n)**. Hence P vs NP, RP ⊆ P, NEXP ⊄ P/poly and *superlinear circuit lower bounds for NP* need non-algebrizing techniques. AW09's extensions only need multidegree ≤ 2 (multiquadratic) | Williams' ACC⁰ bound: "definitely avoids relativization and algebrization because there are oracles A relative to which NEXP^A ⊂ ACC^A, and even NEXP^Ã ⊂ ACC^A"; "all known improved SAT algorithms break down when oracles (or algebraic extensions thereof) are added" | S. Aaronson, A. Wigderson, ACM TOCT 1(1), 2009 (STOC 2008), ECCC TR08-005 | yes (PDF, §1, Defs 2.2–2.3, Thms 5.6–5.8) |
| B6 | Algebrization, axiomatic version | Adds an "Arithmetic Checkability" axiom ("all NP languages have verifiers that are efficiently computable low-degree polynomials over the integers") to the Arora–Impagliazzo–Vazirani theory of relativizing techniques. "Most known complexity results proved using arithmetization are provable within our theories, while many open questions are independent of the theories" | — | R. Impagliazzo, V. Kabanets, A. Kolokolova, STOC 2009 | yes (authors' abstract page) |
| B7 | Affine relativization | Reformulates algebrization with closure properties, using "affine oracles" (an error-correcting code applied to the characteristic string). "Every statement that AW declare as algebrizing does relativize affinely" (abstract, truncated in my copy) | — | B. Aydınlıoğlu, E. Bach, ECCC TR16-040 (journal version; ToCT 2018 from memory, not checked) | yes (abstract) |
| B8 | **Locality** | Magnification theorems are proved by unconditionally constructing very efficient circuits for Q that contain small-fan-in oracle gates. Many lower-bound techniques for weak models "quite often easily extend to circuits containing such oracles", so they cannot prove the lower bounds magnification needs. Frontier-B instance (Thm 2): **B1^O** for any ε > 0, MCSP[2^{n^{1/3}}, 2^{n^{2/3}}] ∈ Formula-O-XOR[N^{1.01}], with oracle gates of fan-in ≤ N^ε placed just above the XOR leaves. **B3^O** for any δ > 0, InnerProduct on N bits has no N^{2−3δ}-size Formula-O-XOR circuits with ≤ N^{2−3δ} oracle gates of fan-in N^δ. **B4^O** Thm 59 (H18). Reductions InnerProduct → MCSP of the needed form cannot exist | AK10/CT19 parity example and Thm 49 (H19). Atserias–Müller's uniform route (H7) "seems to sidestep the localization barrier" because "Santhanam and Williams' proof does not seem to localize" | CHOPRS (above), §1.3 | yes (PDF) |
| B9 | **GCT: rectangular Kronecker coefficients** | "The vanishing of rectangular Kronecker coefficients cannot be used to prove superpolynomial determinantal complexity lower bounds for the permanent polynomial" | — | C. Ikenmeyer, G. Panova, arXiv 1512.03798 (FOCS 2016 / Adv. Math.; venues from memory, not checked) | yes (abstract) |
| B10 | **GCT: no occurrence obstructions** | Thm 1.4: "Let n, d, m be positive integers with n ≥ m^{25} and λ ⊢ nd. If λ occurs in C[Z_{n,m}], then λ also occurs in C[Ω_n]. In particular, Conjecture 1.3 [existence of occurrence obstructions] is false." Here Z_{n,m} is the orbit closure of the padded permanent and Ω_n that of det_n. Cor. 2.6: the same against power sums PS_n. The permanent may be replaced by any degree-m polynomial in m² variables. Multiplicity obstructions are *not* ruled out (§1(c)) | — | P. Bürgisser, C. Ikenmeyer, G. Panova, arXiv 1604.06431 v3 ("To appear in the Journal of the AMS"; JAMS 2019) | yes (PDF Thm 1.4, Cor 2.6) |
| B11 | Black-box worst-to-average for NP | If an NP-complete problem has a non-adaptive self-corrector w.r.t. a samplable distribution, then coNP ⊆ NP/poly and PH collapses to Σ₃. So average-case hardness of NP, or OWF security, "cannot be based (using non-adaptive reductions) on the worst-case complexity of an NP-complete problem (unless the polynomial hierarchy collapses)". Feigenbaum–Fortnow 1993 proved this for random self-reductions | Hirahara 2018 (W1): the reduction is non-black-box, from a problem believed outside coNP. Recovery reductions (W6) relax the model | A. Bogdanov, L. Trevisan, ECCC TR05-015 (FOCS 2003 / SICOMP 2006; venues from memory, not checked) | yes (abstract). FF93: secondary via this abstract |
| B12 | OWF from NP-hardness | Non-adaptive black-box reductions cannot base OWFs on NP-hardness (Akavia–Goldreich–Goldwasser–Moshkovitz 2006, "strong evidence"). Basing AIPRGs on NP-hardness this way collapses PH; for AIOWF/AIHSG it would give OWFs from NP-hardness | Hirahara 2023 (O6) and Liu–Pass 2023 (O9) use non-black-box analyses | M. Nanashima, ECCC TR20-095 (ITCS 2021) | yes for Nanashima; AGGM06 no (secondary via Nanashima's abstract) |
| B13 | NP-hardness of learning | Applebaum–Barak–Xiao 2008: black-box limits on basing learning lower bounds on worst-case assumptions; defines CGL | Hirahara 2022, GK25, GJK26 (non-black-box or half-Levin) | B. Applebaum, B. Barak, D. Xiao, "On Basing Lower-Bounds for Learning on Worst-Case Assumptions", FOCS 2008, pp. 211–220 (bibliographic data from TR26-091 references) | no (secondary via GK25 abstract) |
| B14 | Bounded relativization | A statement is C-relativizing if it holds relative to every oracle in C. IP = PSPACE is PSPACE-relativizing. Improving Impagliazzo–Wigderson to worst-case derandomization, Oliveira–Santhanam's pseudodeterministic constructions to a.e., or Santhanam's pr-MA ⊄ SIZE(n^k) to a.e., **by PSPACE-relativizing techniques ⇒ NP ≠ L** (indeed PSPACE ≠ EXPH). New result: BPE^{MCSP}/2^{εn} ⊄ SIZE[2^n/n] | — | S. Hirahara, Z. Lu, H. Ren, ECCC TR23-070 (CCC 2023; venue from memory, not checked) | yes |
| B15 | Algebraic natural proofs | Essentially all known algebraic circuit lower bounds cannot be used against VP *iff* succinct hitting sets for VP exist (GKSS17). Over characteristic 0, VNP has **no** efficient equations if the permanent is exponentially hard (CKRST, rev. 2024). VP with bounded coefficients has efficient equations | — | J. Grochow, M. Kumar, M. Saks, S. Saraf, ECCC TR17-009; P. Chatterjee, M. Kumar, C. Ramya, R. Saptharishi, A. Tengse, ECCC TR20-063 (rev. 28 Feb 2024) | yes. Forbes–Shpilka–Volk 2018: no (secondary, CKRST abstract) |

### 2.9 Newer barriers and limitations, 2015–2026 (besides B10–B15)

| # | Statement | Reference | checked |
|---|---|---|---|
| X1 | **Algebrization barriers via XOR-Missing-String.** There is an oracle A₁ with *multilinear* extension Ã₁ such that PostBPE^{Ã₁} has linear-size A₁-oracle circuits on infinitely many lengths. So PostBPE ⊄ i.o.-SIZE[O(n)] needs non-algebrizing techniques, while MA_E ⊄ P/poly algebrizes. There is an (A₂, Ã₂ multilinear) with BPE^{Ã₂} in linear-size A₂-circuits on *all* lengths; AW09 needed a multiquadratic extension. A natural subclass of MA_E containing the Buhrman–Fortnow–Thierauf hard language has h(n)-size circuits for every super-half-exponential h relative to some (A₃, Ã₃), "suggest[ing] that half-exponential might be the correct barrier for MA_E circuit lower bounds w.r.t. algebrizing techniques" | L. Chen, Y. Hu, H. Ren, ECCC TR25-184 / arXiv 2511.14038 (ITCS 2026) | yes |
| X2 | **Unconditional AC⁰-natural barrier.** "No AC⁰-natural proof can prove a lower bound greater than 2^{n^{7/(d−5)}} against depth-d circuits", by localizing the Trevisan–Xue PRG. Most known constant-depth techniques are AC⁰-natural. The state of the art via the switching lemma is 2^{n^{1/(d−1)}}. Conditionally, natural proofs cannot prove 2^{n^{c/d}} for some large c | B. Loff, S. Sherif, N. Talebanfard, F. Ugazio, arXiv 2606.12631 (10 Jun 2026) [PREPRINT] | yes |
| X3 | Oracle results on algorithmic methods. Constructing restricted uniform circuits for Missing-String ⇔ constructing hard functions (relativizing). There is an oracle where SAT is solvable in half-exponential time yet EXP ⊂ P/poly; relative to *all* oracles, SAT in sub-half-exponential time ⇒ EXP ⊄ P/poly. **The conference version had an incorrect theorem; the ECCC version proves the negation of its Theorem 1.10** | N. Vyas, R. Williams, ECCC TR24-113 (= 02:K16) | yes (abstract) |
| X4 | **mABP min-partition-rank barrier.** Claim: there is a full-rank multilinear polynomial computable by a polynomial-size multilinear ABP, so the min-partition rank method cannot prove superpolynomial mABP lower bounds. **The 11 May 2026 revision states that an anonymous referee found a gap in Lemma 4.1, on which "all the results in the paper crucially rely"** | D. Kush, ECCC TR26-043 [PREPRINT; status uncertain] | yes (abstract + change note) |
| X5 | Meta-mathematics of algebraic lower bounds. Rank-method lower bounds (e.g. Limaye–Srinivasan–Tavenas, Forbes) are formalizable in VNC² and thus in quasi-poly Frege. PCR cannot efficiently prove superpolynomial algebraic lower bounds for any family. If the "Tensor Rank Principle" is hard for constant-depth IPS, then constant-depth IPS cannot prove constant-depth algebraic lower bounds | M. Garlik, S. Gryaznov, J. Lu, R. Santhanam, I. Tzameret, ECCC TR26-277 / arXiv 2610.33938 (26 Oct 2026) [PREPRINT] | yes |
| X6 | Functional lower bound method (IPS) limitation: it "cannot lead to proof complexity lower bounds for any hard Boolean instance (e.g. CNFs) for any sufficiently strong proof systems" | T. Hakoniemi, N. Limaye, I. Tzameret, ECCC TR24-079 | yes |
| X7 | Rank-type limits in communication complexity. The Log-Approximate-Rank Conjecture is false: a total XOR function with O(n²) approximate rank has Ω(√n) randomized CC (CMS18). Two conjectured routes to log-rank for XOR functions are refuted (HHLO23) | A. Chattopadhyay, N. Mande, S. Sherif, ECCC TR18-176; H. Hatami, K. Hosseini, S. Lovett, A. Ostuni, ECCC TR23-203 | yes |
| X8 | Unprovability barriers in bounded arithmetic. APC₁ cannot prove strong average-case separations of Π₃-SIZE[n^d] from Σ₃-SIZE[2^{n^δ}] (LO23). IS¹₂ does not prove that SAT needs co-nondeterministic circuits of size n^k for some k (CLO24). For every k some L ∈ P is consistent with PV as L ∉ SIZE(n^k) (KO17) | J. Li, I. C. Oliveira, ECCC TR23-022; L. Chen, J. Li, I. C. Oliveira, ECCC TR24-083; J. Krajíček, I. C. Oliveira, ECCC TR16-071 | yes |
| X9 | Rudich's conjecture (no NP-constructive natural properties against P/poly) ⇒ Fortnow–Santhanam's Oracle Derandomization Hypothesis is false; a single non-uniform proof complexity generator is secure against all proof systems; non-uniform non-interactive ZK with perfect soundness | R. Ilango, ECCC TR25-190 [PREPRINT] | yes |
| X10 | Demi-bits generators ⇒ Avoid is hard for nondeterministic algorithms. Demi-bits secure against AM ⇒ dWPHP is unprovable in PV₁, separating APC₁ from PV₁. Pseudo-surjective proof complexity generators follow. Many proof complexity generators sit inside one demi-bits generator | H. Ren, Y. Wang, Y. Zhong, ECCC TR25-191; X. Li, H. Ren, Y. Zhong, ECCC TR26-196 [PREPRINT] | yes |
| X11 | Relativization, 2026 results. There is an oracle with BQP ⊄ IP, so prover-efficient classical IPs for BQP need non-relativizing techniques (also the first IP vs MIP oracle separation). There is a recursive oracle O and a unary language in EQP^O \ (IP^O ∪ PH^O). For promise problems, "results for languages need not transfer to promises": there is an O with P^O = BQP^O but PromiseBQP^O ⊄ PromiseP^O/poly | A. Bouland, A. Huang, A. Natarajan, I. Shalit, A. Tal, arXiv 2609.25680; S. Oral, S. Podder, arXiv 2611.12746; D. Miloschewsky, S. Podder, D. Rudolph, arXiv 2609.07945 [PREPRINTS] | yes |
| X12 | Random-oracle evidence. Relative to a random oracle with O(log n)-bit queries, some function is in O(n) RAM time but needs n²/polylog(n) multitape-TM time | L. Chen, Y. Wang, ECCC TR26-006 [PREPRINT] | yes |
| X13 | A quantum analogue of Razborov–Rudich for state-preparation lower bounds: no natural property proves superpolynomial bounds even against a fixed level of the Magic Hierarchy, under a standard cryptographic assumption | C. Li, N. Parham, arXiv 2610.06826 (5 Oct 2026) [PREPRINT] | yes |
| X14 | Witness-isolation barriers. Any fixed positive success probability for a pruning procedure ⇒ NP ⊆ P/poly, with no cryptographic assumption (TR26-246). Under iO + OWFs no isolator reaches a/log L (TR26-201). Near-inverse-linear barriers for explicit affine isolation (arXiv 2610.11432) | S. Ben Daniel, ECCC TR26-246, TR26-201; arXiv 2610.11432 [PREPRINTS] | yes |
| X15 | Limits of the Oct-2026 ETH-refuting technique: the rewrite-and-merge class, clause-product interpolation, single contraction trees, and the "pieces" exponent cap ρ ≥ 1/2 | see `survey/01-eth-refutation.md` §2.4 and KNOWN_RESULTS.md [method-limits]. Not duplicated | (in 01) |
| X16 | Natural-proofs limits at near-linear size | Miles–Viola and Raz 2026 are already in KNOWN_RESULTS. In addition, Chen–Li–Yang (H9) give PRFs computable by POLYLOGTIME-uniform AC⁰[2] circuits with 2n + o(n) wires, assuming sub-exponential hardness of factoring, DDH or RLWE. What this implies for natural proofs at size 2n is the lab's question; the parameters are not checked (`conjecture`) | yes (CLY22 abstract) |

### 2.10 Explicit Oct–Nov 2026 search: area-04 items found (all [PREPRINT])

- 5 Oct, arXiv 2610.06826: natural proofs for quantum state preparation (X13).
- 12 Oct, ECCC TR26-249 / arXiv 2610.16535: Goldberg, Nanashima, Oliveira, "Learning, Compression, and Meta-Complexity" (survey).
- 13 Oct, ECCC TR26-253 / arXiv 2610.19162: average versus worst case for PH (W5).
- 14 Oct, ECCC TR26-290 / arXiv 2610.20188: symmetry of information for nondeterministic computations (O19).
- 26 Oct, ECCC TR26-277: meta-mathematics of algebraic complexity (X5).
- 6 Nov, arXiv 2611.09020: D. Myrisiotis, "Reconfiguration of Time-Bounded Descriptions". Connectivity of the graph of short programs; PSPACE-completeness of connectivity for a constructed adjunction-universal machine.
- 9 Nov, arXiv 2611.12746: EQP ⊄ IP relative to an oracle (X11).
- 18 Nov, arXiv 2611.25046: S. Ben-David, M. H. Ebtehaj, "The Metacomplexity Structure of Search Problems". Refutation tasks are Heyting arrows. For every verifiable search problem S, either S ∈ (FP/poly)_io or its refutation task is.
- 19 Nov, ECCC TR26-322 and TR26-333: ZK and WI imply meta-complexity hardness (O16, O17).
- Related, not specific to this area: ECCC TR26-313 / arXiv 2611.07972 (Chukhin et al.) and TR26-328 (Karp–Lipton). Both are in KNOWN_RESULTS. Hexagon (hexagonmath.org) searches for "Kolmogorov" and "P vs NP" found nothing relevant. OpenAI's release index (CONTENTS.md, items numbered up to 378) has **no** meta-complexity, magnification or barrier item. Its nearest items, #103 (L = RL = BPL) and #108 (a cubic permanent–determinant lower bound), are out of scope.
- **Not found** in Oct–Nov 2026: NP-hardness of MCSP, MINKT or MFSP; a closed magnification gap; a refutation of a classical barrier; a new GCT no-go.

---

## 3. Key techniques and the barriers they hit or evade

| Technique | Used in | Hits | Evades / why |
|---|---|---|---|
| **Diagonalization + nontrivial circuit-SAT algorithm** (Williams' algorithmic method) | NEXP, NQP ⊄ ACC⁰; E^NP ⊄ THR∘THR[n^{2.5−ε}] (02) | Must produce *constructive* useful properties (B4). Relativizing variants are limited by oracles (X3). Conclusions land in big classes (02) | **Relativization and algebrization:** oracles with NEXP^Ã ⊂ ACC^A exist, and "all known improved SAT algorithms break down when oracles (or algebraic extensions) are added" (Williams 2014). **Natural proofs:** by diagonalization through Succinct-3SAT completeness, i.e. via *non-largeness*. Williams himself says it "is hard to formally rule out that a proof cannot possibly be made natural" |
| **Arithmetization / IP / PCP** | IP = PSPACE, MIP = NEXP, MA_EXP ⊄ P/poly, promise-MA ⊄ SIZE(n^k) | **Algebrization** (B5, X1; half-exponential for MA_E per X1) | Relativization |
| **Random restrictions, shrinkage, pseudorandom restrictions** (for MCSP: HS17, CKLM19, CJW20) | L2, L3, frontier B4/C4/D4 | **Locality** (CHOPRS Thm 2 B4^O, Thm 59, §5.1–5.2). **Natural proofs**: switching-lemma proofs are AC⁰-natural (X2) | — |
| **Polynomial approximation, coin problem** (Razborov–Smolensky; GII+19) | MCSP ∉ AC⁰[p] (L1); frontier A3 | Natural (the rank property is P/poly-natural; cslib proves a 173·8^n-gate test); **localizable** (Pich 2022; CHOPRS Prop. 39) | — |
| **Hashing / compression to short fingerprints** (sparse-language magnification; distinguisher matrices) | H8, H9, H11 | **Locality**: every 2^{n^{o(1)}}-sparse problem has n^{2+o(1)} probabilistic formulas with n^{o(1)}-fan-in oracle gates (Atserias–Müller Cor. 23) | **Natural proofs**: CHOPRS Thm 1 makes some instances *equivalent* to the non-existence of natural properties. Atserias–Müller's uniform variant seems to sidestep locality |
| **Merge trees / anti-checkers with Σ₃SAT oracles** (MMW19; OPS19) | H1–H5 | **Locality** (CHOPRS Prop. 63 bullets; cslib formalizes the MMW and OPS bullets). The Anti-Checker Hypothesis is false (H18) | — |
| **Non-black-box worst-to-average reductions** (K^t, hitting-set generators, NW reconstruction) | W1–W5 | Robust reductions DistNP → GapMINKT fail relative to an oracle (N7). The worst-case mild-gap reduction must be non-relativizing (W5) | **Bogdanov–Trevisan / Feigenbaum–Fortnow** (B11): non-black-box, and from a problem believed outside coNP |
| **Cryptography inside reductions** (witness encryption, iO, NIWI, CS proofs, proofs of work) | M1–M3, M13 | Assumption-heavy. Quasi-polynomial time (M1) | **Mazor–Pass Levin barrier** (N5) by non-Levin (M1) or half-Levin (M13) reductions. **Murray–Williams local-reduction barrier** (N1) by quasi-poly or randomized reductions |
| **Gap CMMSA / partial-function gadgets** (Hirahara 2022; Hirahara–Nanashima 2026) | M4, O15 | Only partial functions or approximate learning MDL | **Ko's relativization barrier** (P9): "provably non-relativizing" |
| **Symmetry of information, coding theorems, pK^t / rK^t** | O7, O11–O13, O18–O20 | Worst-case SoI for pnKt would imply coNP ⊄ AM (O19), so it is hard to prove | — |
| **Gate elimination** (02) | B2 4n, U2 5n | Technique-specific < 5n limits (02); locality: not analysed by CHOPRS (as in 02) | Natural proofs only partly: affine dispersers for dimension O(log n) have no known P-constructive test (02, MS26) |
| **GCT occurrence obstructions** | det vs padded permanent | **BIP19 no-go** (n ≥ m^{25}); IP17 | Multiplicity obstructions are not ruled out (BIP19 §1(c)) |
| **Rank methods** (algebraic, communication) | mABP, multilinear formulas; CC | LARC false (X7); min-partition rank (X4, gap flagged); VNC² formalizability (X5) | — |
| **Lifting** | monotone, KRW (02); hardness of monotone learning (P3) | No general lifting barrier was verified in this survey; deferred to the batch-3 communication/KRW scout | — |
| **Bounded-arithmetic formalization** | provability of lower bounds | Unprovability results (X8) are meta-barriers | — |

**Why each barrier does or does not bite on the lab's likely tools (summary).**
1. Any purely simulation- or diagonalization-based argument for P ≠ NP or NP ⊄ SIZE(n) relativizes. It is blocked by BGS, and for NP ⊄ SIZE(n) by Wilson's oracle (02:K3).
2. Any arithmetization-plus-diagonalization argument for NP ⊄ SIZE(n), NEXP ⊄ P/poly or P ≠ NP is blocked by algebrization (B5). For BPE and PostBPE linear-size bounds see X1.
3. Any argument that yields an efficiently testable, dense property against P/poly is blocked by natural proofs if PRGs exist (B2). Against TC⁰ and size n·polylog n, see Miles–Viola in the registry. Against AC⁰ it is blocked unconditionally above 2^{n^{7/(d−5)}} (X2).
4. Any magnification route whose required lower bound would be proved by a technique that works with small-fan-in oracles is blocked by locality (B8).
5. GCT via occurrence obstructions is blocked (B10).

---

## 4. Open sub-problems ranked by tractability × impact

Scores are 1–5. T is tractability *for this lab now* (AI-assisted, Lean-capable, with ≤ 4 agents per run). I is impact.
Each entry names a source stating the problem open and gives the newest progress I found. I checked each problem
against the Oct–Nov 2026 listings (§2.10) and the cslib-frontier issues (§7). None is claimed solved as of 2026-11-23.

| Rank | Problem | T | I | T×I | Why (one line) | Open per | Last progress |
|---|---|---|---|---|---|---|---|
| 1 | **Lean 4 formalization of the algebrization barrier.** Statement: Def. 2.3; Thm 5.1/5.2-type: ∃(A,Ã) with NP^Ã ⊆ P^A via a PSPACE-complete A and its multilinear extension; Thm 5.3-type: ∃(A,Ã) with NP^A ⊄ P^Ã via algebraic query lower bounds; ideally the circuit form Thm 5.6, NTIME^Ã(2^n) ⊂ SIZE^A(n). The key steps are Babai–Fortnow–Lund's fact that the multilinear extension of a PSPACE language is in PSPACE (used for Thm 5.1) and an algebraic query lower bound (Thm 5.3). Build on cslib's oracle library (`baker_gill_solovay`, TQBF completeness) and its new low-degree extension module (PR #6151, merged 17 Nov 2026) | 4 | 3 | 12 | First machine-checked algebrization barrier. Feeds every lab barrier audit (CLAUDE.md rule 2) and mission item 4. The ingredients already exist in cslib | Not formalized anywhere I found: cslib has no algebrization file, and searches find no algebrization issue or PR (§7, §10); its roadmap only says "barriers such as natural proofs and algebrization". The konard/p-vs-np README cites AW09 but formalizes no barrier | math: CHR25 (Nov 2025). Lean: PR #6151 (17 Nov 2026, low-degree extension building block) |
| 2 | **Is the Oct-2026 AC⁰ frontier AC⁰-natural, and can the LSTU barrier exponent 7/(d−5) be pushed toward 1/(d−1)** (or made non-trivial at small depth, d ≤ 12, where 2^{n^{7/(d−5)}} ≥ 2^n is vacuous)? | 3 | 3 | 9 | Would show switching-lemma-type proofs are optimal up to constants in the exponent. Directly relevant to the 2026 AC⁰ records (02:A1–A4) and to whether they can be pushed further | LSTU abstract: the barrier is "in the same quantitative regime as the SL frontier which instead has 1/(d−1)" | Jun 2026 (LSTU); AC⁰ records Sep–Oct 2026 (02) |
| 3 | **A general *uniform* magnification theorem for all 2^{n^{o(1)}}-sparse NP problems**, and/or **a constructive proof of Santhanam–Williams' P ⊄ P-uniform-SIZE[n^c] exhibiting an explicit hard problem in P** (Atserias–Müller's two questions) | 3 | 3 | 9 | The uniform route (H7) is the only magnification route said to "sidestep" locality. A general version would show this evasion is robust | Atserias–Müller arXiv 2503.24061 §1.5 ("This motivates two questions ...") | Jun 2025 (v2) |
| 4 | **Repair or refute Kush's mABP barrier**: does a full-rank multilinear polynomial have polynomial-size mABPs, i.e. is N(n) = n^{O(1)} for 1-balanced-chain set systems? | 3 | 3 | 9 | A concrete combinatorial claim whose proof is publicly flagged as having a gap. The original question is from Fabris–Limaye–Srinivasan–Yehudayoff (ECCC 2026). Algebraic scope, so hand it to the algebraic scout | TR26-043 change note (11 May 2026) | May 2026 |
| 5 | **Re-base the ETH-conditional meta-complexity hardness results on hypotheses that survive the Oct-2026 refutation**: MCSP\* (N^{Ω(log log N)}), MFSP ∉ P, MBPSP\*, rETH-hardness of monotone learning and approximation (P3). Candidates: Szeider's k×k Clique Hypothesis (no 2^{o(k log k)}L^{O(1)} algorithm), the MIT-HG SH framework (which degrades 2^{o(k log k)} to 2^{O(k^{1−ε})}, too weak for these quasi-polynomial bounds — `informal-argument`), or NP-hardness where it exists (M4) | 4 | 2 | 8 | Cheap, publishable cleanup. The cslib-frontier library proves *both* `not_ETH` and `ETH → MCSP* lower bound`, so its formal MCSP\* theorem is vacuous (T11) | MITHG26 §3 notes the k×k Clique limitation. X. Li's survey of learning (Hexagon 2610.00613, Claude-written) does not cover MCSP or monotone learning. No meta-complexity re-basing found | 16 Nov 2026 (MITHG v2); 19 Nov 2026 (Molter, FPT ≠ W[1]) |
| 6 | **Worst-case mild-gap reduction for MINpKT^PH** (equivalent to "DistPH ⊆ AvgBPP ⇒ PH ⊆ BPP"); it must be non-relativizing | 2 | 4 | 8 | A crisp, purely meta-computational reformulation of a central average-case question | GHLLO TR26-253 (13 Oct 2026); TR25-215 | Oct 2026 |
| 7 | **Lean formalization of the CHOPRS locality barrier**: Thm 59 + Cor. 61 (Anti-Checker Hypothesis false), the remaining Prop. 63 bullets ([AK10], [LW13], [OS18] k-VC, [OPS19] Gap-MKtP), Thm 1 equivalences | 3 | 3 | 9 → **6** after a duplication discount | Valuable, but cslib is actively on it. Contribute there rather than duplicate | cslib PR #4512 roadmap entry (merged 11 Nov 2026); #798 comment: "statable on main but not provable" yet; it needs exponent-2 shrinkage under k-wise independent restrictions and HS17 | 11 Nov 2026 (cslib M5.5 milestones A–C landed) |
| 8 | **Worst-case symmetry of information for pnKt / nKt**: prove it (⇒ coNP ⊄ AM) or refute it | 2 | 3 | 6 | Natural next step after O18/O19; both outcomes are informative | GHLLO TR26-290, TR25-215 | 14 Oct 2026 |
| 9 | **Algebrization barrier for full MA_E at super-half-exponential size**, or an MA_E lower bound beyond half-exponential by non-algebrizing means | 2 | 3 | 6 | X1 handles only a natural subclass. Settles where arithmetization stops | CHR25 abstract ("suggests that half-exponential might be the correct barrier") | Nov 2025 |
| 10 | **NP-hardness of MCSP**: remove or weaken the three assumptions of HI25, make the reduction polynomial-time, or make it many-one | 1 | 5 | 5 | The headline problem. Even one fewer assumption would be notable | TR26-091 §1 (Jun 2026) lists exactly these questions | FOCS 2025 (HI25); Jun 2026 (GJK26) |
| 11 | **Close a CHOPRS/CJW/AM frontier gap with a non-localizing technique**. Examples: frontier D, MCSP[2^{√n}] vs GapAND-Formula, N^{1.99} → N^{2.01}; or MCSP[(log n)^c] probabilistic formulas, n^{2−o(1)} → n^{2+ε} | 1 | 5 | 5 | Would give NQP ⊄ NC¹ or NP ⊄ Formula[n^k]. Locality says the known methods cannot do it | CHOPRS §1.4 (Q2/Q3); CJW20; AM25 | none since Jun 2025 (AM25) |
| 12 | **Close the Pessiland gap** (ℓ^{1−o(1)} vs O(ℓ) for agnostic-learning MDL) | 1 | 5 | 5 | Would base OWFs on average-case NP hardness. The "small gap" phrasing understates the difficulty | TR26-052 (rev. 23 Jun 2026) | Jun 2026 |
| 13 | **OWFs from plain worst-case hardness of K^t** (drop "boundary" and the derandomization assumption), or from NP ⊄ BPP | 1 | 5 | 5 | The cryptographic "holy grail" in meta-complexity form | LP25 (TR25-125/202); LMP26 (TR26-051) | Apr 2026 |
| 14 | **NP-hardness of improper PAC learning of P/poly** (unconditional) | 1 | 5 | 5 | Long-standing. Only semi-proper (GK25) and assumption-based (GJK26) versions are known | GK25 abstract ("partial progress toward the ultimate goal"); GJK26 | Jun–Jul 2026 |
| 15 | **NP-hardness of MINKT (total)** (Ko 1991) | 1 | 4 | 4 | Settled only for nondeterministic and partial versions (M11, M4) | HLO TR25-203 ("A longstanding open problem"); the cslib roadmap lists it as "open and not planned" | Jul 2026 (HLO rev.) |
| 16 | **Kolmogorov's chain-rule ⇔ P = NP without the NP-hardness assumption on GapMcK^tP** | 1 | 4 | 4 | Would make Kolmogorov's suggestion a theorem | Kabanets–Kolokolova TR25-089 (rev. Mar 2026) | Mar 2026 |

---

## 4A. Live competition (who is visibly working on each open problem now)

| Open problem (rank) | Visible activity (names seen on 2025–2026 papers, issues or PRs) |
|---|---|
| 1 Lean algebrization | **None found.** cslib-frontier has related infrastructure (PR #6151 low-degree extension, 17 Nov 2026; the oracle library) but no algebrization issue or PR (GitHub searches, 23 Nov 2026). Its roadmap line on barriers is generic. Moderate risk that a cslib agent picks it up; check before starting |
| 2 AC⁰-natural barrier | LSTU authors (Loff, Sherif, Talebanfard, Ugazio), Jun 2026. AC⁰ frontier work by Chukhin, Li–Zhong, Korten, Kardeş–Rossman (arXiv 2609.01759, Sep 2026: top-down "Chopping Game" and k-local variants) |
| 3 Uniform magnification | Atserias, Müller (2025). No 2026 follow-up found |
| 4 Kush mABP barrier | Kush (Apr–May 2026); Fabris–Limaye–Srinivasan–Yehudayoff (ECCC 2026, cited there; not opened) |
| 5 ETH re-basing | General: MIT Hardness Group (arXiv 2611.02650, 2–16 Nov 2026); Molter (arXiv 2611.26080, 19 Nov 2026); Lampis (cstheory.SE answer 57313, 27 Oct 2026, per MITHG26); Szeider (k×k Clique Hypothesis, cited by MITHG26 as [Sze26], not opened); X. Li / Claude (Hexagon 2610.00613, learning). **None covers MCSP\*, MFSP, MBPSP\* or monotone-learning hardness** |
| 6, 8 PH avg/worst, SoI | Goldberg, Hu, Lu, Lyu, Oliveira (Warwick group; Oct 2026); Hu, Manor, Oliveira (Feb 2026); Kabanets, Kolokolova |
| 7 Lean locality barrier | **cslib-frontier #798 / #4430 / #4512** (owner SamuelSchlesinger; AI coordinator agents). Milestones A–C (#4437, #4441, #4458) landed 11 Nov 2026; Thm 59/Cor. 61 remain |
| 9 MA_E algebrization | Chen, Hu, Ren (ITCS 2026) |
| 10 MCSP NP-hardness | Hirahara, Ilango (FOCS 2025); Goldberg, Juvekar, Kabanets (Jun 2026); Mazor, Pass (rev. May 2026); Huang, Ilango, Ren (SICOMP 2025) |
| 11 Magnification gaps | No 2026 paper found. An unrefereed Zenodo series ("Starflower Inheritance III", record 19243722, Mar 2026) claims a route via negation-width reductions; not evaluated |
| 12 Pessiland | Hirahara, Nanashima (Apr/Jun 2026); Liu, Mazor, Pass (Apr 2026); Arnon, Mazor, Pass, Silbak (Nov 2026) |
| 13 OWF from worst-case | Liu, Pass (2025); Liu, Mazor, Pass (2026); Hirahara, Lu, Oliveira |
| 14 Learning NP-hardness | Goldberg, Kabanets (2025); Goldberg, Juvekar, Kabanets (2026); Cavalar, de Rezende, Gray, Santhanam (Jul 2026); Liu, Mazor, Pass |
| 15 MINKT | Hu, Lu, Oliveira (rev. Jul 2026). cslib: total MINKT/MINcKT NP-hardness "open and not planned" (roadmap/models.md) |
| 16 Chain rule | Kabanets, Kolokolova (Mar 2026); Hirahara, Nanashima ("algorithmic proof of a chain rule", TR25-092 rev. Apr 2026) |

---

## 5. Known traps (approaches known to fail or be blocked, with the citation)

- **T1. Relativizing proofs of P ≠ NP, of NP ⊄ SIZE(n), or of meta-complexity statements.**
  - BGS (B1).
  - Wilson's oracles (02:K3) and AW09's oracle with EXP^{NP} ⊂ P^A/poly.
  - For meta-complexity: Ren–Santhanam's relativized worlds (N7) and Ko's barrier for learning (P9).
- **T2. Arithmetization-based proofs of superlinear circuit lower bounds for NP, NEXP ⊄ P/poly, or P vs NP.**
  - Algebrization (B5: NP^Ã ⊂ SIZE^A(n); NTIME^Ã(2^n) ⊂ SIZE^A(n)).
  - For PostBPE and BPE linear size, and for MA_E beyond half-exponential: X1.
- **T3. Dense, efficiently testable properties against P/poly or TC⁰.**
  - Natural proofs (B2) and Miles–Viola (registry).
  - Against AC⁰, unconditional above 2^{n^{7/(d−5)}} (X2).
  - "My property has quasi-polynomially small density, so I evade RR" is cheap and proves nothing. Chow (B3) exhibits such properties under RR's own assumption.
- **T4. "Avoiding constructivity" for NEXP-type lower bounds.**
  - Impossible: NEXP ⊄ C ⇔ a constructive useful property against C exists (B4).
  - Evade *largeness* instead.
- **T5. Magnification plus a technique that tolerates small-fan-in oracles.**
  - Blocked by locality (B8).
  - Random restrictions, shrinkage and pseudorandom restrictions localize (CHOPRS Thm 2, Thm 59, §5).
  - The approximation method localizes (H20).
  - Reductions from InnerProduct to frontier-B MCSP cannot exist (CHOPRS §1.3).
- **T6. Building on the Anti-Checker Hypothesis (OPS19).** It is false (H18).
- **T7. NP-hardness of MCSP via restricted reductions.** Each is blocked or forces a breakthrough:
  - local or projection reductions (N1);
  - oracle-independent reductions (N2);
  - Levin reductions for Gap-MCSP (N5);
  - honest non-adaptive randomized reductions to ω(log n)-approximate K (N3);
  - n^δ-additive K^t with fast reductions (N4);
  - poly-time reductions (N1 ⇒ EXP ≠ ZPP);
  - Turing reductions (⇒ EXP ⊄ P/poly; Saks–Santhanam CCC 2020; checked: no).
  - Worst-case hardness of Gap_pMK^tP yields a hard disjoint NP pair (N6).
- **T8. Black-box worst-to-average or OWF-from-NP reductions.** Bogdanov–Trevisan (B11), AGGM06 (B12), ABX08 (B13). Use non-black-box methods (W1, O6).
- **T9. GCT occurrence obstructions for det vs padded permanent.**
  - Impossible for n ≥ m^{25}, even against power sums (B10).
  - Rectangular Kronecker vanishing fails as well (B9).
- **T10. Rank-based methods.**
  - LARC is false (X7).
  - Min-partition rank against mABPs is claimed insufficient, but the gap is flagged (X4).
  - Rank-based algebraic lower bounds formalize in VNC² (X5).
- **T11. Building on ETH, rETH, Gap-ETH or SETH conditional meta-complexity results after Oct 2026.**
  - Affected: MCSP\* N^{Ω(log log N)} (M6), MFSP ∉ P (M15), MBPSP\* (M14), W4's ETH item, and the rETH-hardness of monotone learning and approximation (P3, Jul 2026).
  - Their premise is claimed false (01-eth-refutation.md).
  - In cslib-frontier, `ETH.not_decidableInSubexpTime_PartialMCSP (h : ETH)` (`MCSP/PartialETH.lean`) and `not_ETH : ¬ETH` (`FineGrained/CountingNativeEndpoint.lean`) both appear. Grep finds a single `def ETH` (`FineGrained.lean`), so the formal MCSP\* lower bound is vacuous in that library. `informal-argument` (read, not built).
  - Under the MIT-HG SH framework, k×k-type 2^{o(k log k)} bounds degrade to 2^{O(k^{1−ε})} (MITHG26 §3). This appears too weak to keep MCSP\*'s quasi-polynomial bound (`informal-argument`). Szeider's k×k Clique Hypothesis is the stated replacement for such bounds.
- **T12. Over-reading the ETH refutation onto Hirahara's 2021 theorem.**
  - W3's hypotheses are "UP, NP or PH ⊄ DTIME(2^{O(n/log n)})", with n the input length. The Oct-2026 algorithms do
    not contradict them.
  - Those algorithms give NTIME[t] ⊆ DTIME[2^{O(t/√log t)}] (Strassle–Subercaseaux, registry). For languages in
    NTIME[n^k] this is nowhere near 2^{O(n/log n)}.
  - 3-SAT itself was never the witness: a length-n encoding has O(n/log n) occurring variables, so brute force already
    runs in 2^{O(n/log n)}. ETH was not the relevant hypothesis. `informal-argument`.
- **T13. Trusting preprints and claimed barriers without reading revision notes.** In this area:
  - Kush TR26-043: gap in Lemma 4.1.
  - Hirahara–Nanashima TR26-052: Lemma 5.10 flaw, regime restricted.
  - Vyas–Williams: the conference version had an incorrect theorem.
  - Ilango TR23-165: a fixed bug.
  - Mazor–Pass TR24-053: revised May 2026.
- **T14. Confusing problem variants.** MCSP vs partial MCSP vs multi-output MCSP; MINKT vs MINKT\* vs MINcKT vs MINcKT^SAT; K^t vs Kt vs KT vs pK^t vs rK^t vs nKt. Each has a different hardness status (§2.1). An NP-hardness proof for a variant is not one for MCSP.
- **T15. Reading "Lean-verified" as "proved".** See 5A for the 2026 P vs NP artifacts with axioms. In cslib, faithfulness notes such as the MMW specialization (H5) and Liu–Pass's "M2a polynomial-threshold form" (the near-linear t ≥ (1+ε)n regime is *not* formalized) must be read before citing.

### 5A. Failed attempts at P vs NP and recurring error patterns

| Attempt | What was claimed | Why it failed / status | Source | checked |
|---|---|---|---|---|
| Woeginger's list (1986–2016) | 115 tagged entries in my parse: 62 "Equal", 50 "Not equal", 2 "Unprovable", 1 "Undecidable". Last dated entry Sept 2016 | The page's own note: only one paper on the list "has appeared in a peer-reviewed journal ... and whose correctness is accepted": Yannakakis', which "does not settle the P-versus-NP question" but shows an approach fails | G. Woeginger, "The P-versus-NP page", win.tue.nl/~gwoegi/P-versus-NP.htm | yes (page fetched, counts by script) |
| Swart (1986/87) and LP formulations of TSP/HC | Poly-size LPs for Hamiltonian cycle | Yannakakis (1988/91): no poly-size *symmetric* LP. Fiorini–Massar–Pokutta–Tiwary–de Wolf: "no polynomial-size LP whose associated polytope projects to the traveling salesman polytope, even if the LP is not required to be symmetric" (also cut and stable-set polytopes) | Woeginger page; FMPTW, JACM 2015 / STOC 2012, arXiv 1111.0837 | yes (FMPTW abstract); Yannakakis: no (via Woeginger page) |
| Deolalikar (Aug 2010) | P ≠ NP via FO(LFP) and the solution-space structure of random k-SAT | Immerman's note (posted 12 Aug 2010): (1) "it is not true that each stage of the fixed point must be order invariant"; (2) "In this domain—only monadic fixed points and successor—FO(LFP) does not express all of P!" Blog comments (Dawar, Tao, 13 Aug 2010): solution-space arguments must separate k-SAT from XORSAT, which is in P ("proves too much") | R. J. Lipton blog, "Fatal flaws in Deolalikar's proof", 12 Aug 2010 | yes (via WebFetch summary of the post and comments) |
| N. Blum (Aug 2017) | P ≠ NP by extending Berg–Ulfberg's monotone approximation to non-monotone circuits | Tardos's function (monotone, poly-time, exponential monotone complexity) satisfies the method's conditions, so the method would "prove" a false lower bound. Raised in Lipton's blog comments (vloodin, 18 Aug 2017: "Tardos example refutes the proof"), verified 22 Aug 2017. arXiv v2 withdrawn 30 Aug 2017. v3 (Jun 2020) is "the replacement of the incorrect paper" and argues "the approximation method alone cannot be used to prove a super-linear lower bound" | arXiv 1708.03486 (history and comments); Lipton blog 17 Aug 2017 | yes (arXiv); blog via WebFetch |
| Xu–Zhou, "SAT Requires Exhaustive Search" (2023; journal 2025) | Model RB/CSP instances "cannot be solved without exhaustive search ... stronger than P ≠ NP" | Critique: the proof "assume[s] that an algorithm for Model RB must have a certain structure that can leverage downward self-reducibility ... this structure is not guaranteed to exist". Published nonetheless in Frontiers of Computer Science 19(12):1912405 (2025). The authors' reply, arXiv 2401.01193, was not opened | arXiv 2302.09512 (JREF); M. C. Chavrimootoo et al., arXiv 2312.02071 | yes (both abstracts) |
| Dong et al. 2023 (AI) | GPT-4 "produces a proof schema ... throughout 97 dialogue turns, concluding P ≠ NP, which is in alignment with (Xu and Zhou, 2023)" | Inherits the Xu–Zhou flaw. An LLM dialogue is not a proof | arXiv 2309.05689 | yes |
| Arthanari (Jun 2026) | "Lean 4 machine-verified proof of P = NP" via pedigree-polytope membership in strongly polynomial time (STSP reduces to it) | ProofAtlas (status checked 7 Aug 2026): the repository "declares decisive results and one membership-characterization direction as axioms"; not independently audited. Pattern: TSP-polytope approach + axioms in Lean. *Note:* FMPTW rules out poly-size extended formulations, not poly-time membership algorithms per se. I did not analyse whether this argument yields such a formulation | arXiv 2606.03194 (2 Jun 2026); proofatlas.ai/collaboration/p-vs-np | yes (arXiv abstract); ProofAtlas via WebFetch |
| "Mintpath" `p_ne_np` Lean package (Jul 2026) | P ≠ NP "with zero sorries and two axioms" | Axioms; builds only on an older pinned Lean | ProofAtlas (secondary) | no (package not opened) |
| konard/p-vs-np (GitHub, updated Sep 2026) | Educational Lean/Rocq repository; formalizes Swart's attempt | Says "No certified conclusion establishes P = NP or P ≠ NP" and warns that toy-model encodings "should not be read as statements about the Clay problem" | github.com/konard/p-vs-np README | yes (WebFetch) |

**Recurring error patterns** (each tied to an example above):
1. **Restricting the algorithm class.** The argument assumes every algorithm has a particular form, e.g. it exploits self-reducibility (Xu–Zhou), or it proves a lower bound for a restricted model and then claims it for all algorithms.
2. **Proving too much.** The same argument would separate an easy problem: XORSAT (Deolalikar), Tardos's function (Blum), the monotone versus non-monotone gap. Always test the argument on known-easy problems that share the claimed "hard" structure.
3. **Polytope or LP characterizations of TSP and Hamiltonian cycle** (Swart, Arthanari). These hit extension-complexity lower bounds whenever they yield small extended formulations.
4. **Misused logical characterizations.** Descriptive-complexity theorems (Immerman–Vardi) need an order; restricting to monadic fixed points or successor loses P (Deolalikar).
5. **Ignoring the barriers.** Blum's v3 opens with "some reasons that 'natural proofs' built not a barrier". Diagonalization-only arguments relativize (T1).
6. **"Machine-checked" with axioms or toy models** (Arthanari; Mintpath; the konard caution). Run `#print axioms` and check that the statement is the Clay statement.
7. **LLM-generated "proof schemas"** that launder a flawed human argument (Dong et al.). The 2026 version is AI-assisted papers with Lean artifacts. Apply 1–6 regardless of the tooling.

### 5B. Barrier-audit checklist for red-teamers and the barrier-auditor

Apply every item to every proposed argument. Record each answer in the review file.

1. **Statement hygiene.**
   - Fix the model: uniform or non-uniform; circuits, formulas or branching programs; basis B2 or U2 or De Morgan; size measured in gates, wires or leaves.
   - Fix the quantifiers: i.o. or a.e.; worst-case, average-case or zero-error.
   - Fix the class: P, NP, NEXP, E^NP, ...
   - Fix the problem variant (T14).
   - Write the exact claimed bound with constants.
2. **Proves-too-much tests.**
   - Run the argument on XORSAT, 2-SAT, perfect matching, parity, Tardos's function, the Andreev function, random functions, and monotone vs non-monotone versions.
   - If it "separates" any of them, it is wrong.
3. **Relativization.**
   - Does every step hold relative to every oracle (simulation, padding, diagonalization, counting)?
   - If the conclusion is P ≠ NP, NP ⊄ SIZE(n) or P^NP ⊄ SIZE(n), name the non-relativizing step (B1; Wilson's oracles).
   - For meta-complexity steps, compare with Ren–Santhanam's oracle worlds (N7).
4. **Algebrization.**
   - Is the non-relativizing step arithmetization, IP, PCP or low-degree extension?
   - If so, check AW09's list (B5): NP ⊄ SIZE(n), NEXP ⊄ P/poly, P ≠ NP, RP ⊆ P all need non-algebrizing techniques.
   - Also check CHR25 (X1) for PostBPE and BPE linear size, and for MA_E beyond half-exponential.
   - Name the non-algebrizing ingredient. The only known family is algorithm-based (structure-exploiting SAT or CAPP algorithms).
5. **Natural proofs.**
   - Extract the property the proof uses. Is it constructive (decidable from the truth table in P/poly or quasi-poly)? Large (density ≥ 2^{−O(n)})? Useful against the target class?
   - If all three hold, the target class must not contain strong PRFs:
     - P/poly: RR (B2);
     - TC⁰ and size n·polylog n: Miles–Viola (registry);
     - linear functions: Raz 2026 (registry);
     - AC⁰[2] with 2n + o(n) wires: PRFs exist under sub-exponential DDH or factoring (X16, parameters not checked);
     - AC⁰ above 2^{n^{7/(d−5)}}: unconditional (X2).
   - If the property is constructive but not large, check consistency with B4. That is fine: it is how diagonalization evades.
6. **Locality (magnification only).**
   - Does the lower-bound technique still work for the target model extended with oracle gates of fan-in N^{o(1)} or N^ε, at the magnification theorem's quantity and adaptivity?
   - If yes, it is blocked (B8), because the magnified problem has such oracle circuits unconditionally.
   - Exceptions to study: H19 (Thm 49; parity/TC⁰) and the uniform route H7.
   - Do not use the Anti-Checker Hypothesis (T6).
7. **GCT.** Occurrence obstructions for det vs padded permanent are dead (B10, n ≥ m^{25}). Rectangular Kronecker vanishing is dead (B9). Only multiplicity obstructions remain.
8. **Meta-complexity reductions** (claimed NP-hardness of MCSP or MINKT). Identify the reduction type: projection or AC⁰, oracle-independent, Levin, non-adaptive honest randomized, poly-time deterministic, Turing. Then check the matching consequence in N1–N6, which the argument must *also* prove.
9. **Worst-to-average, OWF-from-NP, or learning-from-NP.** If the reduction is black-box and non-adaptive, it collapses PH (B11–B13). Say why the argument is non-black-box.
10. **Unprovability.** Is the argument formalizable in PV, IS¹₂ or APC₁ for a statement known to be unprovable there (X8)? Then it cannot work as stated.
11. **Hypothesis hygiene after Oct 2026.**
    - ETH, SETH, NSETH, #ETH, Gap-ETH, rETH, the Sparse Max-3SAT hypothesis, 3SUM, APSP and k-Clique are claimed refuted (registry).
    - Replace them with SH/Weak ETH (MITHG26), the k×k Clique Hypothesis, OV or CNF-SETH, and recompute the parameters (T11).
12. **Lean hygiene** (CLAUDE.md rule 6).
    - `#print axioms` may list only propext, Classical.choice and Quot.sound.
    - Check statement faithfulness against textbook P/NP (the toy-model warning in 5A).
    - Read every "Faithfulness" or "Model note" block in cslib docstrings, e.g. MMW specializations and the Liu–Pass time-bound note.
13. **Revision hygiene.** Read the ECCC and arXiv revision notes of every cited 2025–2026 preprint (T13).
14. **Novelty and competition.** Check KNOWN_RESULTS.md, this survey's §2, cslib-frontier issues and PRs (#798 family), and ECCC/arXiv for the last 60 days.

---

## 6. People and groups (names seen on the 2024–2026 papers cited above)

- **Meta-complexity, NP-hardness:**
  - Shuichi Hirahara (NII) [M1, M4, O15, W1–W3, M8, M12].
  - Rahul Ilango [M1–M3, M6, M12, X9].
  - Hanlin Ren [M3, X1, X10, B14].
  - Yizhi Huang [M3].
  - Bruno Loff [M12, X2].
  - Halley Goldberg, Mandar Juvekar, Valentine Kabanets [M13, P2, N4].
  - Serge Gaspers, Tao Zixu He, Simon Mackenzie [M12].
  - Ludmila Glinskih, Artur Riazanov [M14].
  - Edward Hirsch, Ilya Volkovich [TR25-220].
- **Kolmogorov complexity, OWFs, SoI:**
  - Yanyi Liu, Rafael Pass, Noam Mazor [O9, O10, O14, N5, N6, U2, U3].
  - Gal Arnon, Jad Silbak [O16, O17].
  - Igor C. Oliveira, Zhenjian Lu, Jinqiao Hu, Jingyi Lyu, Yahel Manor [O18, O19, M11, W5, L6].
  - Mikito Nanashima [O15, O8, P7].
  - Antonina Kolokolova [O20].
  - Marco Carmosino [O21, H6].
  - Stefan Grosser [H6].
  - Rahul Santhanam [O3, O4, N3, P3, X5].
  - Alexey Milovanov [L7].
  - Dimitrios Myrisiotis [arXiv 2611.09020].
  - Shalev Ben-David, M. H. Ebtehaj [arXiv 2611.25046].
- **Learning:** Bruno P. Cavalar, Susanna F. de Rezende, Matthew Gray, Rahul Santhanam [P3]; Ari Karchmer [P8].
- **Magnification and locality:**
  - Albert Atserias, Moritz Müller [H7, H11].
  - Ján Pich [H20, H21].
  - Lijie Chen, Ce Jin, Ryan Williams [H8, H10, H17].
  - Jiatu Li, Tianqi Yang [H9].
  - Roei Tell [H15].
  - Dylan McKay, Cody Murray [H2–H3].
  - Ninad Rajgopal [B8].
- **Barriers:**
  - Yang Hu [X1].
  - Suhail Sherif, Navid Talebanfard, Francesca Ugazio [X2].
  - Nikhil Vyas [X3].
  - Deepanshu Kush [X4].
  - Michal Garlik, Svyatoslav Gryaznov, Jiaqi Lu, Iddo Tzameret [X5].
  - Christine Li, Natalie Parham [X13].
  - Adam Bouland, Andrew Huang, Anand Natarajan, Itay Shalit, Avishay Tal; Sinan Oral, Supartha Podder; David Miloschewsky, Dorian Rudolph [X11].
  - Sebastian Ben Daniel [X14].
  - Christian Ikenmeyer, Greta Panova, Peter Bürgisser [B9, B10] (2016–2019 papers).
- **ETH re-basing:** MIT Hardness Group (Josh Brunner, Erik D. Demaine, Fabian Frei, Timothy Gomez, Markus Hecher, Jeffery Li, Jayson Lynch); Hendrik Molter; Xiaoyu Li (with Claude).
- **Formalization:** Samuel Schlesinger (cslib-frontier #798 owner; the issue is driven largely by AI coordinator agents); Christian Reitwiessner (results inventory).

---

## 7. Formalization status (Lean / Coq / Isabelle)

All cslib-frontier items below are from the local clone (commit 1435284b, 23 Nov 2026) and its GitHub issues and PRs.
I grepped `sorry`, `axiom` and `native_decide` in CslibFrontier/Computability/MCSP (45 files, 17,755 lines), Kolmogorov
(28 files, 7,196 lines), Crypto/Computational/OneWay (15 files, 8,342 lines), Circuit/Boolean/NaturalProof and
Circuit/Boolean/Oracle. Every count was **0**. I did **not** build or run `#print axioms`.

| Result | Formal artifact | Faithfulness notes (from docstrings) | Status |
|---|---|---|---|
| MCSP, GapMCSP, MCSP ∈ NP, partial MCSP, Succinct MCSP, Multi-output MCSP definitions | `MCSP/{Basic,NP,Partial,PartialNP,Succinct,Multi}.lean` | De Morgan circuits counting all gates | grep-clean |
| Partial MCSP NP-hard under randomized reductions (Hirahara 2022, Thm I.2 "In particular") | `MCSP/PartialHardness/Reduction.lean`, `rpHard`, `rpHard_encBinary` | "The construction and its analysis are the library's own" (route B, via GapCMMSA). The gap constant is 8 instead of 4 | grep-clean |
| MINKT\* NP-hard under randomized reductions | `Kolmogorov/MINKTStar/Hardness.lean`, `MINKTStar.rpHard` | Uses steps-of-described-machine K^t, not the source's KT-style measure. The (log N)^ε inapproximability and the distributional forms are not formalized | grep-clean |
| Multi-output MCSP NP-hard (ILO20 Thm 4) | `MCSP/MultiNPHard.lean`, `MultiMCSP.rpHard_pos` | Reduces from the library's GapSetCover 3 rather than Trevisan's bounded set cover | grep-clean |
| Ilango's ETH lower bound for MCSP\* | `MCSP/PartialETH.lean`, `ETH.not_decidableInSubexpTime_PartialMCSP` | **Hypothesis `ETH` is refuted in the same library (`not_ETH`)** (T11) | grep-clean; vacuous |
| Murray–Williams consequences of MCSP NP-hardness (EXP ≠ NP ∩ P/poly, EXP ≠ ZPP) | `MCSP/HardnessConsequences.lean` | Full-NPHard specialization of MW Thm 4.1 | grep-clean |
| Kabanets–Cai: MCSP ∈ BPP ⇒ no OWF | `Crypto/Computational/OneWay/MCSP.lean` | — | grep-clean |
| Liu–Pass Thm 3.1 (a) ⇔ (b) | `Crypto/Computational/OneWay/LiuPass.lean`, `exists_oneWay_iff_exists_mildlyHardOnAverage_timeBoundedNat`; converse in `LiuPassConverse.lean` | "M2a polynomial-threshold form". **The near-linear regime t ≥ (1+ε)n is not formalized** (roadmap item) | grep-clean |
| Hardness magnification: MMW19 (merge tree, P ≠ NP form), OS18 Lemma 16 / Thm 17 / Thm 27, OPS19 anti-checker existence and Lemma 4.1 (#4429) | `MCSP/Magnification.lean` (`P_ne_NP_of_yesSet_hard`), `MCSP/FormulaMagnification*.lean`, `MCSP/AntiChecker*.lean` | MMW specialized to decision MCSP, no oracle, size-only | grep-clean |
| CHOPRS local circuit classes [q, ℓ, a]–C and Prop. 63 bullets for [OS18], [OPS19] Gap-MCSP and [MMW19] | `Circuit/Boolean/Oracle/{LocalClass,LocalCircuit}.lean`, `MCSP/FormulaMagnification/Locality.lean`, `MCSP/Magnification/MergeTree/Locality.lean` | **The locality barrier itself (Thm 59 / Cor. 61) and Thm 1 are not formalized** (PR #4512, roadmap) | partial |
| Natural proofs barrier (RR Thm 4.1-style) | `Circuit/Boolean/NaturalProof.lean`, `not_isUseful_PPoly_of_isNatural`; `.../Generator.lean` via GGM | The security hypothesis is *non-uniform* explicit exponential circuit security of a keyed family, stronger than the textbook's. The factoring and discrete-log consequence is not formalized (results/arora-barak-2007.md §22). The cslib audit also reports that RR's published Thm 5.1(b) has a "missing additive −n loss" relative to AB draft 22.3; I did not check this | grep-clean; partial |
| Razborov's rank property is P/poly-natural (173·8^n-gate test) | `Circuit/Boolean/Razborov/Natural.lean` | Library's own gate count | grep-clean |
| Learners ⇒ natural properties (OS17 (1) ⇒ (5)); CIKK for AC⁰[2] (`cikkLearner`) | `MachineLearning/UniformLearning/CryptoHardness/NaturalProperty.lean`; #4451 | CIKK Thm 5.1 abstract form is open (#4635); non-adaptive circuits (#4634) | partial |
| Baker–Gill–Solovay | `Complexity/Classes/Oracle/Collapse.lean`, `baker_gill_solovay` | Equality oracle = TQBF | (registry) |
| **Algebrization (AW09, IKK09, CHR25)** | **none**. GitHub issue search "algebrization": 0 results. PR search "algebrization OR low-degree extension OR Aaronson": 10 results, none about algebrization. PR #6151 (low-degree extension) is a building block | — | **gap** (open problem 1) |
| Hirahara 2018 non-black-box reduction | building block only: `Kolmogorov/NisanWigderson.lean` (the decoder is a *hypothesis*, `ReconstructionDecoder`) | — | gap |
| Total MINKT/MINcKT NP-hardness | roadmap: "open and not planned" | — | (an open problem) |
| NP-hardness of deterministic CC (GHM) | "Includes a Lean formalization and interactive proof inspector" | not inspected | claimed (arXiv 2508.05597 v6) |
| konard/p-vs-np | Lean 4 / Rocq / Agda; Swart attempt; Isabelle "sunset" | "No certified conclusion" | educational |
| Arthanari P = NP; Mintpath P ≠ NP | Lean artifacts with axioms (per ProofAtlas) | not accepted | — (5A) |
| Other assistants | No Coq or Isabelle formalization of natural proofs, algebrization, locality or meta-complexity hardness found in searches. Isabelle/AFP has a monotone-Clique lower bound (registry) and, per a web-search snippet, a Cook–Levin formalization | — | — |

---

## 8. Known-results registry entries (proposed for research/KNOWN_RESULTS.md)

Format: `- [area] statement — Authors (Year), venue/arXiv — checked:yes/no`. Entries already in the registry (OS18,
OPS19, MMW19, CJW19, CLY22, CHOPRS, AM25, Raz 2026, Miles–Viola, CHR25 and LSTU from crosscheck 02) are not repeated,
except where I add parameters (marked "refines").

- [meta-hardness] MCSP NP-hardness is open; a constant-gap GapMCSP is NP-hard under deterministic quasi-poly (non-adaptive) Turing reductions assuming sub-exponential NIWI for SAT, a.e. sub-exponential nondeterministic circuit lower bounds for coNP, and a.e. δ2^n/n lower bounds for P^NP/poly — Hirahara, Ilango (2025), FOCS 2025 pp. 1648–1664 — checked:no (via ECCC TR26-091)
- [meta-hardness] Partial MCSP (and learning programs) NP-hard under randomized poly-time many-one reductions; provably non-relativizing (overcomes Ko 1991) — Hirahara (2022), FOCS 2022 / ECCC TR22-119 — checked:yes
- [meta-hardness] Multi-output MCSP NP-hard under randomized many-one reductions — Ilango, Loff, Oliveira (2020), CCC 2020 / ECCC TR20-021 — checked:yes
- [meta-hardness] Depth-d formula MCSP (d ≥ 2) NP-hard under quasi-poly randomized reductions; MCSP* ∉ P under ETH [premise claimed false Oct 2026] — Ilango (2020), FOCS 2020 / ECCC TR20-183 — checked:yes
- [meta-hardness] OR∘AND∘MOD₂-MCSP NP-hard (deterministic poly-time many-one) — Hirahara, Oliveira, Santhanam (2018), ECCC TR18-030 (CCC 2018, venue unchecked) — checked:yes
- [meta-hardness] With probability 1 over a random oracle O, P/poly reduction from approximate hypergraph vertex cover to MCSP^O (extends to K^t) — Ilango (2023), FOCS 2023 / ECCC TR23-165 — checked:yes
- [meta-hardness] Unconditional near-optimal NP-hardness of approximating MOCSP; essentially optimal NP-hardness of approximating K^t(x∣y) (t ≫ ∣y∣) under sub-exponential witness encryption — Huang, Ilango, Ren (2023), STOC 2023 / SICOMP 54(4) 2025 / ECCC TR23-046 — checked:yes
- [meta-hardness] MINcKT^SAT NP-hard under deterministic poly-time reductions; EXP^NP ⊆ P^{R_K} — Hirahara (2020), STOC 2020 / ECCC TR20-050 — checked:yes
- [meta-hardness] For t ≥ n², McK^tP[ζ] (RAM programs) is NP-complete; for t ≥ 1.1n, mild average-case hardness ⇔ OWF — Liu, Pass (2021), ECCC TR21-059 — checked:yes
- [meta-hardness] McKTP NP-complete under randomized reductions; average-case hard ⇔ logspace OWFs — Allender, Cheraghchi, Myrisiotis, Tirumala, Volkovich (2021), ECCC TR21-009 — checked:yes
- [meta-hardness] MINnKT ∈ BPP ⇔ NP ⊆ BPP [PREPRINT] — Hu, Lu, Oliveira (2025/26), ECCC TR25-203 — checked:yes
- [meta-hardness] Deterministic communication complexity of a given matrix is NP-hard — Hirahara, Ilango, Loff (2025), ECCC TR25-094 — checked:yes
- [meta-hardness] NP-hard to approximate deterministic CC within any fixed additive error (also Yao's alternating model); Lean formalization claimed [PREPRINT] — Gaspers, He, Mackenzie (2025/26), arXiv 2508.05597 v6 — checked:yes
- [meta-hardness] Gap-ImpMCSP and improper full-support PAC learning NP-hard under randomized half-Levin reductions (not Levin), assuming sub-exponential iO + no i.o. sub-exponentially-optimal proof systems [PREPRINT] — Goldberg, Juvekar, Kabanets (2026), ECCC TR26-091 — checked:yes
- [meta-hardness] Partial MBPSP / read-k / OBDD minimization superpolynomial under ETH [premise claimed false]; NP-hard to decide compressibility of a BP for a partial function — Glinskih, Riazanov (2024), arXiv 2407.04632 — checked:yes
- [meta-hardness] MFSP ∉ P under ETH [premise claimed false] — Ilango (2021), FOCS 2021 — checked:no
- [meta-hardness] n^{1−o(1)}-approximate MCSP/MKTP NP-intermediate if OWFs exist; MKTP ∉ AC⁰[p] — Allender, Hirahara (2017/19), ECCC TR17-073 / ACM ToCT 11(4) 2019 — checked:yes
- [meta-barrier] MCSP not NP-hard under O(n^{1/2−ε})-time projections; AC⁰-reduction NP-hardness ⇒ NP ⊄ P/poly and E ⊄ io-SIZE(2^{δn}); poly-time NP-hardness ⇒ EXP ≠ NP ∩ P/poly (⇒ EXP ≠ ZPP) — Murray, Williams (2015/17), ECCC TR14-164 / Theory of Computing 13 (2017) — checked:yes
- [meta-barrier] Oracle-independent reductions to MCSP essentially reduce nothing; NP-hardness via non-adaptive poly-time reductions ⇒ ZPP ≠ EXP — Hirahara, Watanabe (2016), ECCC TR15-198 (CCC 2016, venue unchecked) — checked:yes
- [meta-barrier] Randomized non-adaptive honest reductions to ω(log n)-approximate K only reach AM ∩ coAM; SAT → ω(log n)-approximate K^t ⇒ NE = coNE or E has sub-exponential nondeterministic circuits i.o. — Saks, Santhanam (2022), CCC 2022 / ECCC TR22-074 — checked:yes
- [meta-barrier] Under derandomization, SAT-hardness of n^δ-additive-approximate K^t under fast honest randomized non-adaptive reductions ⇒ NP = coNP — Goldberg, Kabanets (2024), ECCC TR24-120 — checked:yes
- [meta-barrier] Under iO + sub-exponential OWF, Gap-MCSP is not NP-complete under randomized Levin reductions — Mazor, Pass (2024), ECCC TR24-053 — checked:yes
- [meta-barrier] Gap_pMK^tP ∉ P/poly (+ derandomization) ⇒ a hard disjoint NP pair (barrier to NP-completeness), ZK for NP with an inefficient prover, conditional PRGs [PREPRINT] — Liu, Mazor, Pass (2026), ECCC TR26-051 — checked:yes
- [meta-barrier] Relativized worlds: MCSP ∈ P but search-MCSP ∉ P; Kt (2+ε)-approximable; no natural proofs and no AIOWF; no robust DistNP → GapMINKT reductions — Ren, Santhanam (2021), ECCC TR21-089 — checked:yes
- [meta-lb] MCSP needs depth-d AC⁰[p] size exp(N^{0.49/d}) — Golovnev, Ilango, Impagliazzo, Kabanets, Kolokolova, Tal (2019), ECCC TR19-018 (ICALP 2019, venue unchecked) — checked:yes
- [meta-lb] MCSP needs N^{3−o(1)} De Morgan formulas, N^{2−o(1)} formulas (any basis) and BPs, 2^{Ω(N^{1/(d+2.01)})} depth-d AC⁰ — Cheraghchi, Kabanets, Lu, Myrisiotis (2019), ECCC TR19-022 (ICALP 2019, venue unchecked) — checked:yes
- [meta-lb] MCSP[2^{√n}] ∉ Formula[N^{2−δ}] (worst case) — Hirahara, Santhanam (2017), CCC 2017 — checked:no (via OS18, AM25)
- [meta-lb] MCSP[2^{μ₂n}] ∉ randomized one-tape TM time N^{1.99} (μ₂ > the MMW constant μ₁ for which N^{1.01} ⇒ P ≠ NP); MKTP needs Ω(N^{1.5}/log N) nondeterministic and parity BPs — Cheraghchi, Hirahara, Myrisiotis, Yoshida (2020), ECCC TR20-103 — checked:yes
- [meta-lb] SoS needs degree Ω(s^{1−ε}) to refute that f has size-s circuits; no low-degree SoS proofs of NP ⊄ P/poly — Austrin, Risse (2023), ECCC TR23-010 — checked:yes
- [meta-lb] R_{nKt[γn]} ∉ NTIME[2^{o(n)}] ∩ coNTIME[2^{o(n)}] for 1/2 < γ < 1 [PREPRINT] — Goldberg, Hu, Lu, Lyu, Oliveira (2025), ECCC TR25-215 — checked:yes
- [meta-ub] Every compression problem has 2^{4ℓ/5}·poly(t) circuits; MCSP has circuits 2^{(4/5)w+o(w)}·poly(2^n) — Hirahara, Ilango, Williams (2023), ECCC TR23-171 (STOC 2024, venue unchecked) — checked:yes
- [meta-ub] Non-uniform Perebor false for K^t: circuits 2^{4n/5+o(n)} for every polynomial t; any efficient function invertible by 2^{4n/5+o(n)} circuits — Mazor, Pass (2023), ECCC TR23-175 (ITCS 2024, venue unchecked) — checked:yes
- [avg-worst] Average-case MINKT easy (errorless) ⇒ approximate MINKT within additive Õ(√k) in ZPP; non-black-box, bypassing Bogdanov–Trevisan — Hirahara (2018), FOCS 2018 / ECCC TR18-138 — checked:yes
- [avg-worst] DistPH ⊆ AvgP ⇔ GapMINKT^PH ∈ P; GapMINKT^NP ∈ P ⇒ P = BPP — Hirahara (2020), ECCC TR20-143 (FOCS 2020, venue unchecked) — checked:yes
- [avg-worst] UP ⊄ DTIME(2^{O(n/log n)}) ⇒ DistNP ⊄ AvgP; PH analogue — Hirahara (2021), STOC 2021 / ECCC TR21-058 — checked:yes
- [avg-worst] Avg-vs-worst for PH ⇔ (Gap-MINpKT^PH ∈ prBPP ⇒ Mild-Gap-MINpKT^PH ∈ prBPP); worst-case reductions between them must be non-relativizing [PREPRINT] — Goldberg, Hu, Lu, Lyu, Oliveira (2026), ECCC TR26-253 — checked:yes
- [owf] OWF ⇔ K^t mildly hard on average, for every polynomial t ≥ (1+ε)n — Liu, Pass (2020), FOCS 2020 / ECCC TR20-052 — checked:yes
- [owf] MKtP two-sided average-case hard ⇔ i.o. OWF; errorless average-case hard ⇔ EXP ≠ BPP — Liu, Pass (2021), CRYPTO 2021 / ECCC TR21-056 — checked:yes
- [owf] KT bounded-error average-case hard ⇔ NC⁰ OWFs — Ren, Santhanam (2021), CCC 2021 / ECCC TR21-057 — checked:yes
- [owf] OWF ⇔ hardness of approximating (time-unbounded) K on some samplable distribution — Ilango, Ren, Santhanam (2022), STOC 2022 / ECCC TR21-082 — checked:yes
- [owf] OWF ⇔ (NP-hardness of approximating distributional K under randomized reductions ∧ NP worst-case hard) — Hirahara (2023), STOC 2023 / ECCC TR23-037 — checked:yes
- [owf] OWF ⇔ failure of average-case symmetry of information for pK^t — Hirahara, Ilango, Lu, Nanashima, Oliveira (2023), STOC 2023 / ECCC TR23-035 — checked:yes
- [owf] OWF ⇔ (NP ⊆ CZK ∧ NP worst-case hard) ⇔ (CZK hard ∧ GapMCSP ∈ CZK) — Hirahara, Nanashima (2024), STOC 2024 / ECCC TR24-063 — checked:yes
- [owf] First OWF-complete promise problem (MK^tP on small-computational-depth instances) — Liu, Pass (2023), ECCC TR23-103 — checked:yes
- [owf] Under E ⊄ ioSIZE[2^{o(n)}], OWF ⇔ boundary hardness of K^t; unconditional for pK^t and randomized K^t [PREPRINT] — Liu, Pass (2025), ECCC TR25-125, TR25-202 — checked:yes
- [owf] Pessiland ruled out iff the ℓ^{1−o(1)} vs O(ℓ) approximation gap for agnostic-learning MDL closes; revised (Jun 2026) to large-constant ℓ after a flaw in Lemma 5.10 [PREPRINT] — Hirahara, Nanashima (2026), ECCC TR26-052 — checked:yes
- [owf] Conditional pK^t is NP-hard for sublinear t; NP-hardness for large polynomial t would exclude Pessiland — Lu, Santhanam (2024), ECCC TR24-085 — checked:yes
- [soi] Symmetry of information fails unconditionally for rKt and pKt [PREPRINT] — Hu, Manor, Oliveira (2026), ECCC TR26-021 — checked:yes
- [soi] SoI holds on average for randomized extensions of nKt; worst-case SoI for pnKt ⇒ coNP ⊄ AM [PREPRINT] — Goldberg, Hu, Lu, Lyu, Oliveira (2025/26), ECCC TR25-215, TR26-290 — checked:yes
- [soi] Chain rule for conditional K^t (error o(N)) ⇔ E ⊄ io-SIZE[2^{o(n)}] ∧ GapMcK^tP ∈ promise-P [PREPRINT] — Kabanets, Kolokolova (2025/26), ECCC TR25-089 — checked:yes
- [owf] Two-message arguments with an inefficient simulator ⇒ errorless average-case hardness of MKtP [PREPRINT] — Arnon, Mazor, Pass, Silbak (2026), ECCC TR26-322 — checked:yes
- [learning] Semi-proper agnostic learning (size s by size s·n^{1/(log log n)^{O(1)}}) NP-hard; witness encryption ⇔ half-Levin reduction to CGL — Goldberg, Kabanets (2025), ECCC TR25-070 — checked:yes
- [learning] Under rETH [claimed false]: learning monotone formulas needs n^{Ω(log n)} time; m^{1−δ}-approximating monotone circuit size needs m^{Ω(log m)} [PREPRINT] — Cavalar, de Rezende, Gray, Santhanam (2026), ECCC TR26-128 — checked:yes
- [learning] Natural properties ⇒ learning and compression; quasi-poly learning of AC⁰[p] — Carmosino, Impagliazzo, Kabanets, Kolokolova (2016), CCC 2016 / ECCC TR16-008 — checked:yes
- [magnification][refines] Gap-MCSP threshold of OPS19 is Gap-MCSP[2^{βn}/(cn), 2^{βn}] ∉ Circuit[N^{1+ε}] for every small β; Gap-MKtP thresholds TC⁰[N^{1+ε}], B2-Formula[N^{2+ε}], U2-Formula[N^{3+ε}], BP[N^{2+ε}], AC⁰[6][N^{1+ε}] ⇒ EXP lower bounds — Oliveira, Pich, Santhanam (2019), CCC 2019 / ToC 17(11) 2021 — checked:yes
- [magnification][refines] MMW19 Thm 1.3: no poly(s)-space, poly(s)-update streaming algorithm for search-MCSP^A[s], A ∈ PH ⇒ P ≠ NP — McKay, Murray, Williams (2019), STOC 2019 pp. 1215–1225 — checked:yes
- [magnification] Magnification frontiers A–E with thresholds vs known bounds (e.g. MCSP[2^{√n}] vs GapAND-Formula: N^{1.99} known, N^{2.01} needed ⇒ NQP ⊄ NC¹) — Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam (2020), ITCS 2020 / JACM 69(4):25 — checked:yes
- [barrier] The Anti-Checker Hypothesis (OPS19) is false (CHOPRS Thm 59/Cor. 61) — CHOPRS (2020) — checked:yes
- [barrier] One lower bound above a magnification threshold is non-localizable: L ∈ E with L ∉ GapAND-Formula[N^{3−ε}] but L ∈ O_{N^{o(1)}}-Formula[N²] — CHOPRS (2020), Thm 49 — checked:yes
- [magnification][refines] Atserias–Müller Thm 9: n^{−ε}-Q ∉ FML[n^{1+2ε+o(1)}] or ∉ PFML[n^{2ε+o(1)}] for sparse Q ∈ NP ⇒ NP ⊄ FML[n^c]; Thm 10 sharp: n^{−ε}-MCSP[2^{√ℓ}] ∉ PFML[n^{2ε−δ}]; Thm 11: n^{−ε}-MCSP[σ] ∉ P-uniform-SIZE[n^{1+ε+o(1)}] ⇒ P ≠ NP^{⊕P} — Atserias, Müller (2025), arXiv 2503.24061 — checked:yes
- [magnification] TC⁰ wire bounds n^{1+c^{−d}} for NC¹-complete functions, for all c > 1, ⇒ TC⁰ ≠ NC¹; known for c ≈ 2.41 — Chen, Tell (2019), STOC 2019 / ECCC TR18-199 — checked:yes (already in registry under [threshold])
- [magnification] Approximation-method lower bounds are localizable, so they cannot be magnified to NC¹ bounds for explicit functions — Pich (2022), arXiv 2212.09285 — checked:yes
- [magnification] Under the witnessing-formula hypothesis, super-polynomial EF + w_n^k(f) lower bounds ⇒ SAT ∉ P/poly — Pich, Santhanam (2023), ECCC TR23-199 — checked:yes
- [magnification] Uniform AC⁰[qpoly] Student–Teacher generation of hard truth tables ⇒ P ≠ NP; a P-ST constructive separation of Palindromes from one-tape nondeterministic n^{1+ε} time ⇒ NP ⊄ SIZE[n^k] [PREPRINT] — Carmosino, Grosser (2025), ECCC TR25-045 — checked:yes
- [barrier] Algebrization definitions and oracles: NP^Ã ⊆ P^A; NP^A ⊄ P^Ã; NTIME^Ã(2^n) ⊂ SIZE^A(n); NP^Ã ⊂ SIZE^A(n); EXP^{NP^Ã} ⊂ P^A/poly; BPEXP^Ã ⊂ P^A/poly; algebrizing: PSPACE^A ⊆ IP^Ã, MA_EXP^Ã ⊄ P^A/poly — Aaronson, Wigderson (2009), ACM TOCT 1(1) / ECCC TR08-005 — checked:yes
- [barrier] Williams' ACC⁰ bound avoids relativization and algebrization: oracles with NEXP^A ⊂ ACC^A and NEXP^Ã ⊂ ACC^A (Aaronson, personal communication); evades natural proofs via diagonalization — Williams (2014), JACM 61(1) (acc-lbs.pdf §1) — checked:yes
- [barrier] NEXP ⊄ C ⇔ a P-constructive property useful against C exists; no P-natural property against C ⇔ derandomization of randomized exponential time by C-truth tables — Williams (2013/16), STOC 2013 special issue / arXiv 1212.1891 — checked:yes
- [barrier] Natural-proofs quantitative form: a 2^{k^ε}-hard PRG in SIZE(k^c) ⇒ no P/poly-natural property with density > 2^{−n^d} useful against SIZE(n^e), for e > 1 + cd/ε; almost-natural useful properties of density 2^{−quasi-poly} exist — Chow (2008/11), arXiv 0805.1385, FOCS 2008 extended abstract (restating Razborov–Rudich 1997) — checked:yes (Chow); RR97: no
- [barrier] Axiomatic algebrization: AIV theory + Arithmetic Checkability proves most arithmetization results; many open questions independent — Impagliazzo, Kabanets, Kolokolova (2009), STOC 2009 — checked:yes
- [barrier] Affine relativization unifies relativization and algebrization; AW's algebrizing statements relativize affinely — Aydınlıoğlu, Bach (2016/18), ECCC TR16-040 (journal venue unchecked) — checked:yes
- [barrier] GCT: no occurrence obstructions for det vs padded permanent when n ≥ m^{25} (also against power sums) — Bürgisser, Ikenmeyer, Panova (2019), JAMS / arXiv 1604.06431 — checked:yes
- [barrier] GCT: vanishing rectangular Kronecker coefficients cannot prove superpolynomial dc(perm) lower bounds — Ikenmeyer, Panova (2017), arXiv 1512.03798 — checked:yes
- [barrier] Non-adaptive self-correctors for NP-complete problems ⇒ coNP ⊆ NP/poly (PH collapses to Σ₃) — Bogdanov, Trevisan (2003/06), ECCC TR05-015 (journal venue unchecked) — checked:yes
- [barrier] PSPACE-relativizing techniques cannot improve IW01, OS17 or pr-MA ⊄ SIZE(n^k) to worst-case or a.e. versions without NP ≠ L; BPE^{MCSP}/2^{εn} ⊄ SIZE[2^n/n] — Hirahara, Lu, Ren (2023), ECCC TR23-070 (CCC 2023, venue unchecked) — checked:yes
- [barrier] VNP has no efficient equations over characteristic 0 if the permanent is exponentially hard; algebraic natural proofs barrier ⇔ succinct hitting sets for VP — Chatterjee, Kumar, Ramya, Saptharishi, Tengse (2020/24); Grochow, Kumar, Saks, Saraf (2017), ECCC TR20-063, TR17-009 — checked:yes
- [barrier] Rank-method lower bounds (LST25, Forbes) formalizable in VNC²; PCR cannot efficiently prove superpolynomial algebraic lower bounds [PREPRINT] — Garlik, Gryaznov, Lu, Santhanam, Tzameret (2026), ECCC TR26-277 — checked:yes
- [barrier][uncertain] Min-partition rank cannot give superpolynomial mABP lower bounds (claimed; a gap in Lemma 4.1 was flagged in the 11 May 2026 revision) [PREPRINT] — Kush (2026), ECCC TR26-043 — checked:yes
- [barrier] Rudich's conjecture ⇒ the Oracle Derandomization Hypothesis is false; a universal non-uniform proof complexity generator exists [PREPRINT] — Ilango (2025), ECCC TR25-190 — checked:yes
- [barrier] Oracle with BQP ⊄ IP (so prover-efficient classical IPs for BQP need non-relativizing techniques); EQP ⊄ IP ∪ PH relative to a recursive oracle [PREPRINT] — Bouland, Huang, Natarajan, Shalit, Tal (2026), arXiv 2609.25680; Oral, Podder (2026), arXiv 2611.12746 — checked:yes
- [barrier] Natural-proofs barrier for quantum state-preparation lower bounds [PREPRINT] — Li, Parham (2026), arXiv 2610.06826 — checked:yes
- [barrier] Log-approximate-rank conjecture false (O(n²) approximate rank vs Ω(√n) randomized CC) — Chattopadhyay, Mande, Sherif (2018/19), ECCC TR18-176 — checked:yes
- [barrier] The functional lower bound method cannot give IPS-type lower bounds for hard Boolean instances against sufficiently strong systems — Hakoniemi, Limaye, Tzameret (2024), ECCC TR24-079 — checked:yes
- [unprovability] IS¹₂ does not prove SAT ∉ coNSIZE[n^k] for some k (unconditional) — Chen, Li, Oliveira (2024), ECCC TR24-083 — checked:yes
- [unprovability] APC₁ cannot prove strong average-case Π₃ vs Σ₃ circuit separations — Li, Oliveira (2023), ECCC TR23-022 — checked:yes
- [constructive] Constructive versions of MCSP, streaming and one-tape lower bounds would give EXP ≠ BPP up to P ≠ NP; no constructive separation for detecting high t-time Kolmogorov complexity — Chen, Jin, Santhanam, Williams (2024), TheoretiCS 3 / arXiv 2203.14379 — checked:yes
- [failed-attempts] Woeginger's P-versus-NP page: 115 tagged claims (62 =, 50 ≠, 2 unprovable, 1 undecidable), last dated Sept 2016; only Yannakakis' (non-resolving) paper is accepted — Woeginger (2016), web page — checked:yes
- [failed-attempts] Blum's 2017 P ≠ NP claim withdrawn (arXiv v2, 30 Aug 2017) after the Tardos-function objection; v3 (2020) argues the approximation method alone cannot give superlinear bounds — Blum (2017/2020), arXiv 1708.03486 — checked:yes
- [failed-attempts] "SAT requires exhaustive search" (published 2025) assumes an algorithm structure based on downward self-reducibility that need not exist — Chavrimootoo, He, Kotler-Berkowitz, Liuson, Nie (2023), arXiv 2312.02071 — checked:yes
- [failed-attempts] 2026 "Lean-verified" P = NP (pedigree polytope) relies on repository axioms, per ProofAtlas — Arthanari (2026), arXiv 2606.03194 — checked:yes (abstract); axiom claim: no (secondary)
- [formalization] cslib-frontier formalizes (grep-clean, not built) partial-MCSP and MINKT* NP-hardness (own route-B reduction), multi-output MCSP NP-hardness, Liu–Pass (a) ⇔ (b) (polynomial-threshold form), MMW19 magnification to P ≠ NP (decision, no oracle), OS18 formula magnification, OPS19 anti-checkers, CHOPRS local classes and three Prop. 63 bullets, the RR barrier under non-uniform security, Kabanets–Cai, MW consequences; not formalized: CHOPRS Thm 59/Cor. 61 and Thm 1, algebrization, Hirahara 2018, Liu–Pass near-linear t — cslib-frontier (2026), commit 1435284b — checked:yes (files read)
- [formalization][trap] cslib-frontier proves both `not_ETH : ¬ETH` and `ETH.not_decidableInSubexpTime_PartialMCSP (h : ETH)`, so the latter is vacuous — cslib-frontier (2026) — checked:yes (statements read; not built)

---

## 9. Bibliography (proposed entries for research/BIB.md)

- `AW09` — S. Aaronson, A. Wigderson. "Algebrization: A New Barrier in Complexity Theory." ACM TOCT 1(1), 2009; STOC 2008; ECCC TR08-005. https://www.scottaaronson.com/papers/alg.pdf
- `BGS75` — T. Baker, J. Gill, R. Solovay. "Relativizations of the P =? NP Question." SIAM J. Comput. 4(4):431–442, 1975. (not opened)
- `RR97` — A. A. Razborov, S. Rudich. "Natural Proofs." J. Comput. Syst. Sci. 55(1):24–35, 1997. https://www.cs.cmu.edu/~rudich/papers/natural.ps (not readable here)
- `Chow11` — T. Y. Chow. "Almost-natural proofs." arXiv 0805.1385 (FOCS 2008 extended abstract; JCSS version, year not checked). https://arxiv.org/abs/0805.1385
- `Wil16NPD` — R. Williams. "Natural Proofs Versus Derandomization." STOC 2013 (special-issue revision; journal from memory). https://arxiv.org/abs/1212.1891
- `Wil14ACC` — R. Williams. "Nonuniform ACC Circuit Lower Bounds." J. ACM 61(1), 2014; CCC 2011. https://people.csail.mit.edu/rrw/acc-lbs.pdf
- `IKK09` — R. Impagliazzo, V. Kabanets, A. Kolokolova. "An Axiomatic Approach to Algebrization." STOC 2009. https://www.cs.sfu.ca/~kabanets/Research/algebrization.html
- `AB18` — B. Aydınlıoğlu, E. Bach. "Affine Relativization: Unifying the Algebrization and Relativization Barriers." ECCC TR16-040 (journal version; ToCT 2018 from memory). https://eccc.weizmann.ac.il/report/2016/040/
- `CHOPRS20` — L. Chen, S. Hirahara, I. C. Oliveira, J. Pich, N. Rajgopal, R. Santhanam. "Beyond Natural Proofs: Hardness Magnification and Locality." ITCS 2020, LIPIcs 151:70; J. ACM 69(4):25, 2022; ECCC TR19-168; arXiv 1911.08297. https://eccc.weizmann.ac.il/report/2019/168/
- `IP17` — C. Ikenmeyer, G. Panova. "Rectangular Kronecker coefficients and plethysms in geometric complexity theory." arXiv 1512.03798 (FOCS 2016 / Adv. Math.; from memory, not checked). https://arxiv.org/abs/1512.03798
- `BIP19` — P. Bürgisser, C. Ikenmeyer, G. Panova. "No occurrence obstructions in geometric complexity theory." J. AMS (2019). https://arxiv.org/abs/1604.06431
- `CHR25` — L. Chen, Y. Hu, H. Ren. "New Algebrization Barriers to Circuit Lower Bounds via Communication Complexity of Missing-String." ITCS 2026; ECCC TR25-184. https://arxiv.org/abs/2511.14038
- `LSTU26` — B. Loff, S. Sherif, N. Talebanfard, F. Ugazio. "The Switching Lemma shows what the Switching Lemma cannot prove: an unconditional natural-proofs barrier." arXiv 2606.12631, 2026. https://arxiv.org/abs/2606.12631
- `HLR23` — S. Hirahara, Z. Lu, H. Ren. "Bounded Relativization." ECCC TR23-070 (CCC 2023; from memory). https://eccc.weizmann.ac.il/report/2023/070/
- `RS21rel` — H. Ren, R. Santhanam. "A Relativization Perspective on Meta-Complexity." ECCC TR21-089 (published venue not checked). https://eccc.weizmann.ac.il/report/2021/089/
- `VW24` — N. Vyas, R. Williams. "On Oracles and Algorithmic Methods for Proving Lower Bounds." ECCC TR24-113. https://eccc.weizmann.ac.il/report/2024/113/
- `Kush26` — D. Kush. "An Unconditional Barrier for Proving Multilinear Algebraic Branching Program Lower Bounds." ECCC TR26-043. https://eccc.weizmann.ac.il/report/2026/043/
- `GGLST26` — M. Garlik, S. Gryaznov, J. Lu, R. Santhanam, I. Tzameret. "Meta-Mathematics of Algebraic Complexity." ECCC TR26-277 / arXiv 2610.33938. https://eccc.weizmann.ac.il/report/2026/277/
- `HLT24` — T. Hakoniemi, N. Limaye, I. Tzameret. "Functional Lower Bounds in Algebraic Proofs: Symmetry, Lifting, and Barriers." ECCC TR24-079. https://eccc.weizmann.ac.il/report/2024/079/
- `GKSS17` — J. Grochow, M. Kumar, M. Saks, S. Saraf. "Towards an algebraic natural proofs barrier via polynomial identity testing." ECCC TR17-009. https://eccc.weizmann.ac.il/report/2017/009/
- `CKRST20` — P. Chatterjee, M. Kumar, C. Ramya, R. Saptharishi, A. Tengse. "On the Existence of Algebraic Natural Proofs." FOCS 2020; ECCC TR20-063 (rev. 2024). https://eccc.weizmann.ac.il/report/2020/063/
- `CMS18` — A. Chattopadhyay, N. Mande, S. Sherif. "The Log-Approximate-Rank Conjecture is False." ECCC TR18-176 (conference venue not checked). https://eccc.weizmann.ac.il/report/2018/176/
- `HHLO23` — H. Hatami, K. Hosseini, S. Lovett, A. Ostuni. "Refuting approaches to the log-rank conjecture for XOR functions." ECCC TR23-203. https://eccc.weizmann.ac.il/report/2023/203/
- `ABX08` — B. Applebaum, B. Barak, D. Xiao. "On Basing Lower-Bounds for Learning on Worst-Case Assumptions." FOCS 2008, pp. 211–220, doi 10.1109/FOCS.2008.35 (per TR26-091 references; not opened).
- `AJ08` — A. E. Andreev, S. Jukna. "Very large cliques are easy to detect." Discrete Math. 308(16):3717–3721, 2008 (per CHOPRS references; not opened).
- `BT06` — A. Bogdanov, L. Trevisan. "On Worst-Case to Average-Case Reductions for NP Problems." ECCC TR05-015 (FOCS 2003 / SICOMP 2006; from memory). https://eccc.weizmann.ac.il/report/2005/015/
- `Nan21` — M. Nanashima. "On Basing Auxiliary-Input Cryptography on NP-hardness via Nonadaptive Black-Box Reductions." ITCS 2021; ECCC TR20-095. https://eccc.weizmann.ac.il/report/2020/095/
- `KC00` — V. Kabanets, J.-Y. Cai. "Circuit Minimization Problem." STOC 2000; ECCC TR99-045. https://eccc.weizmann.ac.il/report/1999/045/
- `MW15` — C. Murray, R. Williams. "On the (Non) NP-Hardness of Computing Circuit Complexity." Theory of Computing 13 (2017) 1–22 (per TR26-091 references); CCC 2015 (memory); ECCC TR14-164. https://eccc.weizmann.ac.il/report/2014/164/
- `HW16` — S. Hirahara, O. Watanabe. "Limits of Minimum Circuit Size Problem as Oracle." ECCC TR15-198 (CCC 2016; from memory). https://eccc.weizmann.ac.il/report/2015/198/
- `AH17` — E. Allender, S. Hirahara. "New Insights on the (Non)-Hardness of Circuit Minimization and Related Problems." ECCC TR17-073; ACM ToCT 11(4):27:1–27:27 (2019), per TR26-091 references. https://eccc.weizmann.ac.il/report/2017/073/
- `AHK15` — E. Allender, D. Holden, V. Kabanets. "The Minimum Oracle Circuit Size Problem." ECCC TR14-176. https://eccc.weizmann.ac.il/report/2014/176/
- `HOS18` — S. Hirahara, I. C. Oliveira, R. Santhanam. "NP-hardness of Minimum Circuit Size Problem for OR-AND-MOD Circuits." ECCC TR18-030 (CCC 2018; from memory). https://eccc.weizmann.ac.il/report/2018/030/
- `Ila20` — R. Ilango. "Constant Depth Formula and Partial Function Versions of MCSP are Hard." FOCS 2020; ECCC TR20-183. https://eccc.weizmann.ac.il/report/2020/183/
- `Ila19` — R. Ilango. "AC0[p] Lower Bounds and NP-Hardness for Variants of MCSP." ECCC TR19-021. Possibly published as "Approaching MCSP from Above and Below: Hardness for a Conditional Variant and AC0[p]", ITCS 2020, LIPIcs 34:1–34:26 (per TR26-091 references; identity not checked). https://eccc.weizmann.ac.il/report/2019/021/
- `Ila21` — R. Ilango. "The Minimum Formula Size Problem is (ETH) Hard." FOCS 2021. (not opened)
- `ILO20` — R. Ilango, B. Loff, I. C. Oliveira. "NP-Hardness of Circuit Minimization for Multi-Output Functions." CCC 2020; ECCC TR20-021. https://eccc.weizmann.ac.il/report/2020/021/
- `Hir22` — S. Hirahara. "NP-Hardness of Learning Programs and Partial MCSP." FOCS 2022, pp. 968–979; ECCC TR22-119. https://eccc.weizmann.ac.il/report/2022/119/
- `Ila23` — R. Ilango. "SAT Reduces to the Minimum Circuit Size Problem with a Random Oracle." FOCS 2023, pp. 733–742, doi 10.1109/FOCS57990.2023.00048 (per TR26-091 references); ECCC TR23-165. https://eccc.weizmann.ac.il/report/2023/165/
- `HIR23` — Y. Huang, R. Ilango, H. Ren. "NP-Hardness of Approximating Meta-Complexity: A Cryptographic Approach." STOC 2023; SIAM J. Comput. 54(4):819–886, 2025; ECCC TR23-046. https://eccc.weizmann.ac.il/report/2023/046/
- `HI25` — S. Hirahara, R. Ilango. "NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions." FOCS 2025, pp. 1648–1664. doi:10.1109/FOCS63196.2025.00087 (not opened)
- `HIL25` — S. Hirahara, R. Ilango, B. Loff. "Communication Complexity is NP-hard." ECCC TR25-094. https://eccc.weizmann.ac.il/report/2025/094/
- `GHM25` — S. Gaspers, T. Z. He, S. Mackenzie. "NP-Hardness and Additive Inapproximability of Deterministic Communication Complexity." arXiv 2508.05597 (v6, Nov 2026). https://arxiv.org/abs/2508.05597
- `GJK26` — H. Goldberg, M. Juvekar, V. Kabanets. "Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions." ECCC TR26-091. https://eccc.weizmann.ac.il/report/2026/091/
- `MP24obf` — N. Mazor, R. Pass. "Gap MCSP is not (Levin) NP-complete in Obfustopia." ECCC TR24-053. https://eccc.weizmann.ac.il/report/2024/053/
- `LMP26` — Y. Liu, N. Mazor, R. Pass. "Cryptographic Implications of Worst-Case Hardness of Time-Bounded Kolmogorov Complexity." ECCC TR26-051. https://eccc.weizmann.ac.il/report/2026/051/
- `SS22` — M. Saks, R. Santhanam. "On Randomized Reductions to the Random Strings." CCC 2022; ECCC TR22-074. https://eccc.weizmann.ac.il/report/2022/074/
- `GK24` — H. Goldberg, V. Kabanets. "Consequences of Randomized Reductions from SAT to Time-Bounded Kolmogorov Complexity." ECCC TR24-120. https://eccc.weizmann.ac.il/report/2024/120/
- `GR24` — L. Glinskih, A. Riazanov. "Partial Minimum Branching Program Size Problem is ETH-hard." arXiv 2407.04632. https://arxiv.org/abs/2407.04632
- `HLO25` — J. Hu, Z. Lu, I. C. Oliveira. "Hardness of Computing Nondeterministic Kolmogorov Complexity." ECCC TR25-203. https://eccc.weizmann.ac.il/report/2025/203/
- `GHLLO25` — H. Goldberg, J. Hu, Z. Lu, J. Lyu, I. C. Oliveira. "Synergies Between Complexity Theory and Nondeterministic Kolmogorov Complexity." ECCC TR25-215. https://eccc.weizmann.ac.il/report/2025/215/
- `GHLLO26a` — same authors. "The Gap Between Average-Case and Worst-Case Complexity." ECCC TR26-253 / arXiv 2610.19162. https://eccc.weizmann.ac.il/report/2026/253/
- `GHLLO26b` — same authors. "Asymmetry and Complexity of Nondeterministic Computations." ECCC TR26-290 / arXiv 2610.20188. https://eccc.weizmann.ac.il/report/2026/290/
- `HMO26` — J. Hu, Y. Manor, I. C. Oliveira. "Failure of Symmetry of Information for Randomized Computations." ECCC TR26-021. https://eccc.weizmann.ac.il/report/2026/021/
- `KK25` — V. Kabanets, A. Kolokolova. "Kolmogorov's Approach to P vs NP: Chain Rules for Time-Bounded Kolmogorov Complexity." ECCC TR25-089. https://eccc.weizmann.ac.il/report/2025/089/
- `GII19` — A. Golovnev, R. Ilango, R. Impagliazzo, V. Kabanets, A. Kolokolova, A. Tal. "AC0[p] Lower Bounds against MCSP via the Coin Problem." ECCC TR19-018 (ICALP 2019; from memory). https://eccc.weizmann.ac.il/report/2019/018/
- `CKLM19` — M. Cheraghchi, V. Kabanets, Z. Lu, D. Myrisiotis. "Circuit Lower Bounds for MCSP from Local Pseudorandom Generators." ECCC TR19-022 (ICALP 2019; from memory). https://eccc.weizmann.ac.il/report/2019/022/
- `HS17` — S. Hirahara, R. Santhanam. "On the Average-Case Complexity of MCSP and Its Variants." CCC 2017, LIPIcs 79:7. (not opened)
- `CHMY20` — M. Cheraghchi, S. Hirahara, D. Myrisiotis, Y. Yoshida. "One-Tape Turing Machine and Branching Program Lower Bounds for MCSP." ECCC TR20-103. https://eccc.weizmann.ac.il/report/2020/103/
- `AR23` — P. Austrin, K. Risse. "Sum-of-Squares Lower Bounds for the Minimum Circuit Size Problem." ECCC TR23-010; arXiv 2311.12994. https://eccc.weizmann.ac.il/report/2023/010/
- `Mil26` — A. Milovanov. "Limit on the computational power of C-random strings." ECCC TR26-034. https://eccc.weizmann.ac.il/report/2026/034/
- `HIW23` — S. Hirahara, R. Ilango, R. Williams. "Beating Brute Force for Compression Problems." ECCC TR23-171 (STOC 2024; from memory). https://eccc.weizmann.ac.il/report/2023/171/
- `MP23perebor` — N. Mazor, R. Pass. "The Non-Uniform Perebor Conjecture for Time-Bounded Kolmogorov Complexity is False." ECCC TR23-175 (ITCS 2024; from memory). https://eccc.weizmann.ac.il/report/2023/175/
- `MP24s2d` — N. Mazor, R. Pass. "Search-to-Decision Reductions for Kolmogorov Complexity." ECCC TR24-003. https://eccc.weizmann.ac.il/report/2024/003/
- `HKLO24` — S. Hirahara, V. Kabanets, Z. Lu, I. C. Oliveira. "Exact Search-to-Decision Reductions for Time-Bounded Kolmogorov Complexity." CCC 2024; ECCC TR24-059. https://eccc.weizmann.ac.il/report/2024/059/
- `Hir18` — S. Hirahara. "Non-black-box Worst-case to Average-case Reductions within NP." FOCS 2018; ECCC TR18-138. https://eccc.weizmann.ac.il/report/2018/138/
- `Hir20a` — S. Hirahara. "Unexpected Hardness Results for Kolmogorov Complexity Under Uniform Reductions." STOC 2020; ECCC TR20-050. https://eccc.weizmann.ac.il/report/2020/050/
- `Hir20b` — S. Hirahara. "Characterizing Average-Case Complexity of PH by Worst-Case Meta-Complexity." ECCC TR20-143 (FOCS 2020; from memory). https://eccc.weizmann.ac.il/report/2020/143/
- `Hir21` — S. Hirahara. "Average-Case Hardness of NP from Exponential Worst-Case Hardness Assumptions." STOC 2021; ECCC TR21-058. https://eccc.weizmann.ac.il/report/2021/058/
- `CHV21` — L. Chen, S. Hirahara, N. Vafa. "Average-case Hardness of NP and PH from Worst-case Fine-grained Assumptions." ECCC TR21-166. https://eccc.weizmann.ac.il/report/2021/166/
- `NM25` — T. Nareddy, A. Mishra. "Recovery Reductions, Conjectures, and Barriers." ECCC TR25-157. https://eccc.weizmann.ac.il/report/2025/157/
- `LP20` — Y. Liu, R. Pass. "On One-way Functions and Kolmogorov Complexity." FOCS 2020; ECCC TR20-052; arXiv 2009.11514. https://arxiv.org/abs/2009.11514
- `LP21crypto` — Y. Liu, R. Pass. "On the Possibility of Basing Cryptography on EXP ≠ BPP." CRYPTO 2021; ECCC TR21-056. https://eccc.weizmann.ac.il/report/2021/056/
- `LP21np` — Y. Liu, R. Pass. "On One-way Functions from NP-Complete Problems." ECCC TR21-059. https://eccc.weizmann.ac.il/report/2021/059/
- `RS21kt` — H. Ren, R. Santhanam. "Hardness of KT Characterizes Parallel Cryptography." CCC 2021; ECCC TR21-057. https://eccc.weizmann.ac.il/report/2021/057/
- `IRS22` — R. Ilango, H. Ren, R. Santhanam. "Hardness on any Samplable Distribution Suffices: New Characterizations of One-Way Functions by Meta-Complexity" (ECCC title). ECCC TR21-082. Published at STOC 2022 per the Lu–Santhanam TR24-085 abstract; the published title was not checked. https://eccc.weizmann.ac.il/report/2021/082/
- `San20` — R. Santhanam. "Pseudorandomness and the Minimum Circuit Size Problem." ITCS 2020; ECCC TR19-155. https://eccc.weizmann.ac.il/report/2019/155/
- `ACMTV21` — E. Allender, M. Cheraghchi, D. Myrisiotis, H. Tirumala, I. Volkovich. "One-way Functions and a Conditional Variant of MKTP." ECCC TR21-009. https://eccc.weizmann.ac.il/report/2021/009/
- `Hir23` — S. Hirahara. "Capturing One-Way Functions via NP-Hardness of Meta-Complexity." STOC 2023; ECCC TR23-037. https://eccc.weizmann.ac.il/report/2023/037/
- `HILNO23` — S. Hirahara, R. Ilango, Z. Lu, M. Nanashima, I. C. Oliveira. "A Duality Between One-Way Functions and Average-Case Symmetry of Information." STOC 2023; ECCC TR23-035. https://eccc.weizmann.ac.il/report/2023/035/
- `HN24` — S. Hirahara, M. Nanashima. "One-Way Functions and Zero Knowledge." STOC 2024; ECCC TR24-063. https://eccc.weizmann.ac.il/report/2024/063/
- `LP23wc` — Y. Liu, R. Pass. "On One-way Functions and the Worst-case Hardness of Time-Bounded Kolmogorov Complexity." ECCC TR23-103. https://eccc.weizmann.ac.il/report/2023/103/
- `LP23samp` — Y. Liu, R. Pass. "One-way Functions and Hardness of (Probabilistic) Time-Bounded Kolmogorov Complexity w.r.t. Samplable Distributions." CRYPTO 2023; ECCC TR23-152. https://eccc.weizmann.ac.il/report/2023/152/
- `HLO24` — S. Hirahara, Z. Lu, I. C. Oliveira. "One-Way Functions and pKt Complexity." ECCC TR24-136. https://eccc.weizmann.ac.il/report/2024/136/
- `HLN24` — S. Hirahara, Z. Lu, M. Nanashima. "Optimal Coding for Randomized Kolmogorov Complexity and Its Applications." ECCC TR24-155. https://eccc.weizmann.ac.il/report/2024/155/
- `LS24` — Z. Lu, R. Santhanam. "Impagliazzo's Worlds Through the Lens of Conditional Kolmogorov Complexity." ECCC TR24-085. https://eccc.weizmann.ac.il/report/2024/085/
- `LP25a` — Y. Liu, R. Pass. "Hardness Along the Boundary: Towards One-Way Functions from the Worst-case Hardness of Time-Bounded Kolmogorov Complexity." ECCC TR25-125. https://eccc.weizmann.ac.il/report/2025/125/
- `LP25b` — Y. Liu, R. Pass. "One-way Functions and Boundary Hardness of Randomized Time-Bounded Kolmogorov Complexity." ECCC TR25-202. https://eccc.weizmann.ac.il/report/2025/202/
- `HN26` — S. Hirahara, M. Nanashima. "A Sharp Characterization of Pessiland." ECCC TR26-052. https://eccc.weizmann.ac.il/report/2026/052/
- `AMPS26a` — G. Arnon, N. Mazor, R. Pass, J. Silbak. "Complexity-Theoretic Consequences of Zero-Knowledge with Inefficient Simulation." ECCC TR26-322. https://eccc.weizmann.ac.il/report/2026/322/
- `AMPS26b` — same authors. "Does Witness Indistinguishability Require Cryptography?" ECCC TR26-333. https://eccc.weizmann.ac.il/report/2026/333/
- `CJ26` — M. Carmosino, M. Juvekar. "Parallel Kolmogorov Complexity with Connections to Learning Theory and Cryptography." ECCC TR26-176. https://eccc.weizmann.ac.il/report/2026/176/
- `GK25` — H. Goldberg, V. Kabanets. "Witness Encryption and NP-hardness of Learning." ECCC TR25-070. https://eccc.weizmann.ac.il/report/2025/070/
- `CdRGS26` — B. P. Cavalar, S. F. de Rezende, M. Gray, R. Santhanam. "ETH-Hardness of Learning Monotone Circuits and Approximating Their Size." ECCC TR26-128; arXiv 2607.12331. https://eccc.weizmann.ac.il/report/2026/128/
- `CIKK16` — M. Carmosino, R. Impagliazzo, V. Kabanets, A. Kolokolova. "Learning Algorithms from Natural Proofs" (ECCC title "Algorithms from Natural Lower Bounds"). CCC 2016; ECCC TR16-008. https://eccc.weizmann.ac.il/report/2016/008/
- `OS17` — I. C. Oliveira, R. Santhanam. "Conspiracies between Learning Algorithms, Circuit Lower Bounds and Pseudorandomness." CCC 2017; ECCC TR16-197. https://eccc.weizmann.ac.il/report/2016/197/
- `HN23` — S. Hirahara, M. Nanashima. "Learning in Pessiland via Inductive Inference." ECCC TR23-100 (FOCS 2023; from memory). https://eccc.weizmann.ac.il/report/2023/100/
- `Kar23` — A. Karchmer. "Distributional PAC-Learning from Nisan's Natural Proofs." ECCC TR23-085. https://eccc.weizmann.ac.il/report/2023/085/
- `OS18` — I. C. Oliveira, R. Santhanam. "Hardness Magnification for Natural Problems." FOCS 2018, pp. 65–76; ECCC TR18-139. https://eccc.weizmann.ac.il/report/2018/139/
- `OPS19` — I. C. Oliveira, J. Pich, R. Santhanam. "Hardness Magnification near State-of-the-Art Lower Bounds." CCC 2019; ToC 17(11):1–38, 2021; ECCC TR18-158. https://eccc.weizmann.ac.il/report/2018/158/
- `MMW19` — D. M. McKay, C. D. Murray, R. R. Williams. "Weak Lower Bounds on Resource-Bounded Compression Imply Strong Separations of Complexity Classes." STOC 2019, pp. 1215–1225. https://people.csail.mit.edu/rrw/MCSP-MKTP-stoc19.pdf
- `CJW19` — L. Chen, C. Jin, R. Williams. "Hardness Magnification for all Sparse NP Languages." FOCS 2019, pp. 1240–1255; ECCC TR19-118. https://eccc.weizmann.ac.il/report/2019/118/
- `CJW20` — L. Chen, C. Jin, R. Williams. "Sharp Threshold Results for Computational Complexity." STOC 2020, pp. 1335–1348; ECCC TR20-065. https://eccc.weizmann.ac.il/report/2020/065/
- `CLY22` — L. Chen, J. Li, T. Yang. "Extremely Efficient Constructions of Hash Functions, with Applications to Hardness Magnification and PRFs." ECCC TR22-086. https://eccc.weizmann.ac.il/report/2022/086/
- `CT19` — L. Chen, R. Tell. "Bootstrapping Results for Threshold Circuits 'Just Beyond' Known Lower Bounds." STOC 2019; ECCC TR18-199. https://eccc.weizmann.ac.il/report/2018/199/
- `AM25` — A. Atserias, M. Müller. "Simple general magnification of circuit lower bounds." arXiv 2503.24061 (v2 Jun 2025). https://arxiv.org/abs/2503.24061
- `Pich22` — J. Pich. "Localizability of the approximation method." arXiv 2212.09285. https://arxiv.org/abs/2212.09285
- `Pich20` — J. Pich. "Learning algorithms from circuit lower bounds." arXiv 2012.14095. https://arxiv.org/abs/2012.14095
- `PS23` — J. Pich, R. Santhanam. "Towards P ≠ NP from Extended Frege Lower Bounds." ECCC TR23-199. https://eccc.weizmann.ac.il/report/2023/199/
- `CG25` — M. Carmosino, S. Grosser. "Student-Teacher Constructive Separations and (Un)Provability in Bounded Arithmetic: Witnessing the Gap." ECCC TR25-045. https://eccc.weizmann.ac.il/report/2025/045/
- `CKKOT24` — M. Carmosino, V. Kabanets, A. Kolokolova, I. C. Oliveira, D. Tsintsilidas. "Provability of the Circuit Size Hierarchy and Its Consequences." ECCC TR24-145. https://eccc.weizmann.ac.il/report/2024/145/
- `CJSW24` — L. Chen, C. Jin, R. Santhanam, R. Williams. "Constructive Separations and Their Consequences." TheoretiCS 3 (2024); arXiv 2203.14379. https://arxiv.org/abs/2203.14379
- `SW14` — R. Santhanam, R. Williams. "On Uniformity and Circuit Lower Bounds." Comput. Complex. 23:177–205, 2014. (not opened; via AM25)
- `LO23` — J. Li, I. C. Oliveira. "Unprovability of strong complexity lower bounds in bounded arithmetic." ECCC TR23-022 (conference venue not checked). https://eccc.weizmann.ac.il/report/2023/022/
- `CLO24` — L. Chen, J. Li, I. C. Oliveira. "On the Unprovability of Circuit Size Bounds in Intuitionistic S^1_2." ECCC TR24-083. https://eccc.weizmann.ac.il/report/2024/083/
- `KO17` — J. Krajíček, I. C. Oliveira. "Unprovability of circuit upper bounds in Cook's theory PV." LMCS 13(1:4), 2017; ECCC TR16-071. https://eccc.weizmann.ac.il/report/2016/071/
- `Ila25` — R. Ilango. "The Oracle Derandomization Hypothesis is False (And More) Assuming No Natural Proofs." ECCC TR25-190. https://eccc.weizmann.ac.il/report/2025/190/
- `RWZ25` — H. Ren, Y. Wang, Y. Zhong. "Hardness of Range Avoidance and Proof Complexity Generators from Demi-Bits." ECCC TR25-191. https://eccc.weizmann.ac.il/report/2025/191/
- `LRZ26` — X. Li, H. Ren, Y. Zhong. "Many Proof Complexity Generators Inside One Demi-Bits Generator." ECCC TR26-196. https://eccc.weizmann.ac.il/report/2026/196/
- `BHNST26` — A. Bouland, A. Huang, A. Natarajan, I. Shalit, A. Tal. "BQP ⊆ IP Does Not Relativize." arXiv 2609.25680. https://arxiv.org/abs/2609.25680
- `OP26` — S. Oral, S. Podder. "EQP ⊆ IP Does Not Relativize." arXiv 2611.12746. https://arxiv.org/abs/2611.12746
- `MPR26` — D. Miloschewsky, S. Podder, D. Rudolph. "Promises should be taken seriously: On relativization with promise problems." arXiv 2609.07945. https://arxiv.org/abs/2609.07945
- `CW26` — L. Chen, Y. Wang. "Separating RAM and Multitape Turing Machines with Short Random Oracles." ECCC TR26-006. https://eccc.weizmann.ac.il/report/2026/006/
- `LP26q` — C. Li, N. Parham. "Natural proofs for quantum state preparation lower bounds." arXiv 2610.06826. https://arxiv.org/abs/2610.06826
- `BenD26` — S. Ben Daniel. "Constant-Probability Witness Isolation Implies NP in P/poly." ECCC TR26-246; "Obfuscation and the Limits of Witness Isolation." ECCC TR26-201. https://eccc.weizmann.ac.il/report/2026/246/
- `KR26` — G. Kardeş, B. Rossman. "On Top-Down and Local Lower Bounds for AC0 Circuits." arXiv 2609.01759. https://arxiv.org/abs/2609.01759. Probably the "Kardeş–Rossman [KR26]" top-down AC⁰ argument that crosscheck 02 (missing item 12) could not locate: same authors, same topic. The match with the citation in TR26-248 was not verified.
- `MITHG26` — MIT Hardness Group (J. Brunner, E. D. Demaine, F. Frei, T. Gomez, M. Hecher, J. Li, J. Lynch). "ETH is Dead, Long Live SH." arXiv 2611.02650. https://arxiv.org/abs/2611.02650
- `Mol26` — H. Molter. "Running-Time Lower Bounds under FPT ≠ W[1]." arXiv 2611.26080. https://arxiv.org/abs/2611.26080
- `Li26learn` — X. Li (Claude agents). "What Does the Refutation of the Exponential Time Hypothesis Mean for Learning Theory?" Hexagon 2610.00613, Oct 2026. https://hexagonmath.org/2610.00613v1 [AI]
- `BEM26` — S. Ben-David, M. H. Ebtehaj. "The Metacomplexity Structure of Search Problems." arXiv 2611.25046. https://arxiv.org/abs/2611.25046
- `Myr26` — D. Myrisiotis. "Reconfiguration of Time-Bounded Descriptions." arXiv 2611.09020. https://arxiv.org/abs/2611.09020
- `GNO26` — H. Goldberg, M. Nanashima, I. C. Oliveira. "Learning, Compression, and Meta-Complexity." ECCC TR26-249 / arXiv 2610.16535. https://eccc.weizmann.ac.il/report/2026/249/
- `Oli25` — I. C. Oliveira. "Meta-Mathematics of Computational Complexity Theory." ECCC TR25-041 (survey). https://eccc.weizmann.ac.il/report/2025/041/
- `All20` — E. Allender. "The New Complexity Landscape around Circuit Minimization." ECCC TR20-078 (survey). https://eccc.weizmann.ac.il/report/2020/078/
- `Woeg16` — G. Woeginger. "The P-versus-NP page." https://www.win.tue.nl/~gwoegi/P-versus-NP.htm
- `Lip10` — R. J. Lipton. "Fatal flaws in Deolalikar's proof." Gödel's Lost Letter, 12 Aug 2010. https://rjlipton.com/2010/08/12/fatal-flaws-in-deolalikars-proof/
- `Blum17` — N. Blum. "A Solution of the P versus NP Problem" (withdrawn) / "On the Approximation Method and the P versus NP Problem." arXiv 1708.03486 (v3, 2020). https://arxiv.org/abs/1708.03486
- `Lip17` — R. J. Lipton, K. W. Regan. "On the edge of eclipses and P=NP." 17 Aug 2017 (updates 18 and 22 Aug). https://rjlipton.com/2017/08/17/on-the-edge-of-eclipses-and-pnp
- `XZ23` — K. Xu, G. Zhou. "SAT Requires Exhaustive Search." Frontiers of Computer Science 19(12):1912405, 2025; arXiv 2302.09512. https://arxiv.org/abs/2302.09512
- `CHKLN23` — M. C. Chavrimootoo, Y. He, M. Kotler-Berkowitz, H. Liuson, Z. Nie. "Evaluating the Claims of 'SAT Requires Exhaustive Search'." arXiv 2312.02071. https://arxiv.org/abs/2312.02071
- `Dong23` — Q. Dong, L. Dong, K. Xu, G. Zhou, Y. Hao, Z. Sui, F. Wei. "Large Language Model for Science: A Study on P vs. NP." arXiv 2309.05689. https://arxiv.org/abs/2309.05689
- `Arth26` — T. S. Arthanari. "Lean 4 Machine-Verified Proof of P = NP via the Pedigree Polytope Membership Problem." arXiv 2606.03194, 2026. https://arxiv.org/abs/2606.03194
- `PA26` — ProofAtlas. "P versus NP" collaboration page (status checked 7 Aug 2026). https://www.proofatlas.ai/collaboration/p-vs-np/
- `FMPTW15` — S. Fiorini, S. Massar, S. Pokutta, H. R. Tiwary, R. de Wolf. "Exponential Lower Bounds for Polytopes in Combinatorial Optimization." J. ACM 2015; STOC 2012. https://arxiv.org/abs/1111.0837
- `konard26` — konard. "p-vs-np" (GitHub repository, README updated Sep 2026). https://github.com/konard/p-vs-np
- `cslib798` — cslib-frontier issue #798 "Metacomplexity track"; PR #4512 (ROADMAP: magnification and locality); #4644; #4634/#4635 (CIKK); PR #6151 (low-degree extension). https://github.com/cslib-community/cslib-frontier/issues/798

---

## 10. Search log

**Lab context read:** CLAUDE.md; research/KNOWN_RESULTS.md; survey/00, 01 (§1–§5 and the grep hits), 02 (§1, §2.10, §3–§8);
reviews/survey-02 crosscheck (§3–§5, §9) and survey-01 crosscheck (grep hits); DIRECTIONS, LOG, DEAD_ENDS, CLAIMS.

**cslib-frontier (local clone /tmp/claude-0/ext/cslib-frontier, commit 1435284b):**
- Read: ROADMAP.md; roadmap/{models,complexity,circuits}.md; results/README.md; results/arora-barak-2007.md §22.
- Read the module docstrings of CslibFrontier/Computability/MCSP/** (Basic, NP, Partial, PartialETH, PartialHardness/*, Magnification*, FormulaMagnification/*, AntiChecker, Multi*, HardnessConsequences, ZeroErrorAverageCase), Kolmogorov/* (MINKT, MINKTStar, MINcKT, MKtP, AverageCase, Conditional, ChainRule, SymmetryOfInformation, NisanWigderson, Depth, Incompleteness), Crypto/Computational/OneWay/{LiuPass,LiuPassConverse,MCSP}.lean, Circuit/Boolean/NaturalProof*, Circuit/Boolean/Oracle/{LocalCircuit,LocalClass}.lean, Razborov/Natural.lean, MachineLearning/.../NaturalProperty.lean, Classes/Oracle/Collapse.lean.
- Grepped `sorry`, `axiom` and `native_decide`.
- GitHub web pages: issue #798 (both halves), #4644, PR #4512. Issue search "MCSP OR Kolmogorov OR magnification OR locality OR algebrization OR 'natural proofs'" (119 results, first page read). Issue search "algebrization" (0 results). PR search "algebrization OR 'low-degree extension' OR Aaronson" (10 results).
- `gh api` was refused for this repository ("GitHub access to this repository is not enabled for this session"), so I used WebFetch.

**ECCC:**
- Year listings 1999, 2003, 2005, 2006, 2008, 2009, 2014–2026, fetched with curl and parsed by a script.
- Report pages read (abstracts and change notes):
  - 2026: 006, 015, 021, 034, 043, 051, 052, 053, 062, 068, 091 (+PDF), 098, 109, 128, 176, 196, 201, 205, 246, 249, 253, 275, 277, 290, 318, 322, 333.
  - 2025: 001, 028, 041, 045, 070, 072, 086, 089, 092, 094, 104, 125, 157, 184, 187, 190, 191, 202, 203, 211, 215, 220, 221.
  - 2024: 003, 051, 053, 055, 059, 060, 063, 079, 083, 085, 113, 115, 120, 136, 145, 155, 194, 195, 201.
  - 2023: 010, 022, 028, 035, 037, 038, 046, 070, 079, 080, 085, 100, 103, 152, 165, 171, 175, 192, 193, 199, 203.
  - 2022: 074, 084, 086, 119, 127.
  - 2021: 009, 056, 057, 058, 059, 082, 089, 166.
  - 2020: 021, 050, 052, 063, 065, 078, 095, 103, 143, 183.
  - 2019: 018, 021, 022, 118, 155, 168 (+PDF).
  - 2018: 030, 138, 139, 158, 159, 176, 199.
  - 2017: 009, 023, 073.
  - 2016: 008, 040, 071, 197.
  - 2015: 198. 2014: 164, 176. 2005: 015. 1999: 045.
- The first listing request returned an empty reply; one retry succeeded.

**arXiv:**
- The API (export.arxiv.org) needs https and was rate-limited ("Rate exceeded", HTTP 503) after a few queries. Queries that did run: all:"minimum circuit size", all:MCSP, all:"meta-complexity", all:metacomplexity, all:"hardness magnification", all:"time-bounded Kolmogorov".
- Monthly listings cs.CC 2026-09, 2026-10, 2026-11 (curl, all entries parsed).
- Abstract pages: 0805.1385 (+PDF), 1111.0837, 1212.1891, 1512.03798, 1604.06431 (+PDF), 1708.03486, 1911.08297, 2012.14095, 2203.14379, 2212.09285, 2302.09512, 2309.05689, 2312.02071, 2407.04632, 2503.24061 (+PDF), 2508.05597, 2511.14038, 2512.21764, 2606.03194, 2606.12631, 2608.02859, 2608.14673, 2609.01759, 2609.07945, 2609.25680, 2609.35927, 2610.06826, 2610.11432, 2610.16535, 2611.02650 (+PDF), 2611.05136, 2611.09020, 2611.12746, 2611.12943, 2611.25046, 2611.26080.

**PDFs read:** scottaaronson.com/papers/alg.pdf (AW09); people.csail.mit.edu/rrw/acc-lbs.pdf (Williams ACC, §1 barrier paragraph); people.csail.mit.edu/rrw/MCSP-MKTP-stoc19.pdf (MMW19).

**Web searches (WebSearch):**
- "Hirahara Ilango FOCS 2025 MCSP NP-hard quasi-polynomial reductions constant gap"
- "hardness magnification 2025 2026 new results circuit lower bounds preprint"
- "NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions"
- "McKay Murray Williams Weak lower bounds ... pdf"
- "Razborov Rudich Natural proofs pdf Theorem 4.1 ..."
- "Impagliazzo Kabanets Kolokolova An axiomatic approach to algebrization"
- "Ilango The Minimum Formula Size Problem is (ETH) Hard FOCS 2021 abstract"
- "Deolalikar P vs NP 2010 flaws Immerman FO(LFP) ..."
- "Norbert Blum 2017 P≠NP proof Tardos function counterexample"
- "claimed proof P ≠ NP 2026 AI-generated arXiv preprint retracted" (extended)
- "critique SAT Requires Exhaustive Search ..."
- "formalization Lean OR Coq OR Isabelle Kolmogorov complexity OR natural proofs ..."
- "Minimum Circuit Size Problem 2026 NP-hard OR NP-complete new result" (extended)
- "ETH refuted 2026 consequences minimum formula size problem ..." (it returned only cryptocurrency "ETH" news; no useful result)

**WebFetch:** github.com/cslib-community/cslib-frontier issues and PRs listed above; github.com/konard/p-vs-np (twice); rjlipton.com 2010/08/12 and 2017/08/17; proofatlas.ai/collaboration/p-vs-np; hexagonmath.org (front page, search "Kolmogorov", "circuit", "P vs NP"); hexagonmath.org/2610.00613v1 (Li 2026); cs.sfu.ca/~kabanets/Research/algebrization.html (by curl); win.tue.nl/~gwoegi/P-versus-NP.htm (by curl); raw.githubusercontent.com/openai/math/main/CONTENTS.md (curl; all item titles, numbered up to 378, grepped); raw.githubusercontent.com/anthropics/formal-math/main/README.md (curl).

**Could not open / not used:**
- RR97 primary (Rudich's natural.ps is a bitmap-font PostScript and no PS→text tool was available; ScienceDirect HTTP 403). RR's statement is therefore taken from Chow (opened).
- BGS75 primary.
- HI25 FOCS 2025 (IEEE Xplore returned no content).
- Ilango FOCS 2021 MFSP.
- HS17 CCC 2017.
- Santhanam–Williams 2014.
- Ko 1991; AGGM06; ABX08; Feigenbaum–Fortnow 1993; Saks–Santhanam CCC 2020; Forbes–Shpilka–Volk 2018; Dörfler–Ikenmeyer–Panova; Lu–Santhanam–Tzameret TR25-134 (title only); Sheshadri TR26-275 (abstract incomplete); Istrate TR26-318 (first sentence only).
- The Polymath wiki Deolalikar page (404).
- Blum's "mistake.pdf" (HTTP 503 via WebFetch; curl gave no file).
- CACM blog "What Happened in Fall 2026: AI and P vs NP" (HTTP 403).
- The Mintpath Reservoir package; Szeider's [Sze26] and Lampis' posts (seen only as MITHG26 references); the Xu–Zhou reply arXiv 2401.01193; the Zenodo "Starflower Inheritance III" record (search snippet only).
- DBLP API (bot challenge); Semantic Scholar API (HTTP 429 twice).
