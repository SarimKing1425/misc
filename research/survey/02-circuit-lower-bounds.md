# Survey 02: Boolean circuit lower bounds, the algorithmic method, explicit constructions

- Author: lit-scout (area 02), 2026-11-23. Single agent, no sub-agents.
- Scope: general fan-in-2 circuits (B2 and U2/De Morgan bases), formulas, AC0, AC0[p], ACC0, threshold circuits
  (THR∘THR), monotone circuits, Kannan-type fixed-polynomial lower bounds, near-maximum lower bounds for exponential
  classes, range avoidance, matrix rigidity, hardness magnification and the locality barrier. There is a dedicated
  section (§4) on R. Williams' 23 Nov 2026 challenge, and a note on the claimed Oct-2026 ETH refutation.
- **Conventions.** `checked: yes` means I opened the primary paper or abstract on 2026-11-23 and the bound matches
  the text. `checked: no` means I did not, even if a secondary source I opened states it; the secondary source is
  then named. **[PREPRINT]** means not yet peer-reviewed (an ECCC/arXiv posting, many under 2 months old).
  **[AI]** means the authors disclose that the proof was found or elicited by an AI system. Anything the lab itself
  derives is marked with a CLAUDE.md status label (`conjecture` / `informal-argument`) and is not a known result.
- **Recency warning.** This area moved more between Sept and Nov 2026 than in the previous five years: a 4n B2 bound,
  the AC0 "parity barrier" broken, n^{2.5−ε} for THR∘THR, exponential correlation bounds against polynomials, and
  two claimed ETH refutations. Many of these are preprints with AI-produced proofs. Treat every [PREPRINT]
  row as "claimed" until the community has digested it.

---

## 1. Plain-language summary

A Boolean circuit is a network of simple logic gates, and one route to P ≠ NP is to show that some NP problem, such
as SAT, needs super-polynomially many gates. Today nobody can prove that any concrete NP problem needs more than a
small constant times n gates on n-bit inputs: about 5n in the De Morgan basis (2002), 3.1n in the full binary basis
(peer-reviewed, 2022), and 4n in a preprint from this month whose proof was found with AI tools. The only method that
works for general circuits ("gate elimination") is believed, and partly proven, to stall below 5n. Real progress
therefore happens on restricted circuits (very shallow ones, ones with counting or threshold gates, and monotone
ones), several of which got claimed records in 2026, mostly in preprints. Williams' "algorithmic method" turns a
slightly-faster-than-brute-force satisfiability algorithm for a circuit class into a proof that some hard function
lies outside that class; it gave NEXP ⊄ ACC0 and, in 2026, a new bound for two-layer threshold circuits. Williams' new
challenge, to show that SAT on length-L inputs needs more than L^{1.01} gates, is far beyond current tools: gate
elimination stops at a constant times L, natural-proof methods are expected to stop near L·polylog L, and "hardness
magnification" shows that such bounds for some sparse NP problems would already imply much stronger separations. The
claimed October-2026 sub-exponential 3-SAT algorithm, if correct, implies (as its authors note, through a 2010
theorem of Williams) that the huge class E^NP has no circuits of size c·n·√log n, but it does not move lower bounds
for NP or SAT.

---

## 2. Frontier table

Notation: n = number of input bits unless stated. "B2" = all 2-input gates; "U2" (De Morgan basis) = 2-input gates
except XOR/XNOR. SIZE[s] = B2 circuits of size O(s).

### 2.1 General fan-in-2 circuits (explicit functions)

| # | Model | Function | Best known bound | Reference | Status | checked |
|---|---|---|---|---|---|---|
| G1 | B2 | explicit F ∈ P (any affine disperser for dimension d; Li's FOCS'23 disperser gives d = O(log n)) | **4n − O(log n)**, precisely 4n − 10d (Thm 4.1 text: "any B2-circuit computing f has size at least 4n − 10d"; the proof yields a refuter in time poly(n, 2^d)) | O. S. Mishra, R. Santhanam, "An explicit 4n − O(log(n)) size lower bound against general Boolean circuits", ECCC TR26-260 Revision 1, 3 Nov 2026 | [PREPRINT][AI] (proof "elicited from AI tools") | yes (PDF) |
| G1a | B2 | same | 3.5n − o(n) (v1 abstract; rev1 calls it 3.5n − O(log n)) | Mishra–Santhanam, ECCC TR26-260 v1, 19 Oct 2026 | superseded by G1 | yes |
| G2 | B2 | affine dispersers for sublinear dimension | **3.1n − o(n)** (best *peer-reviewed* B2 bound) | J. Li, T. Yang, "3.1n − o(n) circuit lower bounds for explicit functions", STOC 2022, pp. 1180–1193; ECCC TR21-023 | peer-reviewed | yes |
| G3 | B2 | affine dispersers for sublinear dimension | (3 + 1/86)n − o(n) | M. G. Find, A. Golovnev, E. A. Hirsch, A. S. Kulikov, FOCS 2016, pp. 89–98; journal "Improving 3n circuit complexity lower bounds", Comput. Complex. 32(2):13, 2023; ECCC TR15-166 | peer-reviewed | yes |
| G3a | B2 | quadratic dispersers (no explicit construction known in NP) | 3.11n | same journal version (FGHK 2023), merging ECCC TR15-170 | conditional on explicit quadratic dispersers | yes |
| G4 | B2 | affine dispersers for dim o(n) | 3n − o(n) | Demenkov–Kulikov, MFCS 2011 | — | no (secondary: FGHK abstract, MS26 §1.3) |
| G5 | B2 | explicit (Paul-type) | 3n − o(n) (record for >30 years) | N. Blum, TCS 28:337–345, 1984 | — | no (secondary: MS26, Li–Yang abstract) |
| G6 | B2 | Mod3 | 2.5n − 3 (Stockmeyer 1977); Mod3 has 3n + O(1) circuits (Demenkov et al. IPL 2010), so this function cannot give > 3n + O(1) | MS26 §1.3 | — | no (secondary MS26) |
| G7 | B2 | Σ_{i<j} x_i x_j over F2 / Mod3 | 2n − O(1) (Kloss–Malyshev 1965; Schnorr 1974) | MS26 §1.3 | — | no (secondary) |
| G8 | U2 | (n − o(n))-mixed functions in P | **5n − o(n)** | K. Iwama, H. Morizumi, "An explicit lower bound of 5n − o(n) for Boolean circuits", MFCS 2002, LNCS 2420:353–364 (some literature attributes it to Iwama–Lachish–Morizumi–Raz; both attributions appear) | peer-reviewed | no (secondary: MS26, JMV §1) |
| G9 | U2 | (n − o(n))-mixed | 4.5n − o(n) | O. Lachish, R. Raz, STOC 2001, pp. 399–408 | — | no (secondary MS26) |
| G10 | U2 | limitation | an (n − o(n))-mixed function has U2 complexity 5n + o(n), so Lachish–Raz-type arguments cannot exceed 5n | K. Amano, J. Tarui, TCS 412(18):1646–1651, 2011 | barrier | no (secondary MS26) |
| G11 | U2 | Parity (XOR) | 3(n − 1), tight (Schnorr 1974); also a 2026 constructive refuter for De Morgan circuits of size exactly 3(n − 1) | Carmosino, Dang, Jackman, arXiv 2604.23958 (Apr 2026); 2602.17942 (Feb 2026) | [PREPRINT] | yes (abstracts) |
| G12 | B2 #SAT/correlation | B2 circuits of size 2.5n − o(n) (Chen–Kabanets TCS 2016) and 2.99n (Golovnev–Kulikov–Smal–Tamaki MFCS 2016): non-trivial #SAT algorithms | — | MS26 §1.3 | — | no (secondary) |
| G13 | depth | explicit function, fan-in-2 formula depth | (3 − o(1))·log n; (4 − o(1))·log n if the top 2 − o(1) layers are AND gates | Hao Wu, ECCC TR24-086 (abstract states "current best depth lower bound is (3 − o(1))·log n") | [PREPRINT for the restricted result] | yes |

Gate-elimination limits (rows that bound the technique, not the function):

| # | Statement | Reference | checked |
|---|---|---|---|
| GL1 | Gate elimination cannot give cn beyond a constant c that depends on the number of substitutions per step. Per MS26 §1.5: no bound > 5n by substituting variables with arbitrary functions while arguing > 5 gates eliminated per step. | Golovnev, Hirsch, Knop, Kulikov, "On the limits of gate elimination", MFCS 2016 / JCSS 96:107–119, 2018; ECCC TR16-119 | yes (abstract); the 5n specifics are via MS26 |
| GL2 | "gate elimination is inherently limited to proving lower bounds of less than 5n"; every circuit of size s is an OR of 2^{s/3.9} 16-CNFs, so a depth-3 2^{n−o(n)} bound with bottom fan-in 16 gives 3.9n − o(n) (now below G1) | Golovnev, Kulikov, Williams, "Circuit depth reductions", ITCS 2021, LIPIcs 185:24; arXiv 1811.04828 | yes |
| GL3 | Mishra–Santhanam: "Our current belief is that the bound in this paper [4n] is close to the limit of what can be achieved using gate elimination." It is unknown whether affine dispersers have linear-size B2 circuits. | MS26 §1.5–1.6 | yes |

### 2.2 Formulas

| # | Model | Function | Best known bound | Reference | checked |
|---|---|---|---|---|---|
| F1 | De Morgan formulas (leaf count) | Andreev's function A ∈ P | **Ω(n^3 / (log^2 n · log log n))**, "tight (for A) up to the log log n factor, and the best known lower bound for functions in P"; average case: Komargodski et al.'s h_r ∈ P is not computable on > 1/2 + 2^{−r} of inputs by formulas of size n^3/(r^2 polylog n), r ≤ n^{1/3} | A. Tal, "Shrinkage of De Morgan formulae by spectral techniques", FOCS 2014; ECCC TR14-048 (rev. 2016) | yes |
| F2 | De Morgan | Andreev | n^{3−o(1)} via shrinkage exponent 2 | J. Håstad, SIAM J. Comput. 1998 | no (secondary: Tal abstract) |
| F3 | De Morgan | Andreev | n^{2.5−o(1)} | A. Andreev, 1987 | no |
| F4 | De Morgan | an AC0 function | cubic (Ω̃(n^3)) via shrinkage under random projections | Filmus, Meir, Tal, ITCS 2021; ECCC TR20-180 | no (title only) |
| F5 | B2 formulas | Nechiporuk-type | Ω(n^2/log n) | Nechiporuk 1966 | no (from memory) |
| F6 | probabilistic De Morgan formulas | MCSP[(log n)^c] | no n^{2−o(1)}-size probabilistic formulas; an n^{2+ε} bound would give NP ⊄ Formula[n^k] ∀k and #SAT ∉ log-depth circuits (sharp threshold) | L. Chen, C. Jin, R. Williams, "Sharp threshold results for computational complexity", STOC 2020; ECCC TR20-065 | yes |
| F7 | De Morgan formulas | MCSP[2^{√n}] | no formulas of size N^{1.99} (Hirahara–Santhanam, CCC 2017) | via MMW19 abstract | no (secondary) |
| F8 | De Morgan | OV_{n,d} | Ω(n^2 d), tight up to constants | Choudhury, Limaye, Sreenivasaiah, Srinivasan, ECCC TR26-121 (Jul 2026) [PREPRINT] | yes |

No improvement on F1 (beyond log factors) was found in 2017–2026 searches.

### 2.3 Constant depth: AC0 (unbounded fan-in AND/OR, depth d)

| # | Function | Best known bound | Reference | Status | checked |
|---|---|---|---|---|---|
| A1 | explicit "trilinear" f_n(x,y,a) = Σ_{i,j} a_{i+j} x_i y_j mod 2 (Goldreich–Tal), x,y ∈ {0,1}^n, a ∈ {0,1}^{2n−1} | for every fixed d ≥ 3: **2^{Ω((n log n / log log n)^{1/(d−1)})}** gates; upper bound: f_n has depth-d circuits with 2^{O(n^{2/d})} gates. "To our knowledge, for every fixed d ≥ 4 … the first lower bound of 2^{ω(n^{1/(d−1)})} … for an explicit function." | N. Chukhin, "Breaking the parity barrier for constant-depth circuits", ECCC TR26-248, 10 Oct 2026 | [PREPRINT][AI-assisted: ChatGPT 6 Astra / Claude Opus 5.5 disclosed] | yes (PDF) |
| A2 | inverse trace over binary fields; Goldreich–Tal trilinear; OpenAI's polynomial evaluator | for every fixed d ≥ 3: **2^{Ω_d((n log n)^{1/(d−1)})}** (all parameter bits count as inputs); correlation of inverse trace with size-S circuits (n ≤ S ≤ 2^{c_d n^{1/(d−1)}}) ≤ 2^{−η_d n log log S/(log S)^{d−1}}; upper bounds for inverse trace: 2^{O(n^{2/3})} at depth 8, 2^{O(√n log n)} at depth 9 | Xin Li, Yan Zhong, "Short point lists for CNFs and stronger constant-depth circuit hardness", ECCC TR26-261, 19 Oct 2026 | [PREPRINT] | yes |
| A3 | explicit function in P (polynomial evaluation over F2[Z]/(P)) | depth 3 (OR–AND–OR): 2^{ω(√n)}; "implicitly" 2^{Ω(√n · log log n / log log log n)} | OpenAI, "Beyond the Square-Root Exponent for Depth-Three Boolean Circuits", OpenAI Math Release preprint, 23 Sep 2026 (family 112 of the 6 Oct 2026 release) | [PREPRINT][AI: "produced by an internal OpenAI model"] | no (not opened; via TR26-248 §1 and arXiv 2610.17090) |
| A4 | Parity | 2^{Ω(n^{1/(d−1)})} for depth d (Håstad 1986/89); top-down proofs now exist for all depths (exp(ε_d n^{1/(d−1)})) | Håstad; O. Korten, "Top-down lower bounds for all depths", ECCC TR26-221 (Sep 2026) | classic / [PREPRINT] | Korten: yes; Håstad: no (secondary: TR26-248, arXiv 2609.34029, 2609.24188) |
| A5 | Parity, depth 3 | Ω(n^{1/4} 2^{√n}), tight up to a constant factor (Paturi–Pudlák–Zane 1999) | via TR26-248 §1 | classic | no (secondary) |
| A6 | best explicit depth-3 before 2026 | 2^{(π/√6)√n − o(√n)} (Paturi–Pudlák–Saks–Zane 2005) | via TR26-248 §1 | superseded by A1–A3 | no (secondary) |
| A7 | **every symmetric function, incl. Majority** | *upper* bound: depth-d circuits of size 2^{O(n^{1/(d−1)})}, matching Håstad. Majority cannot beat parity in AC0. | V. Lecomte, P. Ramakrishnan, "Optimal shallow circuits for majority", arXiv 2609.34029 (Sep 2026) | [PREPRINT][AI: "found by GPT-6 Astra"] | yes |
| A8 | target (Valiant) | a 2^{ω(n/log log n)} depth-3 bound for an explicit function gives the first superlinear lower bound for linear-size, log-depth fan-in-2 circuits | Valiant 1977/83, via TR26-248 §1 and ECCC TR26-208 §5 | open | no (secondary) |
| A9 | E^NP, depth 3 | open: 2^{n^{1/2+ε}} for E^NP is "a notoriously hard open question"; it would follow from F2-polynomial correlation bounds at degree d = n^{1/2+ε} | L. Chen, X. Lyu, ECCC TR21-003 (2021) | open | yes |
| A10 | k-OV / k-XOR / k-SUM / hyperclique, fixed depth | n^{Ω(k)} for OV, (n/k)^{Ω(k)} for XOR and SUM; the k-OV conjecture holds for constant-depth circuits in polylog dimension (n^{k−ε}) | H. Lin, ECCC TR26-139 (2026); N. Chukhin, arXiv 2611.06231 (Nov 2026) | [PREPRINT] | yes |

### 2.4 AC0[p], ACC0 and the algorithmic method

| # | Statement | Reference | Status | checked |
|---|---|---|---|---|
| C1 | NEXP has no non-uniform ACC0 circuits of polynomial (slightly: quasi-polynomial) size; E^NP has no ACC0 circuits of size 2^{n^{o(1)}}; for every d, m there is δ > 0 with E^NP ⊄ depth-d ACC0[m] of size 2^{n^δ} | R. Williams, "Nonuniform ACC circuit lower bounds", CCC 2011; J. ACM 61(1):2, 2014 | peer-reviewed | yes (journal PDF) |
| C2 | Easy-witness lemma for NP: NP ⊆ SIZE[n^k] ⇒ NP verifiers have n^{O(k^3)}-size witness circuits (and the same for NQP). For every k: **NQP ⊄ ACC0∘THR of size n^{log^k n}**. Thm 1.1: if Gap-C-UNSAT on n-input 2^{εn}-size circuits is solvable in nondeterministic O(2^{(1−ε)n}) time, then ∃c ∀k NTIME[n^{ck^4/ε}] ⊄ C-SIZE[n^k]. Thm 1.2: 2^{n−n^ε} time for 2^{n^ε}-size ⇒ NQP lower bounds. | C. Murray, R. Williams, STOC 2018; SIAM J. Comput. 49(5), 2020; ECCC TR17-188 | peer-reviewed | yes |
| C3 | For all c, a language in NQP that no poly-size ACC0 (even 2^{log^a n}-size ACC0∘THR) computes on a 1/2 + 1/log^c n fraction of inputs | L. Chen, ECCC TR19-031 (FOCS 2019; venue not verified) | peer-reviewed | yes |
| C4 | For all a: NQP is not (1/2 + 2^{−log^a n})-approximable by 2^{log^a n}-size ACC0∘THR; for all k, NP is not (1/2 + n^{−k})-approximable by n^k-size Sum∘THR | L. Chen, H. Ren, STOC 2020; ECCC TR20-010 | peer-reviewed | yes |
| C5 | **Almost-everywhere**: f ∈ E^NP not (1/2 + 2^{−n^ε})-approximable by 2^{n^ε}-size ACC0 at every large n; rigid matrices in P^NP for all large n; E^NP functions with constant-error probabilistic degree Ω(n/log^2 n) a.e. | L. Chen, X. Lyu, R. Williams, FOCS 2020; ECCC TR20-150 | peer-reviewed | yes |
| C6 | NEXP has no ACC0 circuits of sub-half-exponential size (previous: sub-third-exponential); MA_{ACC0} ⊄ fixed-poly ACC0; NTIMEGUESS[2^{polylog n}, n^{ω(1)}] has no poly-size ACC0; a derandomization-centric proof of NQP ⊄ ACC0 | L. Chen, ECCC TR22-183 (venue not verified) | — | yes |
| C7 | ACC0∘THR SAT algorithm ⇒ NEXP ⊄ ACC0∘THR | R. Williams, STOC 2014 | peer-reviewed | no (used as stated in C2 abstract) |
| C8 | AC0[⊕]: Majority needs exponential size (Razborov 1987); AC0[p]: MOD_q needs exponential size for primes p ≠ q (Smolensky 1987). Exponent from memory: 2^{Ω(n^{1/(2d)})} | Williams JACM 2014 §1 (qualitative statement) | classic | no (secondary, qualitative only; exponent from memory) |
| C9 | **Correlation**: the XOR of k majorities on disjoint ℓ-bit blocks has correlation ≤ (4d/√ℓ)^k with every Boolean-valued degree-d polynomial over any field (v1, F2: (2d/√ℓ)^k). Hence an explicit function with correlation 2^{−Ω(n/d^2)} against degree-d polynomials; 2^{−n^{Ω(1)}} correlation against 2^{n^{Ω(1)}}-size AC0[q] for every fixed prime power q; 2^{n^{Ω(1)}} size bounds for MAJ∘AC0[q]; PRGs with seed d^2·polylog(n/ε). Previously, for d ≥ log n no explicit function had correlation asymptotically below Razborov–Smolensky's O(d/√n). | E. Chattopadhyay, P. Hatami, C. H. Lee, S. Lovett, A. Tal, E. Viola, "Exponential correlation bounds for polynomials", ECCC TR26-208 (24 Sep 2026; rev. 11 Oct 2026) | [PREPRINT] | yes (PDF) |
| C10 | Open: Majority ∉ ACC0 ("widely believed conjecture"); torus-polynomial route: symmetric torus polynomials are provably weaker than asymmetric ones | V. Krishan, S. Vishwanathan, ECCC TR24-074 (rev. Nov 2025) | open | yes |
| C11 | Symmetric depth-h CC0 circuits computing AND need 2^{Ω̃(n^{1/O(h)})} size (also Pago, ICALP 2026, independently) | V. Krishan, J. Sarma, ECCC TR26-116 (Jul 2026) | [PREPRINT] | yes |
| C12 | Lower bounds for a subclass of AC0[2] capturing both DNF∘XOR and depth-3 AC0 (middle slice, inner product, affine dispersers) | Riazanov, Sofronova, Sokolov, ECCC TR25-024 | — | yes (no exact bounds in abstract) |

Open (verified as open in the cited source): **NP ⊄ ACC0**. The obstacle named by Murray–Williams is the lack of a
Gap-ACC-UNSAT algorithm running in 2^{(1−ε)n} on 2^{εn}-size circuits (MW20 §6, checked: yes). Also open:
**E^NP ⊄ THR∘THR (poly size)** and **NEXP ⊄ TC0**.

### 2.5 Threshold circuits (TC0, THR∘THR, SYM∘THR)

| # | Statement | Reference | Status | checked |
|---|---|---|---|---|
| T1 | **f ∈ E^NP needs n^{2.5−ε}-size THR∘THR (and SYM∘THR) circuits** for every ε ∈ (0,1). Via a deterministic CAPP algorithm for ⊕2∘THR_{O(n^{2.5−ε})}∘THR running in 2^{n−n^{Ω(ε)}}. Previous: n^{2−ε} for E^NP (Tamaki ECCC TR16-100; Alman–Chan–Williams FOCS 2016). | L. Chen, A. Tal, Y. Wang, "Super-quadratic lower bounds for depth-2 linear threshold circuits", ECCC TR26-039 (Mar 2026); STOC 2026 per Nag's revision note (venue not independently verified) | peer-reviewed (if STOC'26) | yes (PDF) |
| T2 | **Almost-everywhere near-cubic wire bounds**: for every c > 0 there is F_c ∈ E^NP such that at every large n, no SYM∘THR with ≤ b·n^3/log^{10} n wires and no THR∘THR with ≤ b'·n^3/log^{12} n wires has agreement ≥ 1/2 + n^{−c} (fixed advantage: log^5 n and log^9 n) | D. Nag, ECCC TR26-167 (Sep 2026, rev. 25 Sep 2026); Lean check of Thm 2.5 *from nine quoted statements* of cited results | [PREPRINT] | yes |
| T3 | Explicit (P) function: Andreev's function is not computable on a (1/2 + ε) fraction by depth-2 LTF circuits with o(ε^3 n^{3/2}/log^3 n) gates or o(ε^3 n^{5/2}/log^{7/2} n) wires (ε ≫ √(log n/n)); a P function needs MAJ∘THR∘THR with n^{3/2}/log^3 n gates / n^{5/2}/log^{7/2} n wires | D. Kane, R. Williams, STOC 2016; ECCC TR15-188 | peer-reviewed | yes |
| T4 | Andreev, sharpened: worst-case **Ω(n^{3/2}/log^2 n) gates and Ω(n^{5/2}/log^{5/2} n) wires**; average-case: matching ε^2 n^{3/2} up to polylog (explicit O(ε^2 n^{3/2} √log(1/ε)) circuit, Ω(ε^2 n^{3/2}/log^2 n) bound); exact circuit with (5/16 + o(1))n^2 gates (previously O(n^3/log n)); sign-coherent circuits need Ω(n^2/log^3 n) | C. Reitwießner, ECCC TR26-330 (20 Nov 2026) | [PREPRINT] | yes |
| T5 | Depth-d threshold circuits for parity need n^{1+c·θ^{−d}} wires with θ ≈ 2.41 (Impagliazzo–Paturi–Saks 1997); **bootstrapping**: if NC1-complete functions need n^{1+c^{−d}} wires for every c > 1 and large d, then TC0 ≠ NC1 | L. Chen, R. Tell, STOC 2019; ECCC TR18-199 | peer-reviewed | yes (Chen–Tell); IPS97: no (secondary) |
| T6 | Win-win (Williams, FOCS 2024): either read-once 2-DNFs are not simulable by 2^{εn}-size depth-2 exact threshold (ETHR∘ETHR) circuits, or OV in c·log n dimensions is in n^{1+ε} time (⇒ CNF-SAT with O(n) clauses in 2^{n/2+o(n)}, and E^NP ⊄ linear-size series-parallel). "It is already a notorious open problem to prove that E^NP does not have polynomial-size depth-two exact threshold circuits." | R. Williams, "The orthogonal vectors conjecture and non-uniform circuit lower bounds", ECCC TR24-142 | peer-reviewed (FOCS'24 per CKMS abstract) | yes |
| T7 | For all k, NP is not (1/2 + n^{−k})-approximable by n^k-size Sum∘THR | Chen–Ren STOC 2020 (C4) | peer-reviewed | yes |
| T8 | MAJ∘MAJ: exponential lower bounds known (e.g., inner product; Hajnal et al. 1993; Forster 2002 for sign-rank) | Chen–Ren abstract ("exponential lower bounds for MAJ of MAJ are already known") | classic | no (secondary) |
| T9 | Depth-2 ReLU circuit lower bounds via "spiky rank" | Hambardzumyan, Myasnikov, Riazanov, Shirley, Shraibman, ECCC TR26-030 | [PREPRINT] | yes |

### 2.6 Monotone circuits

| # | Statement | Reference | Status | checked |
|---|---|---|---|---|
| M1 | Explicit n-variate monotone function needs monotone circuits of size **exp(n^{1/2−o(1)})** (previous: exp(n^{1/3−o(1)}), Andreev; Harnik–Raz). Also clique needs n^{Ω(k)} for k ≤ n^{1/3−o(1)}, and exp(Ω(n)) monotone *arithmetic* size for a related polynomial | B. P. Cavalar, M. Kumar, B. Rossman, "Monotone circuit lower bounds from robust sunflowers", ECCC TR20-181 (journal version 2022) | peer-reviewed | yes |
| M2 | "Best known [monotone circuit] size lower bound is 2^{Ω̃(√n)}"; polylog-size lifting gadgets would give 2^{Ω̃(n)} | Lovett, Meka, Mertz, Pitassi, Zhang, "Lifting with sunflowers", ITCS 2022; ECCC TR20-111 | conjecture (gadget) | no (statement via search snippet; abstract opened only for the lifting part) |
| M3 | Clique: n^{Ω(k)} for k ≤ n^{1/2−ε}; exp(Ω(n^{1/3−ε})) for a function in P | S. F. de Rezende, M. Vinyals, "Lifting with colourful sunflowers", CCC 2025, LIPIcs 339:36 | peer-reviewed | yes |
| M4 | 2^{αN} for an explicit monotone NP function against monotone **formulas**, switching networks, span programs, comparator circuits (optimal up to α) | T. Pitassi, R. Robere, ECCC TR16-188 (STOC 2017; venue not verified) | peer-reviewed | yes |
| M5 | **Perfect matching** on n-vertex graphs needs monotone circuits of size 2^{n^{Ω(1)}} (previous: Razborov's n^{Ω(log n)}, 1985) | Cavalar, Göös, Riazanov, Sofronova, Sokolov, "Monotone circuit complexity of matching", ECCC TR25-102 (rev. Nov 2025) | [PREPRINT] | yes |
| M6 | Bipartite perfect matching on n-vertex graphs needs **exp(Ω(n^{1/2}))** monotone gates (input length ≈ n^2/4 edges) | A. Rao, "Monotone circuit lower bounds from spread matchings", ECCC TR26-129 (rev. 5, 3 Sep 2026) | [PREPRINT] | yes |
| M7 | Supercritical tradeoff: a monotone function with quasi-poly-size monotone circuits for which every poly-depth monotone circuit has exponential size | Göös, Maystre, Risse, Sokolov, ECCC TR24-186 | — | yes |
| M8 | Monotone OV conjecture holds for monotone circuits: ¬OV_{n, c log n} needs Ω(n^{2−ε}) monotone size | Choudhury, Limaye, Sreenivasaiah, Srinivasan, ECCC TR26-121 | [PREPRINT] | yes |
| M9 | Explicit monotone function with formula-over-multislice-gates size 2^{Ω(n/((w+1)log^2 n))} | Beimel, Nir, ECCC TR26-213 | [PREPRINT] | yes |

### 2.7 Kannan-type fixed-polynomial lower bounds and near-maximum bounds for exponential classes

| # | Statement | Reference | Status | checked |
|---|---|---|---|---|
| K1 | ∀k: Σ2P ⊄ SIZE(n^k) | R. Kannan, Inform. Control 1982 | classic | no (secondary: Aaronson 2006 §1) |
| K2 | ∀k: ZPP^NP ⊄ SIZE(n^k) (from Bshouty et al.'s learning algorithm); ∀k: S2P ⊄ SIZE(n^k) (Cai: S2P ⊆ ZPP^NP, JCSS 73(1), 2007) | Köbler–Watanabe 1998; Cai 2007 | classic | no (secondary: Aaronson 2006 §1, footnote 1) |
| K3 | ∀k: PP ⊄ SIZE(n^k) (Vinodchandran 2005, non-relativizing); PP has no quantum n^k circuits with quantum advice; an **oracle relative to which PP has linear-size circuits**; an oracle where ZPP^NP_∥ has linear-size circuits; Wilson (1985) gave **oracles relative to which NP and P^NP have linear-size circuits** | S. Aaronson, "Oracles are subtle but not malicious", CCC 2006; arXiv cs/0504048; ECCC TR05-040 | peer-reviewed | yes (abstract + intro) |
| K4 | ∀k: **MA/1 ⊄ SIZE(n^k)**; an explicit (MA ∩ coMA)/1 language; average-case version; MA has no n^k arithmetic circuits | R. Santhanam, STOC 2007; SIAM J. Comput. 39(3):1038–1061, 2009; ECCC TR07-005 | peer-reviewed | yes |
| K5 | Equivalences: NP ⊆ SIZE(n^k) for some k ⇔ P^NP_∥ ⊆ SIZE(n^k) for some k ⇔ ONP/1 ⊆ SIZE(n^k) for some k; ∀k: MA ⊆ SIZE(n^k) iff AM ⊆ SIZE(n^k) | L. Fortnow, R. Santhanam, ECCC TR06-157 (CCC 2009 version with R. Williams, "Fixed-polynomial size circuit bounds", not opened) | peer-reviewed | yes (ECCC version) |
| K6 | **P^NP ⊄ SIZE[n^k] ∀k ⇔ (NP ⊆ P/poly ⇒ PH ⊆ i.o.-P^NP/n)**. If NP ⊄ SIZE[n^k] ∀k then for C ∈ {⊕P, PP, PSPACE, EXP}: C ⊆ P/poly ⇒ C ⊆ i.o.-NP/n^ε. If a poly-sparse NP language lacks n^{1+ε}-size circuits, then MA ⊆ i.o.-NP/O(log n), MA ⊆ i.o.-P^{NP[O(log n)]} and NEXP ⊄ SIZE[2^{o(m)}] | L. Chen, D. McKay, C. Murray, R. Williams, ECCC TR19-075 (CCC 2019; venue not verified) | peer-reviewed | yes |
| K7 | O2P ⊄ SIZE(n^k) (Chakaravarthy–Roy, STACS 2006); first **explicit** O2P language ∉ SIZE(n^k) and an O2TIME hierarchy | Gajulapalli, Z. Li, Volkovich, ECCC TR24-049; arXiv 2510.15268 | — | yes (GLV); CR06: no |
| K8 | OMIN (= OL2P, input-oblivious linear-ordering class) **contains hard functions against fixed-polynomial-size circuits**; NP ⊆ P/poly ⇒ PH = OM, where OM ⊆ OMIN ∩ P^{prOMA} ∩ ZPP^{ONP} ("no smaller collapse class with such lower bounds is known") | Hirsch, Volkovich, Williams, ECCC TR26-250 (rev. 2, 22 Nov 2026); Hirsch, Volkovich, "The ultimate Karp–Lipton collapse", ECCC TR26-328 (Nov 2026) | [PREPRINT] | yes |
| K9 | L2P sandwiched: P^{prMA} ⊆ L2P ⊆ P^{prSBP}; P^{prMA} ⊆ S2P (answers Chakaravarthy–Roy); Karp–Lipton collapse for L2P | Hirsch, Volkovich, ECCC TR25-142 (rev. Oct 2026) | — | yes |
| K10 | **Win-win**: either NE contains a language needing Boolean circuits of size ≥ 2^n/(2n) (which implies NP ⊄ SIZE[n^k] ∀k), or VP^0_Z ≠ VNP^0_Z (constant-free Valiant over Z). Via fine-grained PIT: deterministic O(s·t^{d−1}) PIT; improving it by t^ε (even nondeterministically) gives the same Boolean bound or a t^{1+ε/2} arithmetic bound for VNP_F | N. Chukhin, K. Gajulapalli, A. Golovnev, I. Mihajlin, ECCC TR26-313 / arXiv 2611.07972 (5 Nov 2026) | [PREPRINT] | yes |
| K11 | **S2E/1 ⊄ SIZE[2^n/n]** (also Σ2E, (Σ2E ∩ Π2E)/1, ZPE^NP/1); via an FZPP^NP/1 i.o. pseudodeterministic Avoid algorithm; "Our proofs relativize". Previously the smallest class known to need exponential size was Δ3E = E^{Σ2P} (Miltersen–Vinodchandran–Watanabe 1999) | L. Chen, S. Hirahara, H. Ren, STOC 2024; arXiv 2309.12912; ECCC TR23-144 | peer-reviewed | yes |
| K12 | **S2E ⊄ i.o.-SIZE[2^n/n]** (single-valued FS2P Avoid algorithm for all n); a.e. near-maximum for Σ2E ∩ Π2E and ZPE^NP; pseudodeterministic FZPP^NP constructions of Ramsey graphs, rigid matrices, PRGs, two-source extractors, linear codes, hard truth tables, K^poly-random strings | Zeyong Li, STOC 2024; arXiv 2310.17762; ECCC TR23-156 | peer-reviewed | yes |
| K13 | **AMEXP/2^{n^ε} needs 2^n/n** (also against AM ∩ coAM-oracle circuits). Earlier: BPE^{MCSP}/2^{n^ε} (Hirahara–Lu–Ren CCC 2023) | L. Chen, J. Li, J. Liang, ECCC TR24-182 (rev. Jun 2026) | — | yes (HLR: secondary) |
| K14 | **E^{prMA}/1 needs 2^n/n** | H. Ren, R. Williams, ECCC TR26-118 / arXiv 2607.09963 (Jul 2026) | [PREPRINT] | yes |
| K15 | SIZE(2^n/n) is meager in S2E (resource-bounded category) | J. M. Hitchcock, ECCC TR26-068 / arXiv 2605.03306 | [PREPRINT] | yes |
| K16 | Σ2EXP is not in sub-half-exponential size (relativizes). Relative to an oracle, SAT is in "half-exponential" time while EXP ⊆ P/poly. Missing-String reformulations of lower bounds | N. Vyas, R. Williams, ECCC TR24-113 | — | yes |
| K17 | **Open**: NP ⊄ SIZE[n^k] (Williams essay: 93%; MS26 §1.1); P^NP ⊄ SIZE[n^k] (K6); NE ⊄ SIZE[O(n)]; E^NP ⊄ SIZE[2^{εn}] (⇔ Avoid ∈ FP^NP, R3). **E^NP ⊄ SIZE[O(n)]** ("still open, and one has to prove this first!", MW20 §6) is now *claimed* in the strengthened form c·n·√log n, conditional on the Oct-2026 ETH refutation (§4.5) | MW20; MS26; Williams essay; OpenAI Cor. 1.4 (secondary) | open / claimed | yes (MW20, MS26) |

### 2.8 Range avoidance (Avoid) and explicit constructions

Avoid: given C: {0,1}^n → {0,1}^m with m > n, output y ∉ Range(C).

| # | Statement | Reference | Status | checked |
|---|---|---|---|---|
| R1 | Classes PEPP / APEPP defined; Avoid is in TFΣ2P | Kleinberg, Korten, Mitropolsky, Papadimitriou, ITCS 2021; ECCC TR20-153 | peer-reviewed | yes |
| R2 | Constructing a hard truth table is APEPP-complete under P^NP reductions (reinterpreting Jeřábek 2004). EXP^NP contains a language of circuit complexity 2^{n^{Ω(1)}} iff it contains one of complexity 2^n/(2n) | O. Korten, "The hardest explicit construction", FOCS 2021; arXiv 2106.00875 | peer-reviewed | yes |
| R3 | FP^NP equivalence: Avoid ∈ FP^NP ⇔ E^NP needs 2^{Ω(n)} circuits | Korten 2021 / Jeřábek 2004, as stated in Huang–Li–Zhong (R11) | — | no (secondary: HLZ25 abstract) |
| R4 | FP^NP C-Avoid algorithms from circuit-analysis data structures; a non-trivial FP^NP Avoid algorithm for De Morgan formulas; E^NP lower bounds ⇔ circuit-analysis algorithms with E^NP preprocessing; AC0-Avoid with poly stretch ⇒ NC1 lower bounds; NC0_4-Avoid with ℓ = n + n^{o(1)} ⇒ NC1 and branching-program lower bounds; Avoid ∈ FNP ⇔ some proof system breaks every non-uniform proof complexity generator | H. Ren, R. Santhanam, Z. Wang, FOCS 2022; ECCC TR22-048 | peer-reviewed | yes |
| R5 | Unconditional **FP^NP algorithm for ACC0-Avoid**, ACC0-RemotePoint and hard partial truth tables | Y. Chen, Y. Huang, J. Li, H. Ren, ECCC TR23-072 (STOC 2023; venue not verified) | peer-reviewed | yes |
| R6 | NC0_2-Avoid in P. NC0_3-Avoid with m = n + n^{2/3} in FP^NP ⇒ explicit rigid matrices (⇒ superlinear log-depth lower bounds). Deterministic poly-time algorithms for NC0_k-Avoid when m ≥ n^{k−1}/log n | Gajulapalli, Golovnev, Nagargoje, Saraogi, ECCC TR23-021 / arXiv 2303.05044 | — | yes |
| R7 | NC0_4-Avoid hardness for explicit constructions | Guruswami, Lyu, Wang, RANDOM 2022 (with RSW22) | peer-reviewed | no (via R6 abstract) |
| R8 | **Monotone** NC0_3-Avoid in deterministic poly time for m > n (Turán-type hypergraph bounds) | N. Kuntewar, J. Sarma, arXiv 2503.17114 / ECCC TR25-034 | [PREPRINT] | yes |
| R9 | Hardness: under subexponentially secure iO, deterministic poly-time Avoid ⇒ NP = coNP; also under poly-secure iO + a weak NETH variant | R. Ilango, J. Li, R. Williams, STOC 2023; ECCC TR23-038 | peer-reviewed | yes |
| R10 | Under crypto assumptions, Avoid and RemotePoint are hard for nondeterministic search, even for constant-depth circuits | Yilei Chen, J. Li, STOC 2024; ECCC TR23-206 | peer-reviewed | yes |
| R11 | For every constant-depth class C ⊇ AC0: FP^NP C-Avoid[n, n^{1+ε}] ⇔ E^NP ⊄ C-SIZE[2^{o(n)}]; E^NP ⊄ o(2^n/n)-size formulas ⇒ FP^NP NC0-Avoid[n, 2n] | S. Huang, X. Li, Y. Zhong, ECCC TR25-049 (rev. 5, Nov 2025) | — | yes |
| R12 | Demi-bits generators ⇒ Avoid hard for nondeterministic algorithms (resolves a Chen–Li question); hardness even for constant-degree F2 polynomials under LPN-style/Goldreich demi-hardness; dWPHP unprovable in PV1 under AM-secure demi-bits | H. Ren, Y. Wang, Y. Zhong, arXiv 2511.14061 / ECCC TR25-191 | [PREPRINT] | yes |
| R13 | Any decision problem efficiently reducible to Avoid (even randomized, adaptive) is in AM ∩ coAM, so NP-hardness of Avoid collapses PH | S. Ghentiyala, Z. Li, N. Stephens-Davidowitz, ECCC TR25-210 (rev. Sep 2026; an earlier proof was replaced) | [PREPRINT] | yes |
| R14 | Rudich's conjecture (no NP-constructive natural properties vs P/poly) ⇒ the Oracle Derandomization Hypothesis is false and Avoid is average-case hard | R. Ilango, ECCC TR25-190 | [PREPRINT] | yes |
| R15 | Black-box stretch amplification needs depth; **oracle relative to which E ⊄ NC/poly but E^NP ⊆ P/poly** | O. Korten, T. Yang, ECCC TR26-302 (rev. 20 Nov 2026) | [PREPRINT] | yes |
| R16 | Avoid reduces to the Linear Ordering Principle; L2P ⊇ MA; L2E needs 2^n/n | O. Korten, T. Pitassi, FOCS 2024; ECCC TR24-076 | peer-reviewed | yes |
| R17 | Under hardness assumptions: deterministic construction of strings with pKt complexity Ω̃(n) or n − o(n); Avoid for uniform circuit sequences of near-minimal stretch; evidence for explicit Valiant-rigid matrices and Ramsey graphs | O. Korten, R. Santhanam, ECCC TR25-104 | — | yes |
| R18 | Other 2025–26: an MCSP avenue to the AM ∩ coAM bound (Hirsch–Volkovich, arXiv 2512.21764); demi-bits contain many proof complexity generators (Li–Ren–Zhong, arXiv 2609.23228); Avoid-hardness ⇒ time/space/alternation tradeoffs (Z. Li, R. Tell, ECCC TR26-233); prAM fragments derandomizable via Avoid (Z. Li, ECCC TR26-270); Remote Point remoteness Ω(n log n / max{k, log n}) over finite fields (B. L. Volk, ECCC TR26-203) | as listed | [PREPRINT] | yes |

### 2.9 Matrix rigidity (R_A(r) = minimum number of entry changes to bring rank ≤ r)

| # | Statement | Reference | Status | checked |
|---|---|---|---|---|
| X1 | **Explicit (poly-time) record**: R_A(r) = Ω((n^2/r)·log(n/r)) for log^2 n ≤ r ≤ n/2 (Friedman 1993 over finite fields; Shokrollahi–Spielman–Stemann 1997 for totally regular matrices) | via C. Ramya, "Recent progress on matrix rigidity – a survey", arXiv 2009.09460 | classic | no (secondary) |
| X2 | Valiant's target (rank εn, sparsity n^{1+δ}) ⇒ log-depth linear-circuit lower bounds | Valiant 1977 | open | no |
| X3 | P^NP, i.o.: R(2^{(log N)^{1/4−ε}}) ≥ δN^2 over F_q | Alman, Chen, FOCS 2019 | peer-reviewed | no (secondary: Ramya Thm 3.10, BHPT abstract) |
| X4 | FNP, i.o.: δN^2-far from rank 2^{log N/Ω(log log N)} (via rectangular PCPs) | Bhangale, Harsha, Paradise, Tal, FOCS 2020; ECCC TR20-075 | peer-reviewed | yes |
| X5 | P^NP, a.e. (all large n) | Chen–Lyu–Williams FOCS 2020 (C5) | peer-reviewed | yes |
| X6 | P^NP, all large n: R_{H_n}(2^{log^{1−ε} n}) ≥ (1/2 − exp(−log^{(2/3)ε} n))·n^2 | L. Chen, X. Lyu, ECCC TR21-003 | — | yes |
| X7 | FZPP^NP (pseudodeterministic) rigid matrices with near-optimal parameters | CHR24 (K11), Li24 (K12) | peer-reviewed | yes |
| X8 | Non-rigidity: Walsh–Hadamard: changing 2^{εn} entries per row drops rank below 2^{n(1−Ω(ε^2/log(1/ε)))}, so Valiant's approach cannot use Hadamard. Explicit matrices that stay rank ≥ 2^{(log n)^{1−δ}} after n^2/2^{(log n)^{δ/2}} changes would give sub-quadratic AC0∘THR∘THR lower bounds | J. Alman, R. Williams, arXiv 1611.05558 (FOCS 2017; venue not verified) | peer-reviewed | yes |
| X9 | Fourier and circulant matrices are not rigid | Dvir, Liu, ECCC TR19-129 (ToC 2020) | — | no (title only) |
| X10 | **Natural-proofs barrier for linear functions**: under strong trapdoored-matrix assumptions (Vaikuntanathan–Zamir SODA'26; Braverman–Newman TCC'25), natural proofs cannot give > n·polylog n lower bounds for linear maps F^n → F^n; under less standard assumptions (Benhamouda et al. CCS'25) not even superlinear | R. Raz, ECCC TR26-008 (rev. Jul 2026) | [PREPRINT] | yes |
| X11 | Spiky rank lower bounds ⇒ rigidity | ECCC TR26-030 (T9) | [PREPRINT] | yes |
| X12 | Conditional rigidity/tensor-rank/monotone-size hardness under NSETH-type assumptions | Chukhin, Kulikov, Mihajlin, Smirnova, ECCC TR25-038; Chukhin, ECCC TR26-041 | — | yes (TR25-038) |

### 2.10 Hardness magnification thresholds (lower bounds "just beyond" known ones would imply much more)

| # | Statement | Reference | checked |
|---|---|---|---|
| H1 | If MCSP[2^{√n}] cannot be solved on average with zero error by linear (even sub-linear) size formulas, then NP ⊄ Formula[poly]; AC0 m^{1+ε} bounds for (log n)^c-vertex-cover ⇒ NP ⊄ Formula[poly] | I. C. Oliveira, R. Santhanam, FOCS 2018; ECCC TR18-139 | yes |
| H2 | Gap-MCSP[2^{βn}/cn, 2^{βn}] ∉ Circuit[N^{1+ε}] ⇒ NP ⊄ Circuit[poly]; Gap-MKtP ∉ TC0[N^{1+ε}] ⇒ EXP ⊄ … | Oliveira, Pich, Santhanam, CCC 2019; ECCC TR18-158 | yes |
| H3 | search-MCSP[n^c] lacks Õ(N)-size Õ(1)-depth circuits ⇒ NP ⊄ P/poly; search-MCSP[2^{n/c}] lacks N^{1+ε}-size O(1/ε)-depth ACC0 ⇒ NP ⊄ ACC0; streaming version ⇒ P ≠ NP | D. McKay, C. Murray, R. Williams, STOC 2019 | yes |
| H4 | **Every 2^{n^{o(1)}}-sparse L ∈ NP with L ∉ Circuit[n^{1+ε}] ⇒ NP ⊄ SIZE[n^k] ∀k**; analogous for De Morgan formulas, B2-formulas, branching programs, AC0[6], TC0; it suffices to beat n^{1+ε}-time, n^ε-space algorithms with n^ε advice | L. Chen, C. Jin, R. Williams, ECCC TR19-118 (FOCS 2019; venue not verified) | yes |
| H5 | If an n^{α(n)}-sparse NP language (α ≤ log n/log log n) lacks probabilistic circuits with **2n + O(n/log log n)** gates, then NTIME[2^n] ⊄ SIZE[2^{n^{1/5}}] and NP ⊄ SIZE[n^k] ∀k. An O(n)-sparse P language needs ≥ 2n − 2. "Even a sub-linear additive improvement on known circuit size lower bounds would imply NEXP ⊄ P/poly." PRFs in AC0[2] with 2n + o(n) wires (subexp factoring/DDH/RLWE); B2 PRFs with 2n + o(n) gates from subexp OWFs | L. Chen, J. Li, T. Yang, ECCC TR22-086 | yes |
| H6 | **Locality barrier**: magnification problems have very efficient circuits with small-fan-in oracle gates, and many lower-bound techniques extend to such oracle circuits; some magnification instances do sidestep natural proofs | Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam, ITCS 2020 / J. ACM 2022; ECCC TR19-168 | yes (abstract) |
| H7 | Distinguisher-based magnification. Fixed-poly formula lower bounds for NP follow from slightly superlinear formula lower bounds for *approximating* any sufficiently sparse NP problem. Thresholds below known lower bounds, sharp; a uniform MCSP magnification that "seems to sidestep the localization barrier" | A. Atserias, M. Müller, arXiv 2503.24061 (2025) | yes |
| H8 | If NC1 = TC0 then certain NC1-complete problems have n^{1+ε}-size O(1/ε)-depth TC0 circuits for every ε > 0 (Allender–Koucký, J. ACM 2010), so such lower bounds would separate | via Williams essay §2.9 | no (secondary) |

---

## 3. Key techniques and the barriers they hit or evade

| Technique | Where it works (best result) | Barriers it hits | Barriers it evades / notes |
|---|---|---|---|
| **Gate elimination** (+ potential functions, affine/quadratic substitutions, cyclic circuits, 2026: "parameter re-parameterization") | B2 4n − O(log n) [G1]; U2 5n − o(n) [G8] | Technique-specific: GHKK18 (< 5n for substitution steps) [GL1]; GKW21 ("inherently < 5n") [GL2]; Amano–Tarui (mixed functions ≤ 5n) [G10]; MS26 believe ~4n near the limit [GL3]. Locality: I did not verify whether CHOPRS's analysis covers gate elimination | Not known to be natural: being an affine disperser for dim O(log n) is dense, but the best known test takes N^{O(log log N)} time (MS26 §1.5). Non-relativizing in the trivial sense (it inspects gates). Constructive: proofs yield refuters (MS26 Thm 4.1; Carmosino–Dang–Jackman 2026) |
| **Random restrictions / switching lemma / shrinkage** | AC0 Håstad; formulas n^{3−o(1)} [F1]; 2026 AC0 records combine switching with OpenAI's restriction lemma + sparsification [A1–A2] | Natural proofs (RR97): these proofs are natural. Locality barrier: restriction-based formula and AC0 bounds extend to local-oracle circuits, so they cannot reach magnification thresholds [H6] | — |
| **Polynomial approximation** (Razborov–Smolensky; probabilistic polynomials; 2026 basis method) | AC0[p] [C8–C9] | Natural; locality (CHOPRS treat the approximation method; see also Pich, "Localizability of the approximation method", arXiv 2212.09285, title only) | — |
| **Algorithmic method** (non-trivial SAT/#SAT/CAPP ⇒ lower bound via NTIME hierarchy + succinct PCPs/local reductions + easy witnesses) | NEXP, NQP ⊄ ACC0 [C1–C2]; E^NP ⊄ THR∘THR[n^{2.5−ε}] [T1]; a.e./average-case [C3–C5] | Lower bounds land in big classes (NEXP, NQP, E^NP), not NP/P. For linear size one needs E^NP (no easy-witness lemma for linear size; JMV open problem). Vyas–Williams 2024 give oracle results limiting relativizing versions [K16] | Evades natural proofs (uses diagonalization: the hard function is not characterized by a large constructive property). Non-relativizing via PCPs; algebrization status: not established by me (checked: no) |
| **Diagonalization + Karp–Lipton** (Kannan-type) | Σ2P, ZPP^NP, S2P, O2P, MA/1, OMIN ⊄ SIZE[n^k] [K1–K8] | Relativization: Wilson's oracles where NP and P^NP have linear-size circuits [K3], so relativizing proofs cannot give NP or P^NP ⊄ SIZE(n). CMMW19: for P^NP, Karp–Lipton-style collapses are *necessary* [K6] | Evades natural proofs |
| **Iterative win-win + Korten's reduction + PCPs** (2023–26) | S2E, ZPE^NP, Σ2E, AMEXP/2^{n^ε}, E^{prMA}/1 need 2^n/n [K11–K14] | CHR24 relativizes, so it cannot alone give E^NP or NE bounds that fail relative to some oracle. Korten–Yang 2026 oracle (E^NP ⊆ P/poly while E ⊄ NC/poly) [R15] limits black-box amplification | Evades natural proofs |
| **Lifting / sunflowers / approximation method** (monotone) | exp(n^{1/2−o(1)}) monotone circuits [M1]; matching [M5–M6]; 2^{Ω(N)} monotone formulas [M4] | Monotone only (Razborov 1989: the approximation method probably does not extend to general circuits; per Williams JACM 2014 §1) | — |
| **Rank/sign-rank/discrepancy, Littlewood–Offord** (threshold circuits) | Kane–Williams/Reitwießner [T3–T4] | Natural-proof-type limits for TC0 via Miles–Viola's TC0 candidate F3 (n^{1+ε} size) | — |
| **Hardness magnification** | conditional only [H1–H7] | Locality barrier [H6] | Some instances overcome natural proofs [H6]; Atserias–Müller "seem to sidestep localization" [H7] |
| **PIT ⇒ lower bounds (Kabanets–Impagliazzo), fine-grained** | win-win NE / VP^0_Z [K10] | Gives win-wins, not unconditional Boolean bounds | — |

General barriers relevant to this area (with what I verified):
- **Natural proofs** (Razborov–Rudich 1997). For *linear-size* bounds the barrier is unclear. Assuming Miles–Viola's
  SPN candidate F2 (computable in n·log^{O(1)} n size, exponentially secure against linear/differential
  cryptanalysis) is a PRF, no natural proof beats n·polylog n for general circuits. Their candidate F3 (TC0,
  n^{1+ε}) gives the same for TC0 (ECCC TR11-076, checked: yes; MS26 §1.5 discussion, checked: yes). Raz 2026
  extends this to linear functions [X10].
- **Relativization** (BGS75): Wilson's oracles [K3]. MS26 argues it is "not relevant" to gate elimination, which
  uses gate structure. Both views are recorded.
- **Algebrization** (Aaronson–Wigderson 2009): by memory, AW09 show that P^NP ⊄ SIZE(n) (hence NP ⊄ SIZE(n)) needs
  non-algebrizing techniques. checked: no.
- **Locality** (CHOPRS 2020) [H6]. **GCT no-go** (BIP19): not relevant to Boolean circuits.

---

## 4. Dedicated section: Williams' challenge (23 Nov 2026)

Source: the director's screenshots, as summarized in `research/survey/00-director-sources.md` §2 (secondary; I
could not open the post). The challenge reads: "Prove that SAT on instances of length L doesn't have L^{1.01}
size circuits first!"

### 4.1 What the statement is and what it implies
- Target: CNF-SAT (standard encoding, input length L) ∉ SIZE[L^{1.01}] for infinitely many L. It is a
  *fixed-polynomial* lower bound for one NP problem.
- Trivially it implies **NP ⊄ SIZE[n^{1.01}]**, hence E^NP ⊄ SIZE[n^{1.01}] (NP ⊆ E^NP), hence **E^NP ⊄
  SIZE[O(n)]**. Murray–Williams call the last one "still open, and one has to prove this first!" (MW20 §6, checked:
  yes; also Williams 2010 footnote 5: "linear size circuit lower bounds are not known for this class"). It is now
  *claimed* via the ETH refutation (§4.5). That removes the first stepping stone but not the gap from n·√log n to
  n^{1.01}.
- It does **not** obviously imply NP ⊄ SIZE[n^k] for all k, or NEXP ⊄ P/poly. SAT is not sparse, so the magnification
  theorems H4/H5 do not apply to SAT itself. I found no magnification theorem for SAT itself.
- Because SAT is complete for NTIME[n] under quasi-linear reductions, NTIME[n] ⊄ SIZE[n^{1.02}] would imply
  SAT ∉ SIZE[L^{1.01}]. Status: `informal-argument` (lab, standard reduction; not red-teamed).

### 4.2 Best known bounds as a function of input length L

| Model | Best known for *some* NP (in fact P) problem | For SAT itself | Gap to L^{1.01} |
|---|---|---|---|
| B2 circuits | 4L − O(log L) [G1, preprint, AI]; 3.1L − o(L) peer-reviewed [G2] | No SAT-specific bound beyond the trivial "depends on (almost) all input bits" ≈ L was found. Projection reductions from G1's function transfer only sublinear bounds, because the Tseitin encoding of a size-s circuit has length ≈ s·log s (`informal-argument`, lab) | needs ω(L): any *superlinear* growth; constant-factor progress never reaches it |
| U2 circuits | 5L − o(L) [G8] | as above | same |
| De Morgan formulas | Ω(L^3/(log^2 L log log L)) [F1] | **L^{3−o(1)}**. Lab observation: Andreev's function has O(n)-size circuits; its Tseitin CNF with the input fixed by unit clauses is a *projection* of the input of length L = O(n log n); formula size is preserved under projections. Williams 2010 fn. 5 makes the analogous remark for E^NP. (`informal-argument`; folklore-level, do not claim as new) | already beyond L^{1.01}, but formulas are a weak model |
| AC0 depth d | 2^{Ω((n log n)^{1/(d−1)})} [A2] | SAT ∉ AC0 by the projection from parity (`informal-argument`) | n/a |
| ACC0, TC0 | No super-polynomial bound for any NP problem. Explicit (P) function vs THR∘THR: Ω(n^{3/2}/log^2 n) gates [T4]; NP is not (1/2 + n^{−k})-approximable by n^k-size Sum∘THR [C4]. Larger classes: NQP ⊄ ACC0 [C2], E^NP ⊄ THR∘THR[n^{2.5−ε}] [T1] | **open whether SAT ∈ ACC0** (NP ⊄ ACC0 open, MW20 §6) | n/a |
| uniform (time–space) | — | SAT ∉ TISP(n^{2cos(π/7)}, n^{o(1)}), 2cos(π/7) < 1.81, and current techniques cannot beat this exponent (Buss–Williams 2012) | via Williams essay §2.3; checked: no (secondary) |

### 4.3 Known obstacles to an L^{1.01} bound (each with citation)
1. **Gate elimination stalls below 5n** [GL1–GL3]. The best new idea (MS26) reached 4n and its authors think this
   is near the limit.
2. **Natural proofs**, if Miles–Viola-type quasi-linear PRFs are secure: no natural proof gives lower bounds above
   n·polylog n, let alone n^{1.01} (§3). An L^{1.01} proof must therefore be non-natural (not constructive or not large), like
   diagonalization-based arguments.
3. **Relativization**: NP (and P^NP) have linear-size circuits relative to Wilson's oracle [K3]. So
   Kannan-style diagonalization alone cannot give NP ⊄ SIZE[n^{1.01}].
4. **Magnification + locality**: for 2^{n^{o(1)}}-sparse NP languages, an n^{1+ε} bound (H4), and for
   n^{α(n)}-sparse ones even 2n + O(n/log log n) against probabilistic circuits (H5), would already give NP ⊄
   SIZE[n^k] ∀k (hence NEXP ⊄ P/poly; Williams essay §2.4). The locality barrier [H6] explains why known techniques
   fail on exactly these sparse problems. Consequence for the lab: an "L^{1.01}"-style lower bound is plausibly
   as hard as fixed-polynomial lower bounds for NP, if one aims it at a sparse problem.
5. **Algorithmic method mismatch**: to get NP ⊄ SIZE[n^k] one needs 2^{(1−ε)n}-time (Gap-)UNSAT for n-input,
   2^{εn}-size circuits (MW20 Thm 1.1 [C2]); MS26 §1.3 cites the same consequence. The connections are not tight in
   the size parameter (MS26 §1.3).
6. **Depth reductions** only reach linear bounds: GKW21 gives 3.9n from depth-3 2^{n−o(n)} bounds [GL2]. Valiant's
   depth-3 route to superlinear bounds needs 2^{ω(n/log log n)}; the current record is 2^{Ω(√(n log n))} [A2, A8].

### 4.4 Which circuit-analysis algorithms would imply new lower bounds (verified statements)

| Algorithm (hypothesis) | Consequence | Source | checked |
|---|---|---|---|
| CircuitSAT on n vars, poly(n) size in 2^n·poly/s(n), s superpoly (or nondeterministic CAPP) | NEXP ⊄ P/poly | Williams 2010/2013 (Thm 1.1); essay §2.2 | yes |
| CircuitSAT in O(2^{(1−δ)n} poly(m)) (co-non)deterministic time | E^NP ⊄ SIZE[2^{εn}] for some ε | Williams 2010 Thm 1.2 | yes |
| Formula-SAT (n^c connectives) in 2^n poly/s(n) | E^NP ⊄ poly-size formulas | Williams 2010 §1 | yes |
| Gap-C-UNSAT, n-input 2^{εn}-size, nondet. O(2^{(1−ε)n}) | ∃c ∀k NTIME[n^{ck^4/ε}] ⊄ C[n^k] (NP fixed-poly bounds) | MW20 Thm 1.1 | yes |
| Gap-C-UNSAT, 2^{n^ε}-size, 2^{n−n^ε} | NQP ⊄ C | MW20 Thm 1.2 | yes |
| SAT of linear-size / linear series-parallel / linear log-depth circuits, or quasipoly SYM∘AND, in 2^n/n^{ω(1)} | E^NP ⊄ the same class | JMV Cor. 2 (Inf. Comput. 2018; ECCC TR13-099) | yes |
| **ETH false** (∀ε: 3SAT in 2^{εn}) | **E^NP has no linear-size circuits** | **Williams 2010/2013 Thm 6.1**; JMV Cor. 3(1′) | yes (Thm 6.1 text) |
| SETH false (∃ε < 1 ∀k: k-SAT in 2^{εn}) | E^NP ⊄ linear-size series-parallel | JMV Cor. 3(2′) | yes |
| ∃α: n^α-SAT in 2^{n−ω(n/log log n)} | E^NP ⊄ linear-size log-depth | JMV Cor. 3(3′) | yes |
| NSETH false; e.g., a 1.9^n nondeterministic CNF-UNSAT algorithm | E^NP ⊄ linear-size (Valiant) series-parallel | JMV; Carmosino et al. ITCS 2016 (ECCC TR15-148); MW20 §6 | yes |
| 3SAT deterministic in c^n with c < 2^{1/10} | E^NP ⊄ SIZE[3n] (Boolean) | Ben-Sasson–Viola ICALP 2014, as reported in JMV §1 | no (secondary: JMV §1) |
| 3SAT in c^n with c < 2^{1/7} | a 2-output f ∈ E^NP needs 3n gates (JMV Cor. 6). **Discrepancy**: MS26 §1.3 states d < 2^{1/7} gives a 3n bound for a *Boolean* f ∈ E^NP | JMV Cor. 6 vs MS26 | both opened |
| depth-(d+2) threshold SAT, n^c size, 2^n/n^{ω(1)} | NE ⊄ poly-size depth-d threshold | JMV Cor. 4 | yes |
| CAPP for ⊕2∘THR∘THR of size n^α in 2^n/n^{ω(1)} | E^NP ⊄ THR∘THR[n^α] | Chen–Williams 2019; Bathie–Williams 2024 (as cited in CTW26 §1.1.2) | no (secondary: CTW26) |
| Non-trivial nondeterministic CAPP for S-size C | (1/2 + 1/n^{ω(1)}) average-case lower bounds for nondeterministic time vs C | Chen–Ren 2020 [C4] | yes |
| Quantified derandomization of n^{1+1.61^{−d}}-wire TC0 | NEXP ⊄ TC0 | Chen–Tell 2019 [T5] | yes |
| OV in n^{1+ε} for c log n dims | E^NP ⊄ linear series-parallel (and SETH false) | Williams 2024 [T6] | yes |
| Nondeterministic PIT improving O(s t^{d−1}) by t^ε | NE needs 2^n/(2n), or VNP_F needs t^{1+ε/2} | Chukhin et al. 2026 [K10] | yes |

### 4.5 Does the claimed Oct-2026 sub-exponential 3-SAT algorithm affect this area?

**Status of the claim** (detail belongs to the ETH survey; this is a quick check only).
- Anthropic, "A 2^{o(n)} Time Algorithm for 3-SAT", Hexagon 2610.00577v1 (27 Oct 2026). The landing page abstract
  claims a **deterministic** 2^{o(n)} algorithm that counts #3-SAT. It says the result "has been formalized in Lean 4",
  labels the text "Primarily AI-generated", and says the core algorithm was found 16 Oct 2026 by an internal Claude
  model. checked: yes (abstract page only).
- OpenAI, "The Exponential Time Hypothesis is False" (17 Oct 2026, rev. 25 Oct 2026), hosted on GitHub
  (openai/math). I could not open it (GitHub access not enabled for this session). Per Dias–Lima (arXiv
  2611.00517): it gives deterministic counting for k-CNF in 2^{O_k(n log log n/√log n)}, and 2^{O(n/√log n)} at
  bounded clause density. The body proves the weaker exponent n(log log n)^2/√log n. The proof certifies no
  speed-up for any writable input (no gain unless log2(n+m) > 10^9). Per the MIT Hardness Group (arXiv 2611.02650):
  both algorithms count k-CNF in 2^{O(n log log n/√log n)}; they propose replacing ETH with SH/Weak ETH.
  checked: no for the OpenAI preprint itself.
- The community review is not finished (director's notes). Per `01-eth-refutation.md` (secondary), no flaw had
  been reported as of 23 Nov 2026 and several people had re-run both Lean proofs. The organizers say their review
  is "not certification". The deterministic 2^{o(n)} claim is therefore `claimed`, not established.

**Consequences, if the claim is correct.**
1. **Known theorem, becomes unconditional: E^NP ⊄ SIZE[O(n)].** Williams 2010/2013 Thm 6.1 (opened): "If the
   Exponential Time Hypothesis is false, then E^NP does not have linear size circuits." JMV Cor. 3(1′) says the same.
   This would be the first superlinear lower bound against general fan-in-2 circuits for E^NP. Before the claim it
   was open (MW20 §6; Williams 2010 fn. 5). Anthropic §1.2 also says the previous best for E^NP over the full binary
   basis was 3.1n − o(n) (per `01-eth-refutation.md`). **This is already written up by the algorithm authors**:
   OpenAI's paper states it as Cor. C.1, applying [Wil10, Thm 6.1], and Anthropic §7 does too (per
   `01-eth-refutation.md` row F14, which that scout checked; I could not open the OpenAI file).
   **Correction to my own search.** My arXiv/ECCC/blog searches did not surface this. I learned it from the
   parallel ETH survey, which I read but did not modify.
2. **The quantitative version is also already known; do not re-derive it.** OpenAI's Cor. 1.4 / App. C.1 combine the
   fixed-density bound 2^{O(n/√log n)} with the Jahanjou–Miles–Viola local reductions. Result: there are L ∈ E^NP
   and c > 0 with C_L(n) > c·n·√(log n) for infinitely many n (any fan-in-2 gates). checked: no (secondary:
   `01-eth-refutation.md` F14). My own sketch of the same argument (δ·n·√log n) matches it and adds nothing new.
   Extensions to other gate bases: Ω(m·√log m / log log m) gates over unbounded AND/OR plus binary XOR (from
   Anthropic's counting theorem), and Ω(m·√log m) for a bounded binary basis with a linear budget of arbitrary XOR
   and symmetric gates, i.o. (M. Wu, M. Wang, "Circuit lower bounds for extended gate bases from subexponential
   counting", arXiv 2611.02560, 2 Nov 2026; checked: yes, abstract). The ETH survey notes (lead-scout inference
   there) that the Williams/JMV transfer part is **not formalized** in Lean, while Anthropic's counting bound is.
   Any improvement a(n) in the sparse-3-SAT exponent improves the E^NP bound to about n·a(n) in lock-step.
3. **SETH and NSETH also fall** (standard: SETH ⇒ ETH; a deterministic 2^{o(n)} k-SAT algorithm decides k-UNSAT, so
   NSETH fails). So JMV Cor. 3(2′) and the NSETH-based series-parallel bound become unconditional, but item 1
   subsumes them for general circuits. Conversely, results that *assume* ETH, rETH, NETH or NSETH lose their
   hypothesis. Examples to re-check: ETH-hardness of learning or approximating monotone circuit size (ECCC
   TR26-128), ETH-hardness of partial MBPSP (ECCC TR24-117), the NETH-variant part of ILW23 [R9], NSETH-based
   rigidity/tensor-rank results [X12], and rETH/NETH derandomization (Chen–Rothblum–Tell–Yogev, ECCC TR19-169).
4. **No known theorem turns it into NP, NEXP, ACC0, THR∘THR or "SAT ∉ SIZE[L^{1.01}]" bounds.** The algorithmic
   method needs savings for circuits with n inputs and poly(n) or 2^{εn} gates. A 2^{o(N)} algorithm in the
   number N of Tseitin variables (≈ gates) gives nothing there. (`informal-argument`, lab; consistent with MW20 Thm 1.1.)
5. **Discrepancy to note.** MS26 (3 Nov 2026) writes "we currently do not have non-trivial satisfiability algorithms
   even for linear-size circuits". If the ETH refutation holds, Tseitin + 2^{o(N)} 3-SAT gives exactly such an
   algorithm (2^{o(n)} for size-cn circuits), so that sentence predates or ignores the claim. Both sources are recorded.

---

## 5. Open sub-problems ranked by tractability × impact

Scores 1–5 (T = tractability for this lab now, I = impact). "Open per" names a source stating it is open; the
"last progress" date is the newest result I found.

| Rank | Problem | T | I | T×I | Why (one line) | Open per | Last progress |
|---|---|---|---|---|---|---|---|
| 1 | **Lean-formalize the transfer "fast sparse 3-SAT ⇒ E^NP ⊄ SIZE[c·n·√log n]"** (Williams Thm 6.1 + JMV local reductions), composed with Anthropic's already Lean-checked counting bound, to get an end-to-end machine-checked superlinear E^NP bound | 3 | 4 | 12 | The bound itself is known (OpenAI Cor. 1.4; Anthropic §7) but its transfer part is unformalized (per 01-survey). It would be the first end-to-end Lean-checked superlinear general-circuit lower bound, squarely on the lab's formalization mission. Needs NTIME hierarchy + succinct/local reductions in Lean (heavy) | MW20 §6 (E^NP ⊄ SIZE[O(n)] open before the claim); 01-eth-refutation.md §2.6 ("not formalized") | algorithm claims 17–27 Oct 2026; Wu–Wang 2 Nov 2026 |
| 2 | **Depth-3 AC0: 2^{n^{1/2+ε}} for an explicit (or E^NP) function**; or pin down the depth-3 complexity of Goldreich–Tal f_n (now between 2^{Ω(√(n log n/log log n))} and 2^{O(n^{2/3})}) | 3 | 4 | 12 | Fresh techniques (restriction lemma + sparsification + short point lists) moved it three times in 6 weeks; on Valiant's route | Chen–Lyu TR21-003 ("notoriously hard"); TR26-248 (upper bound 2^{O(n^{2/d})}) | 19 Oct 2026 (Li–Zhong) |
| 3 | **Lean 4 formalization of B2/U2 gate-elimination bounds** (Schnorr 2n − O(1), U2 3n − 3 for parity, Demenkov–Kulikov 3n − o(n)), reusing formalcs/circuit-complexity | 4 | 3 | 12 | No B2 lower-bound formalization found; constructive proofs (refuters) suit Lean; feeds the formalization track | none states it open (gap found in my searches) | Sep 2026 (Lean AC0 formalization) |
| 4 | **Fixed-poly lower bounds for smaller classes**: kill the algebraic branch of the NE/VP^0_Z win-win, or push OMIN-type bounds toward ONP or P^NP | 2 | 5 | 10 | Win-win and OMIN results are days old; any collapse of a branch gives NP ⊄ SIZE[n^k] | CMMW19 (K6); HV26 TR26-328 ("no smaller collapse class with such lower bounds known"); TR26-313 | 22 Nov 2026 |
| 5 | **Circuit complexity *upper* bounds for explicit affine dispersers** (linear size? what constant?) | 3 | 3 | 9 | Would bound the reach of the 3.1n/4n method; unexplored | MS26 §1.5 ("currently unknown if affine dispersers are computable by B2 circuits in linear size") | none found |
| 6 | **NC0_3-Avoid in FP^NP for stretch between n + n^{2/3} and n^2/log n** (monotone case solved for m > n) | 3 | 3 | 9 | Concrete combinatorics (Turán-type); at m = n + n^{2/3} it gives rigid matrices | GGNS23 (R6); Kuntewar–Sarma 2025 (R8) | Mar 2025 |
| 7 | **THR∘THR: E^NP needs n^{3+ε} gates (or superpolynomial)**; push CTW's CAPP algorithm | 2 | 4 | 8 | New CAPP technique just broke the quadratic wall; superpolynomial would be a TC0 milestone | CTW26 §1; Williams 2024 [T6] ("notorious open problem") | Mar 2026 (gates), Sep 2026 (wires) |
| 8 | **Correlation o(1) against F2 polynomials of degree d = ω(√n)** for an explicit function | 2 | 4 | 8 | Next step after CHLLTV; d = n^{1/2+ε} would give the depth-3 E^NP bound of rank 2 | CHLLTV TR26-208 §5 | Oct 2026 |
| 9 | **NP ⊄ ACC0** via a Gap-ACC-UNSAT algorithm in 2^{(1−ε)n} on 2^{εn}-size circuits | 2 | 4 | 8 | Concrete algorithmic target named by MW; the Yao–Beigel–Tarui blow-up is the obstacle | MW20 §6 | 2022 (Chen TR22-183) |
| 10 | **B2 beyond 4n / U2 beyond 5n** (or limits for MS26's parameter-substitution gate elimination) | 3 | 2 | 6 | AI-assisted case analysis is cheap now; constant-factor gains only | MS26 §1.5 (limits of generalized elimination "unclear") | 3 Nov 2026 |
| 11 | **Andreev vs THR∘THR: close Ω(n^{3/2}/log^2 n) vs (5/16)n^2** (mixed-sign circuits needed below n^2) | 3 | 2 | 6 | Concrete, explicit function; Kane–Williams asked for tight bounds | Reitwießner TR26-330 | 20 Nov 2026 |
| 12 | **Monotone: exp(n^{1−ε}) for an explicit function** (polylog lifting gadgets) | 2 | 3 | 6 | Clear conjecture (LMMPZ); matching results show new sunflower lemmas still pay off | LMMPZ22 (M2) | Sep 2026 (Rao) |
| 13 | **Explicit rigid matrices with Valiant's parameters** (even in P^NP) | 1 | 5 | 5 | Decades stuck; natural-proofs barrier for linear functions [X10] | Ramya 2020; Raz 2026 | 2021 (Chen–Lyu) |
| 14 | **De Morgan formulas n^{3+ε}** (KRW), or MCSP[(log n)^c] needing n^{2+ε} probabilistic formulas | 1 | 5 | 5 | Stuck since 1998 up to logs; the sharp-threshold version would give NP ⊄ Formula[poly] | GKW21 abstract ("stuck at around n^{3−o(1)} for decades"); CJW20 | 2016 (Tal); 2024 (KRW variants) |
| 15 | **Sparse-NP magnification: a probabilistic 2n + ω(n/log log n) bound for an n^{α}-sparse NP language** (2n − 2 is known for a sparse P language) | 1 | 5 | 5 | Tiny-looking gap, but the locality barrier applies; would give NEXP ⊄ P/poly | CLY22 (H5) | 2022 |
| 16 | **Williams' challenge: SAT ∉ SIZE[L^{1.01}]** | 1 | 5 | 5 | Needs a superlinear bound for an explicit (NP) function. The prerequisite E^NP ⊄ SIZE[O(n)] is now claimed (c·n·√log n) via the ETH refutation, but that technique cannot go past ~n·√log n | Williams thread (secondary); MW20 §6 | Oct 2026 (E^NP step, claimed) |

---

## 6. Known traps (approaches known to fail or be blocked)

1. **Plain gate elimination for superlinear bounds.** Limited below 5n [GL1, GL2]; Lachish–Raz-type arguments on
   mixed functions are capped at 5n by Amano–Tarui [G10]; MS26 think 4n is near the limit [GL3].
2. **Using Majority (or any symmetric function) to beat parity in AC0.** Lecomte–Ramakrishnan 2026 [A7]: every
   symmetric function has depth-d circuits of size 2^{O(n^{1/(d−1)})}.
3. **Hadamard, Fourier, circulant (and other Kronecker-structured) matrices for Valiant rigidity.** Not rigid enough:
   Alman–Williams [X8]; Dvir–Liu [X9]. Also Dvir–Edelman (arXiv 1708.01646) and Kivva (arXiv 2103.05631) on non-rigidity
   of structured matrices (titles seen, not opened).
4. **Natural properties for lower bounds above n·polylog n** (general circuits), assuming Miles–Viola PRF
   candidates (§3); for linear functions, Raz 2026 [X10].
5. **Relativizing (pure diagonalization) proofs of NP ⊄ SIZE(n) or P^NP ⊄ SIZE(n).** Blocked by Wilson's oracles
   [K3]. For E^NP from E-hardness via black-box Avoid amplification: Korten–Yang's oracle [R15].
6. **Proving P^NP ⊄ SIZE[n^k] "without" a Karp–Lipton theorem.** Impossible in the sense of CMMW19: the two are
   equivalent [K6].
7. **Magnification attempted with "local" techniques** (restrictions, approximation method). Locality barrier [H6].
8. **Expecting a deterministic poly-time Avoid algorithm.** Implies NP = coNP under iO [R9]. **Expecting Avoid to be
   NP-hard**: collapses PH [R13].
9. **Easy-witness arguments at linear size.** No easy-witness lemma for linear-size circuits is known (JMV §1 raise
   it as open), so linear-size algorithmic-method bounds land in E^NP, not NE.
10. **Expecting the 2^{o(n)} 3-SAT algorithm to give NP/NEXP circuit lower bounds.** It gives only E^NP bounds of
    about n·√log n (§4.5). The cost is exponential in variables plus gates, so nothing is gained for n^{1+ε}-size
    circuits (per 01-eth-refutation.md §2.6). Expecting practical speed-ups also fails (Dias–Lima: no gain for any
    writable instance).
11. **Building on ETH/NETH/rETH/NSETH-conditional results** without checking the Oct-2026 refutation (§4.5, item 3).
    The MIT Hardness Group propose SH/Weak ETH as replacements (arXiv 2611.02650).
12. **Symmetric torus polynomials for Majority ∉ ACC0.** Shown weaker than asymmetric ones [C10].
13. **Lab-specific re-derivation trap.** "SAT needs L^{3−o(1)} De Morgan formulas" and "SAT ∉ AC0" follow from
    projections of Andreev/parity (folklore-level, §4.2). Do not spend effort on them or present them as results.

14. **Re-deriving the E^NP ⊄ SIZE[c·n·√log n] corollary of the ETH refutation.** It is already in OpenAI's paper
    (Cor. 1.4/C.1) and Anthropic §7, with extended-basis versions by Wu–Wang (arXiv 2611.02560). Build on these
    (e.g., formalize them) rather than reproving.
---

## 7. People and groups (names seen on the 2024–2026 papers cited above)

- **General circuits / gate elimination:** Om Swostik Mishra, Rahul Santhanam (Oxford) [G1]; Jiatu Li, Tianqi Yang
  [G2]; Marco Carmosino, Ngu Dang, Tim Jackman [G11]; Alexander Golovnev, Alexander S. Kulikov, Edward A. Hirsch,
  Magnus G. Find [G3, GL1]; R. Ryan Williams [GL2].
- **AC0 / AC0[p]:** Nikolai Chukhin (JetBrains Research) [A1, A10]; Xin Li, Yan Zhong [A2, R11, R12]; Victor
  Lecomte, Prasanna Ramakrishnan [A7]; Oliver Korten [A4, R15]; Haoxing Lin [A10]; Eshan Chattopadhyay, Pooya
  Hatami, Chin Ho Lee, Shachar Lovett, Avishay Tal, Emanuele Viola [C9]; Artur Riazanov, Anastasia Sofronova, Dmitry
  Sokolov [C12]; OpenAI (internal model) [A3].
- **ACC0 / algorithmic method:** Lijie Chen, Hanlin Ren, Xin Lyu, Ryan Williams, Cody Murray [C2–C6]; Vaibhav
  Krishan, Sundar Vishwanathan, Jayalal Sarma [C10, C11].
- **Threshold circuits:** Lijie Chen, Avishay Tal, Yichuan Wang [T1]; Dev Nag [T2]; Christian Reitwießner [T4];
  Ryan Williams [T6]; Lianna Hambardzumyan, Konstantin Myasnikov, Artur Riazanov, Morgan Shirley, Adi Shraibman [T9].
- **Monotone:** Anup Rao [M6]; Bruno Pasqualotto Cavalar, Mika Göös, Artur Riazanov, Anastasia Sofronova, Dmitry
  Sokolov [M5]; Susanna F. de Rezende, Marc Vinyals [M3]; Gilbert Maystre, Kilian Risse [M7]; Tameem Choudhury,
  Nutan Limaye, Karteek Sreenivasaiah, Srikanth Srinivasan [M8]; Amos Beimel, Oded Nir [M9].
- **Fixed-poly / exponential classes:** Edward Hirsch, Ilya Volkovich, Ryan Williams [K8, K9]; Nikolai Chukhin,
  Karthik Gajulapalli, Alexander Golovnev, Ivan Mihajlin [K10]; Hanlin Ren, Ryan Williams [K14]; Lijie Chen, Jiatu Li,
  Jingxun Liang [K13]; Zeyong Li [K12, R18]; Lijie Chen, Shuichi Hirahara, Hanlin Ren [K11]; John M. Hitchcock
  [K15]; Nikhil Vyas [K16].
- **Range avoidance:** Oliver Korten, Toniann Pitassi, Tianqi Yang [R15, R16]; Surendra Ghentiyala, Zeyong Li, Noah
  Stephens-Davidowitz [R13]; Hanlin Ren, Yichuan Wang, Yan Zhong [R12]; Rahul Ilango [R14]; Shengtang Huang, Xin Li,
  Yan Zhong [R11]; Neha Kuntewar, Jayalal Sarma [R8]; Roei Tell [R18]; Ben Lee Volk [R18]; Rahul Santhanam [R17].
- **Rigidity / barriers:** Ran Raz [X10]; Nikolai Chukhin, Alexander Kulikov, Ivan Mihajlin, Arina Smirnova [X12].
- **Magnification:** Albert Atserias, Moritz Müller [H7].
- **E^NP bounds from the ETH refutation:** Mengyang Wu, Minghao Wang (arXiv 2611.02560).
- **Fine-grained after ETH:** MIT Hardness Group (Josh Brunner, Erik D. Demaine, Fabian Frei, Timothy Gomez, Markus
  Hecher, Jeffery Li, Jayson Lynch); Fabio Dias, Yvens Lima (§4.5).
- **Formalization:** Saint Wesonga [Lean, §8]; René Thiemann [Isabelle]; Dev Nag [Lean]; Gregory Morse [Lean].

---

## 8. Formalization status (Lean / Coq / Isabelle)

| Artifact | What is formalized | System | Notes | checked |
|---|---|---|---|---|
| S. Wesonga, "Formalizing PARITY circuit lower bounds in Lean", arXiv 2609.24188 (Sep 2026); repo github.com/formalcs/circuit-complexity | Håstad: for fixed d ≥ 2, depth-≤d formulas and DAG circuits for PARITY need exp(Ω_d(n^{1/(d−1)})) size; PARITY has poly-size log-depth formulas (NC1 ⊄ AC0 for the formalized models). README also lists ACC[p]: poly-size constant-depth ACC[p] circuits err on MOD_r (r coprime to p), Paturi's approximate-degree theorem, and torus-approximant results | Lean 4.33.1 + Mathlib (lab uses v4.36.0, so a port is needed) | README does not state `sorry`/axiom status; audit with `scripts/lean_audit.sh` before reuse | yes (abstract + README via WebFetch) |
| R. Thiemann, AFP entry "Clique is not solvable by monotone circuits of polynomial size" (May 2022; releases through Isabelle2026, Oct 2026) | concrete monotone lower bound (n^{1/7})^{n^{1/8}} for Clique with s = n^{1/4}, following Gordeev's (monotone-restricted) proof | Isabelle/HOL | — | yes |
| D. Nag, ECCC TR26-167 rev. 1 | Theorem 2.5 (fixed-advantage near-cubic wire bound) "formally verified in Lean 4 from nine quoted statements of the cited results" (github.com/devnag/near-cubic-wires) | Lean 4 | cited results are *assumed*, so this is not end-to-end | yes (ECCC note) |
| G. Morse, arXiv 2608.30238 (Aug 2026) | exact unrestricted XOR–AND multiplicative complexity 9 for 4-term binary polynomial multiplication; "no project-specific axiom or native decision procedure" | Lean 4 | peripheral (multiplicative complexity) | yes (abstract) |
| Anthropic, Hexagon 2610.00577v1 | 2^{o(n)} #3-SAT algorithm (ETH refutation) | Lean 4 | relevant to §4.5; may contain reusable running-time formalizations | yes (landing page) |
| none found | any B2/U2 general-circuit lower bound (gate elimination), algorithmic-method theorem, Kannan-type bound, or range-avoidance result in a proof assistant | — | gap; see open problem rank 3 | searches in §10 |

---

## 9. Known-results registry entries (for research/KNOWN_RESULTS.md)

Format: `- [area] statement — Authors (Year), venue/arXiv — checked:yes/no`

- [general-circuits] An explicit F ∈ P (any affine disperser for dim d) requires B2 circuits of size 4n − 10d = 4n − O(log n) — Mishra, Santhanam (2026), ECCC TR26-260 rev.1 [PREPRINT, AI-elicited proof] — checked:yes
- [general-circuits] 3.5n − o(n) B2 lower bound (superseded) — Mishra, Santhanam (2026), ECCC TR26-260 v1 — checked:yes
- [general-circuits] Affine dispersers for sublinear dimension require B2 circuits of size 3.1n − o(n) — Li, Yang (2022), STOC 2022 / ECCC TR21-023 — checked:yes
- [general-circuits] Affine dispersers require (3 + 1/86)n − o(n) B2 gates; quadratic dispersers require 3.11n — Find, Golovnev, Hirsch, Kulikov (2016/2023), FOCS 2016; Comput. Complex. 32(2):13 — checked:yes
- [general-circuits] Explicit (n − o(n))-mixed function requires U2 circuits of size 5n − o(n) — Iwama, Morizumi (2002), MFCS 2002 (also attributed to Iwama–Lachish–Morizumi–Raz) — checked:no
- [general-circuits] Lachish–Raz-type mixed-function arguments cannot exceed 5n (a mixed function with U2 complexity 5n + o(n)) — Amano, Tarui (2011), TCS 412(18) — checked:no
- [general-circuits] Parity has U2 complexity exactly 3(n − 1) (Schnorr 1974); constructive refuters exist for gate-elimination bounds incl. size-3(n−1) De Morgan circuits — Carmosino, Dang, Jackman (2026), arXiv 2604.23958 — checked:yes
- [general-circuits] 3n − o(n) explicit B2 lower bound (Blum 1984) unbeaten until 2016 — Blum (1984), TCS 28 — checked:no
- [general-circuits/barrier] Gate elimination with a bounded number of substitutions per step cannot prove cn beyond a constant c (< 5n for substitution-based elimination) — Golovnev, Hirsch, Knop, Kulikov (2018), JCSS 96 / MFCS 2016 — checked:yes
- [general-circuits/barrier] Every size-s circuit is an OR of 2^{s/3.9} 16-CNFs; gate elimination "inherently limited to < 5n" — Golovnev, Kulikov, Williams (2021), ITCS 2021 / arXiv 1811.04828 — checked:yes
- [general-circuits] Best explicit formula-depth lower bound is (3 − o(1))·log n; (4 − o(1))·log n with AND-only top 2 − o(1) layers — Hao Wu (2024), ECCC TR24-086 — checked:yes
- [formulas] Andreev's function requires De Morgan formulas of size Ω(n^3/(log^2 n · log log n)), best for P (tight up to log log n for that function) — Tal (2014), FOCS 2014 / ECCC TR14-048 — checked:yes
- [formulas] MCSP[(log n)^c] has no n^{2−o(1)} probabilistic formulas; n^{2+ε} would imply NP ⊄ Formula[n^k] ∀k — Chen, Jin, Williams (2020), STOC 2020 / ECCC TR20-065 — checked:yes
- [formulas] OV_{n,d} requires Boolean formulas of size Ω(n^2 d) (tight) — Choudhury, Limaye, Sreenivasaiah, Srinivasan (2026), ECCC TR26-121 — checked:yes
- [AC0] For fixed d ≥ 3, the Goldreich–Tal trilinear function needs depth-d circuits of size 2^{Ω((n log n/log log n)^{1/(d−1)})} and has depth-d circuits of size 2^{O(n^{2/d})} — Chukhin (2026), ECCC TR26-248 [PREPRINT] — checked:yes
- [AC0] For fixed d ≥ 3, inverse trace / Goldreich–Tal / OpenAI's evaluator need depth-≤d size 2^{Ω_d((n log n)^{1/(d−1)})}, plus correlation bounds beating parity's — Li, Zhong (2026), ECCC TR26-261 [PREPRINT] — checked:yes
- [AC0] An explicit P function needs OR–AND–OR circuits of size 2^{ω(√n)} (first break of the depth-3 parity barrier) — OpenAI (2026), OpenAI Math Release preprint, 23 Sep 2026 [AI] — checked:no
- [AC0] Every symmetric function (incl. Majority) has depth-d circuits of size 2^{O(n^{1/(d−1)})} — Lecomte, Ramakrishnan (2026), arXiv 2609.34029 [AI: GPT-6 Astra] — checked:yes
- [AC0] Parity needs exp(ε_d n^{1/(d−1)}) depth-d De Morgan circuits via a purely top-down proof — Korten (2026), ECCC TR26-221 — checked:yes
- [AC0] Before 2026 the best explicit depth-3 bound was 2^{(π/√6)√n − o(√n)} (PPSZ 2005); parity needs Ω(n^{1/4}2^{√n}) at depth 3 (PPZ 1999, tight) — via Chukhin (2026) — checked:no
- [AC0] An E^NP function is not (1/2 + 2^{−d})-approximable by F2 polynomials of degree d = √n/log n for all large n; d = n^{1/2+ε} would give E^NP ⊄ depth-3 size 2^{n^{1/2+ε}} — Chen, Lyu (2021), ECCC TR21-003 — checked:yes
- [AC0] k-OV conjecture holds for constant-depth circuits in polylog dimension (n^{k−ε} gates); clique of size k ≤ n^{1/(h−1)−ε} needs n^{Ω(k)} at depth h — Chukhin (2026), arXiv 2611.06231 — checked:yes
- [AC0[p]] XOR of k majorities on ℓ-bit blocks has correlation ≤ (4d/√ℓ)^k with Boolean-valued degree-d polynomials over any field; explicit 2^{−n^{Ω(1)}} correlation vs 2^{n^{Ω(1)}}-size AC0[q] — Chattopadhyay, Hatami, Lee, Lovett, Tal, Viola (2026), ECCC TR26-208 [PREPRINT] — checked:yes
- [ACC0] NEXP ⊄ poly-size ACC0; E^NP ⊄ 2^{n^{o(1)}}-size ACC0 — Williams (2011/2014), CCC 2011 / J. ACM 61(1) — checked:yes
- [ACC0] NP ⊆ SIZE[n^k] ⇒ n^{O(k^3)}-size witness circuits for NP; ∀k NQP ⊄ n^{log^k n}-size ACC0∘THR; 2^{(1−ε)n} Gap-UNSAT for 2^{εn}-size C ⇒ NP fixed-poly C lower bounds — Murray, Williams (2018/2020), STOC 2018 / SICOMP 49(5) — checked:yes
- [ACC0] NQP not (1/2 + 1/log^c n)-approximable by poly-size ACC0 — Chen (2019), ECCC TR19-031 — checked:yes
- [ACC0] NQP not (1/2 + 2^{−log^a n})-approximable by 2^{log^a n}-size ACC0∘THR; NP not (1/2 + n^{−k})-approximable by n^k-size Sum∘THR — Chen, Ren (2020), STOC 2020 — checked:yes
- [ACC0] Almost-everywhere: E^NP not (1/2 + 2^{−n^ε})-approximable by 2^{n^ε}-size ACC0; P^NP rigid matrices a.e. — Chen, Lyu, Williams (2020), FOCS 2020 — checked:yes
- [ACC0] NEXP ⊄ sub-half-exponential-size ACC0; MA_{ACC0} ⊄ fixed-poly ACC0 — Chen (2022), ECCC TR22-183 — checked:yes
- [ACC0] NP ⊄ ACC0 is open; obstacle: no 2^{(1−ε)n} Gap-ACC-UNSAT on 2^{εn}-size circuits — Murray, Williams (2020), SICOMP §6 — checked:yes
- [ACC0] Symmetric depth-h CC0 circuits for AND need 2^{Ω̃(n^{1/O(h)})} — Krishan, Sarma (2026), ECCC TR26-116 — checked:yes
- [threshold] f ∈ E^NP requires n^{2.5−ε}-size THR∘THR and SYM∘THR (previous n^{2−ε}) — Chen, Tal, Wang (2026), ECCC TR26-039 (STOC 2026 per Nag) — checked:yes
- [threshold] a.e. near-cubic wires: F_c ∈ E^NP has no SYM∘THR with ≤ b n^3/log^{10} n wires or THR∘THR with ≤ b' n^3/log^{12} n wires achieving agreement 1/2 + n^{−c} — Nag (2026), ECCC TR26-167 [PREPRINT] — checked:yes
- [threshold] Andreev's function: no (1/2+ε)-approximating depth-2 LTF circuits with o(ε^3 n^{3/2}/log^3 n) gates or o(ε^3 n^{5/2}/log^{7/2} n) wires — Kane, Williams (2016), STOC 2016 — checked:yes
- [threshold] Andreev: worst-case Ω(n^{3/2}/log^2 n) gates, Ω(n^{5/2}/log^{5/2} n) wires; exact (5/16 + o(1))n^2-gate circuit; sign-coherent circuits need Ω(n^2/log^3 n) — Reitwießner (2026), ECCC TR26-330 [PREPRINT] — checked:yes
- [threshold] n^{1+c^{−d}}-wire bounds for NC1-complete functions for all c > 1 ⇒ TC0 ≠ NC1; known bounds have c ≈ 2.41 (IPS97) — Chen, Tell (2019), STOC 2019 / ECCC TR18-199 — checked:yes
- [threshold] Win-win: read-once 2-DNFs not in 2^{εn}-size ETHR∘ETHR, or OV in n^{1+ε} for c log n dims — Williams (2024), FOCS 2024 / ECCC TR24-142 — checked:yes
- [monotone] Explicit n-variate monotone function needs exp(n^{1/2−o(1)}) monotone circuits; clique n^{Ω(k)} for k ≤ n^{1/3−o(1)} — Cavalar, Kumar, Rossman (2020/2022), ECCC TR20-181 — checked:yes
- [monotone] Clique needs n^{Ω(k)} monotone size for k ≤ n^{1/2−ε}; exp(Ω(n^{1/3−ε})) for a P function — de Rezende, Vinyals (2025), CCC 2025 — checked:yes
- [monotone] 2^{αN} for explicit NP function vs monotone formulas, switching networks, span programs, comparator circuits — Pitassi, Robere (2017), ECCC TR16-188 — checked:yes
- [monotone] Perfect matching on n-vertex graphs needs 2^{n^{Ω(1)}} monotone circuits — Cavalar, Göös, Riazanov, Sofronova, Sokolov (2025), ECCC TR25-102 — checked:yes
- [monotone] Bipartite perfect matching on n-vertex graphs needs exp(Ω(n^{1/2})) monotone gates — Rao (2026), ECCC TR26-129 [PREPRINT] — checked:yes
- [monotone] Supercritical size–depth tradeoff for monotone circuits — Göös, Maystre, Risse, Sokolov (2024), ECCC TR24-186 — checked:yes
- [fixed-poly] ∀k Σ2P ⊄ SIZE(n^k) — Kannan (1982), Inform. Control — checked:no
- [fixed-poly] ∀k ZPP^NP ⊄ SIZE(n^k) (Köbler–Watanabe 1998); S2P ⊆ ZPP^NP (Cai 2007) — via Aaronson (2006) — checked:no
- [fixed-poly] Oracles relative to which NP and P^NP have linear-size circuits (Wilson 1985); oracle where PP has linear-size circuits; PP ⊄ SIZE(n^k) needs non-relativizing proof — Aaronson (2006), CCC 2006 / arXiv cs/0504048 — checked:yes
- [fixed-poly] ∀k MA/1 ⊄ SIZE(n^k); explicit (MA ∩ coMA)/1 language — Santhanam (2007/2009), STOC 2007 / SICOMP 39(3) — checked:yes
- [fixed-poly] NP ⊆ SIZE(n^k) for some k ⇔ P^NP_∥ ⊆ SIZE(n^k) for some k ⇔ ONP/1 ⊆ SIZE(n^k) for some k — Fortnow, Santhanam (2006), ECCC TR06-157 — checked:yes
- [fixed-poly] P^NP ⊄ SIZE[n^k] ∀k ⇔ (NP ⊆ P/poly ⇒ PH ⊆ i.o.-P^NP/n) — Chen, McKay, Murray, Williams (2019), ECCC TR19-075 — checked:yes
- [fixed-poly] Explicit O2P language ∉ SIZE(n^k) and O2TIME hierarchy — Gajulapalli, Li, Volkovich (2024/25), ECCC TR24-049 / arXiv 2510.15268 — checked:yes
- [fixed-poly] OMIN = OL2P contains functions hard for fixed-poly circuits; NP ⊆ P/poly ⇒ PH = OM ⊆ OMIN ∩ P^{prOMA} ∩ ZPP^{ONP} — Hirsch, Volkovich, Williams; Hirsch, Volkovich (2026), ECCC TR26-250, TR26-328 [PREPRINT] — checked:yes
- [fixed-poly] Either NE ⊄ SIZE[2^n/(2n)] (⇒ NP ⊄ SIZE[n^k] ∀k) or VP^0_Z ≠ VNP^0_Z — Chukhin, Gajulapalli, Golovnev, Mihajlin (2026), ECCC TR26-313 / arXiv 2611.07972 [PREPRINT] — checked:yes
- [fixed-poly] NP ⊄ SIZE[n^k] is open (as of Nov 2026) — Mishra, Santhanam (2026), ECCC TR26-260 §1.1; Williams essay — checked:yes
- [exp-classes] S2E/1 (and Σ2E, ZPE^NP/1) requires circuit size 2^n/n; proof relativizes — Chen, Hirahara, Ren (2024), STOC 2024 / arXiv 2309.12912 — checked:yes
- [exp-classes] S2E ⊄ i.o.-SIZE[2^n/n]; a.e. for Σ2E ∩ Π2E and ZPE^NP; FZPP^NP pseudodeterministic rigid matrices, Ramsey graphs etc. — Z. Li (2024), STOC 2024 / arXiv 2310.17762 — checked:yes
- [exp-classes] AMEXP/2^{n^ε} requires 2^n/n — Chen, Li, Liang (2024/26), ECCC TR24-182 — checked:yes
- [exp-classes] E^{prMA}/1 requires 2^n/n — Ren, Williams (2026), ECCC TR26-118 / arXiv 2607.09963 [PREPRINT] — checked:yes
- [exp-classes] EXP^NP has a 2^{n^{Ω(1)}}-hard language iff it has a 2^n/(2n)-hard one; hard truth tables are APEPP-complete under P^NP reductions — Korten (2021), FOCS 2021 / arXiv 2106.00875 — checked:yes
- [exp-classes] E^NP ⊄ SIZE[O(n)] was open before Oct 2026 — Murray, Williams (2020), SICOMP §6; Williams (2010) fn. 5 — checked:yes
- [exp-classes][claimed, conditional on the Oct-2026 ETH refutation] E^NP ⊄ SIZE[O(n)] and ∃L ∈ E^NP with C_L(n) > c·n·√log n i.o. — OpenAI (2026) Cor. 1.4/C.1; Anthropic (2026) §7 — checked:no (secondary: 01-eth-refutation.md F14)
- [exp-classes][claimed] E^NP language needing Ω(m√log m/log log m) gates over unbounded AND/OR + binary XOR; Ω(m√log m) for a bounded basis with a linear budget of XOR/symmetric gates (i.o.) — Wu, Wang (2026), arXiv 2611.02560 — checked:yes
- [exp-classes] Oracle with E ⊄ NC/poly but E^NP ⊆ P/poly — Korten, Yang (2026), ECCC TR26-302 rev.1 [PREPRINT] — checked:yes
- [exp-classes] Oracle where SAT is in half-exponential time yet EXP ⊆ P/poly; Σ2EXP not in sub-half-exponential size (relativizes) — Vyas, Williams (2024), ECCC TR24-113 — checked:yes
- [algorithmic-method] ETH false ⇒ E^NP has no linear-size circuits — Williams (2010/2013), STOC 2010 / SICOMP 42(3), Thm 6.1 — checked:yes
- [algorithmic-method] SAT of linear-size (series-parallel / log-depth) circuits in 2^n/n^{ω(1)} ⇒ E^NP ⊄ that class; SETH false ⇒ E^NP ⊄ linear series-parallel; n^α-SAT in 2^{n−ω(n/log log n)} ⇒ E^NP ⊄ linear log-depth — Jahanjou, Miles, Viola (2015/2018), ICALP 2015 / Inf. Comput. 261 — checked:yes
- [algorithmic-method] 3SAT in deterministic c^n, c < 2^{1/10} ⇒ E^NP ⊄ SIZE[3n] (Ben-Sasson–Viola 2014); c < 2^{1/7} ⇒ a 2-output E^NP function needs 3n gates (JMV Cor. 6; MS26 states 2^{1/7} for Boolean) — JMV (2018) — checked:yes
- [algorithmic-method] CircuitSAT in O(2^{(1−δ)n} poly(m)) (co-non)deterministic ⇒ E^NP ⊄ SIZE[2^{εn}] — Williams (2010), Thm 1.2 — checked:yes
- [algorithmic-method] NSETH false ⇒ E^NP ⊄ linear-size series-parallel — Carmosino et al. (2016), ITCS 2016 / ECCC TR15-148; JMV — checked:yes
- [magnification] 2^{n^{o(1)}}-sparse NP language ∉ Circuit[n^{1+ε}] ⇒ NP ⊄ SIZE[n^k] ∀k (also formulas, BPs, AC0[6], TC0) — Chen, Jin, Williams (2019), ECCC TR19-118 — checked:yes
- [magnification] n^{α(n)}-sparse NP language without 2n + O(n/log log n)-gate probabilistic circuits ⇒ NP ⊄ SIZE[n^k] ∀k and NTIME[2^n] ⊄ SIZE[2^{n^{1/5}}]; an O(n)-sparse P language needs 2n − 2 — Chen, Li, Yang (2022), ECCC TR22-086 — checked:yes
- [magnification] MCSP[2^{√n}] average-case zero-error hardness for linear-size formulas ⇒ NP ⊄ Formula[poly] — Oliveira, Santhanam (2018), FOCS 2018 — checked:yes
- [magnification] Gap-MCSP ∉ Circuit[N^{1+ε}] ⇒ NP ⊄ Circuit[poly] — Oliveira, Pich, Santhanam (2019), CCC 2019 — checked:yes
- [magnification] search-MCSP[n^c] lacking Õ(N)-size Õ(1)-depth circuits ⇒ NP ⊄ P/poly — McKay, Murray, Williams (2019), STOC 2019 — checked:yes
- [barrier] Locality barrier for hardness magnification — Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam (2020), ITCS 2020 / ECCC TR19-168 — checked:yes
- [magnification] Distinguisher-based general magnification below known lower bounds, sharp thresholds — Atserias, Müller (2025), arXiv 2503.24061 — checked:yes
- [barrier] Under trapdoored-matrix assumptions natural proofs cannot give > n·polylog n (or superlinear) circuit lower bounds for linear maps — Raz (2026), ECCC TR26-008 [PREPRINT] — checked:yes
- [barrier] Candidate PRF (SPN with field-inversion S-box) of size n·log^{O(1)} n with exponential security vs linear/differential cryptanalysis (⇒ natural-proofs limit near n·polylog n if secure) — Miles, Viola (2011/2015), ECCC TR11-076 / J. ACM 62(6) — checked:yes
- [range-avoidance] Under subexp iO, deterministic poly-time Avoid ⇒ NP = coNP — Ilango, Li, Williams (2023), STOC 2023 — checked:yes
- [range-avoidance] FP^NP C-Avoid frameworks; E^NP lower bounds ⇔ algorithms with E^NP preprocessing; AC0-Avoid (poly stretch) or NC0_4-Avoid (n + n^{o(1)}) ⇒ NC1 lower bounds — Ren, Santhanam, Wang (2022), FOCS 2022 — checked:yes
- [range-avoidance] Unconditional FP^NP algorithm for ACC0-Avoid / RemotePoint / hard partial truth tables — Chen, Huang, Li, Ren (2023), ECCC TR23-072 — checked:yes
- [range-avoidance] NC0_2-Avoid ∈ P; NC0_k-Avoid ∈ P for m ≥ n^{k−1}/log n; FP^NP NC0_3-Avoid at m = n + n^{2/3} ⇒ rigid matrices — Gajulapalli, Golovnev, Nagargoje, Saraogi (2023), ECCC TR23-021 — checked:yes
- [range-avoidance] Monotone NC0_3-Avoid ∈ P for m > n — Kuntewar, Sarma (2025), arXiv 2503.17114 — checked:yes
- [range-avoidance] Crypto ⇒ Avoid/RPP hard for nondeterministic search even for constant-depth circuits — Chen, Li (2024), STOC 2024 — checked:yes
- [range-avoidance] Demi-bits ⇒ Avoid hard for nondeterministic algorithms — Ren, Wang, Zhong (2025), arXiv 2511.14061 — checked:yes
- [range-avoidance] Decision problems reducible to Avoid lie in AM ∩ coAM (Avoid NP-hard ⇒ PH collapses) — Ghentiyala, Li, Stephens-Davidowitz (2025/26), ECCC TR25-210 rev.1 — checked:yes
- [range-avoidance] For constant-depth C ⊇ AC0: FP^NP C-Avoid[n, n^{1+ε}] ⇔ E^NP ⊄ C[2^{o(n)}] — Huang, Li, Zhong (2025), ECCC TR25-049 — checked:yes
- [range-avoidance] Avoid ≤ Linear Ordering Principle; L2E needs 2^n/n — Korten, Pitassi (2024), FOCS 2024 — checked:yes
- [rigidity] Best explicit rigidity: Ω((n^2/r) log(n/r)) — Friedman (1993); Shokrollahi, Spielman, Stemann (1997) — checked:no
- [rigidity] FNP i.o. matrices δN^2-far from rank 2^{log N/Ω(log log N)} — Bhangale, Harsha, Paradise, Tal (2020), FOCS 2020 — checked:yes
- [rigidity] P^NP for all large n: R(2^{log^{1−ε} n}) ≥ (1/2 − exp(−log^{(2/3)ε} n))n^2 — Chen, Lyu (2021), ECCC TR21-003 — checked:yes
- [rigidity] Walsh–Hadamard is not rigid enough for Valiant's approach — Alman, Williams (2017), arXiv 1611.05558 — checked:yes
- [eth-claim] Deterministic 2^{o(n)} #3-SAT algorithm (refuting ETH), Lean-formalized, primarily AI-generated [CLAIMED, under review] — Anthropic (2026), Hexagon 2610.00577v1 — checked:yes (abstract)
- [eth-claim] Deterministic k-CNF counting in 2^{O_k(n log log n/√log n)} (2^{O(n/√log n)} at bounded density) [CLAIMED] — OpenAI (2026), GitHub openai/math preprint, Thm 1.1 — checked:no (via arXiv 2611.00517, 2611.02650; the parallel survey 01-eth-refutation.md reports checked:yes)
- [formalization] Håstad's PARITY ∉ AC0 bound exp(Ω_d(n^{1/(d−1)})) formalized in Lean 4 — Wesonga (2026), arXiv 2609.24188 — checked:yes
- [formalization] Isabelle/HOL proof that Clique needs monotone circuits of size (n^{1/7})^{n^{1/8}} (s = n^{1/4}) — Thiemann (2022), AFP — checked:yes

---

## 10. Bibliography (proposed entries for research/BIB.md)

Format: key | authors | title | venue | year | url | checked.

- MS26 | O. S. Mishra, R. Santhanam | An Explicit 4n − O(log(n)) Size Lower Bound against General Boolean Circuits (v1: 3.5n − o(n)) | ECCC TR26-260 (rev. 1) | 2026 | https://eccc.weizmann.ac.il/report/2026/260/ | yes
- LY22 | J. Li, T. Yang | 3.1n − o(n) Circuit Lower Bounds for Explicit Functions | STOC 2022, 1180–1193; ECCC TR21-023 | 2022 | https://eccc.weizmann.ac.il/report/2021/023/ | yes
- FGHK16 | M. G. Find, A. Golovnev, E. A. Hirsch, A. S. Kulikov | A Better-than-3n Lower Bound for the Circuit Complexity of an Explicit Function | FOCS 2016, 89–98; journal: Improving 3n Circuit Complexity Lower Bounds, Comput. Complex. 32(2):13 (2023) | 2016/2023 | https://eccc.weizmann.ac.il/report/2015/166/ | yes
- IM02 | K. Iwama, H. Morizumi | An Explicit Lower Bound of 5n − o(n) for Boolean Circuits | MFCS 2002, LNCS 2420:353–364 | 2002 | — | no
- LR01 | O. Lachish, R. Raz | Explicit Lower Bound of 4.5n − o(n) for Boolean Circuits | STOC 2001, 399–408 | 2001 | — | no
- AT11 | K. Amano, J. Tarui | A Well-Mixed Function with Circuit Complexity 5n: Tightness of the Lachish–Raz-Type Bounds | TCS 412(18):1646–1651 | 2011 | — | no
- Blu84 | N. Blum | A Boolean Function Requiring 3n Network Size | TCS 28:337–345 | 1984 | — | no
- GHKK18 | A. Golovnev, E. A. Hirsch, A. Knop, A. S. Kulikov | On the Limits of Gate Elimination | MFCS 2016; JCSS 96:107–119 (2018) | 2018 | https://eccc.weizmann.ac.il/report/2016/119/ | yes
- GKW21 | A. Golovnev, A. S. Kulikov, R. R. Williams | Circuit Depth Reductions | ITCS 2021, LIPIcs 185:24 | 2021 | https://arxiv.org/abs/1811.04828 | yes
- CDJ26a | M. Carmosino, N. Dang, T. Jackman | Convergent Gate Elimination and Constructive Circuit Lower Bounds | arXiv 2602.17942 | 2026 | https://arxiv.org/abs/2602.17942 | yes
- CDJ26b | M. Carmosino, N. Dang, T. Jackman | Constructive Separations from Gate Elimination | arXiv 2604.23958 | 2026 | https://arxiv.org/abs/2604.23958 | yes
- Wu24 | Hao Wu | A nearly-4 log n depth lower bound for formulas with restriction on top | ECCC TR24-086 | 2024 | https://eccc.weizmann.ac.il/report/2024/086/ | yes
- Tal14 | A. Tal | Shrinkage of De Morgan Formulae by Spectral Techniques | FOCS 2014; ECCC TR14-048 | 2014 | https://eccc.weizmann.ac.il/report/2014/048/ | yes
- Has98 | J. Håstad | The Shrinkage Exponent of de Morgan Formulas is 2 | SIAM J. Comput. | 1998 | — | no
- FMT21 | Y. Filmus, O. Meir, A. Tal | Shrinkage under Random Projections, and Cubic Formula Lower Bounds for AC0 | ITCS 2021; ECCC TR20-180 | 2021 | https://arxiv.org/abs/2012.02210 | no
- CJW20 | L. Chen, C. Jin, R. Williams | Sharp Threshold Results for Computational Complexity | STOC 2020; ECCC TR20-065 | 2020 | https://eccc.weizmann.ac.il/report/2020/065/ | yes
- Chu26a | N. Chukhin | Breaking the Parity Barrier for Constant-Depth Circuits | ECCC TR26-248 | 2026 | https://eccc.weizmann.ac.il/report/2026/248/ | yes
- LZ26 | X. Li, Y. Zhong | Short Point Lists for CNFs and Stronger Constant-Depth Circuit Hardness | ECCC TR26-261 | 2026 | https://eccc.weizmann.ac.il/report/2026/261/ | yes
- Ope26b | OpenAI | Beyond the Square-Root Exponent for Depth-Three Boolean Circuits | OpenAI Math Release preprint (OAI:...September-23-2026) | 2026 | (github.com/openai/math, not opened) | no
- LR26 | V. Lecomte, P. Ramakrishnan | Optimal Shallow Circuits for Majority | arXiv 2609.34029 | 2026 | https://arxiv.org/abs/2609.34029 | yes
- Kor26a | O. Korten | Top-Down Lower Bounds for All Depths | ECCC TR26-221 | 2026 | https://eccc.weizmann.ac.il/report/2026/221/ | yes
- Lin26 | H. Lin | Fine-Grained AC0 Lower Bounds for k-OV, k-XOR, and k-SUM via Colored Subgraph Isomorphism | ECCC TR26-139 | 2026 | https://eccc.weizmann.ac.il/report/2026/139/ | yes
- Chu26b | N. Chukhin | Exhaustive Search Is Hard to Beat in Constant Depth for Hyperclique and Orthogonal Vectors | arXiv 2611.06231 | 2026 | https://arxiv.org/abs/2611.06231 | yes
- CL21 | L. Chen, X. Lyu | Inverse-Exponential Correlation Bounds and Extremely Rigid Matrices from a New Derandomized XOR Lemma | ECCC TR21-003 | 2021 | https://eccc.weizmann.ac.il/report/2021/003/ | yes
- CHLLTV26 | E. Chattopadhyay, P. Hatami, C. H. Lee, S. Lovett, A. Tal, E. Viola | Exponential Correlation Bounds for Polynomials | ECCC TR26-208 | 2026 | https://eccc.weizmann.ac.il/report/2026/208/ | yes
- Wil14 | R. Williams | Nonuniform ACC Circuit Lower Bounds | CCC 2011; J. ACM 61(1):2 | 2014 | https://people.csail.mit.edu/rrw/acc-lbs-journal-final.pdf | yes
- Wil10 | R. Williams | Improving Exhaustive Search Implies Superpolynomial Lower Bounds | STOC 2010; SIAM J. Comput. 42(3):1218–1244 (2013) | 2010/2013 | https://people.csail.mit.edu/rrw/improved-algs-lbs2.pdf | yes
- MW20 | C. Murray, R. Williams | Circuit Lower Bounds for Nondeterministic Quasi-Polytime: An Easy Witness Lemma for NP and NQP | STOC 2018; SIAM J. Comput. 49(5) (2020) | 2018/2020 | https://people.csail.mit.edu/rrw/easy-witness-nqp.pdf ; ECCC TR17-188 | yes
- Che19 | L. Chen | Non-deterministic Quasi-Polynomial Time is Average-case Hard for ACC Circuits | ECCC TR19-031 (FOCS 2019, unverified) | 2019 | https://eccc.weizmann.ac.il/report/2019/031/ | yes
- CR20 | L. Chen, H. Ren | Strong Average-Case Circuit Lower Bounds from Non-trivial Derandomization | STOC 2020; ECCC TR20-010 | 2020 | https://eccc.weizmann.ac.il/report/2020/010/ | yes
- CLW20 | L. Chen, X. Lyu, R. Williams | Almost-Everywhere Circuit Lower Bounds from Non-Trivial Derandomization | FOCS 2020; ECCC TR20-150 | 2020 | https://eccc.weizmann.ac.il/report/2020/150/ | yes
- Che22 | L. Chen | New Lower Bounds and Derandomization for ACC, and a Derandomization-centric View on the Algorithmic Method | ECCC TR22-183 | 2022 | https://eccc.weizmann.ac.il/report/2022/183/ | yes
- KV24 | V. Krishan, S. Vishwanathan | Degree Lower Bounds for Torus Polynomials and MAJORITY vs ACC0 (orig. "Towards ACC Lower Bounds using Torus Polynomials") | ECCC TR24-074 | 2024/25 | https://eccc.weizmann.ac.il/report/2024/074/ | yes
- KS26 | V. Krishan, J. Sarma | On CC0 Lower Bounds for AND via Torus Polynomials | ECCC TR26-116 | 2026 | https://eccc.weizmann.ac.il/report/2026/116/ | yes
- RSS25 | A. Riazanov, A. Sofronova, D. Sokolov | Lower Bounds Beyond DNF of Parities | ECCC TR25-024 | 2025 | https://eccc.weizmann.ac.il/report/2025/024/ | yes
- CTW26 | L. Chen, A. Tal, Y. Wang | Super-quadratic Lower Bounds for Depth-2 Linear Threshold Circuits | ECCC TR26-039 (STOC 2026, unverified) | 2026 | https://eccc.weizmann.ac.il/report/2026/039/ | yes
- Nag26 | D. Nag | Almost-Everywhere Near-Cubic Wire Lower Bounds for SYM∘THR and THR∘THR | ECCC TR26-167 | 2026 | https://eccc.weizmann.ac.il/report/2026/167/ | yes
- KW16 | D. Kane, R. Williams | Super-Linear Gate and Super-Quadratic Wire Lower Bounds for Depth-Two and Depth-Three Threshold Circuits | STOC 2016; ECCC TR15-188 | 2016 | https://eccc.weizmann.ac.il/report/2015/188/ | yes
- Rei26 | C. Reitwießner | Improved Bounds for Depth-Two Threshold Circuits Computing Andreev's Function | ECCC TR26-330 | 2026 | https://eccc.weizmann.ac.il/report/2026/330/ | yes
- CT19 | L. Chen, R. Tell | Bootstrapping Results for Threshold Circuits "Just Beyond" Known Lower Bounds | STOC 2019; ECCC TR18-199 | 2019 | https://eccc.weizmann.ac.il/report/2018/199/ | yes
- Wil24 | R. Williams | The Orthogonal Vectors Conjecture and Non-Uniform Circuit Lower Bounds | FOCS 2024; ECCC TR24-142 | 2024 | https://eccc.weizmann.ac.il/report/2024/142/ | yes
- HMRSS26 | L. Hambardzumyan, K. Myasnikov, A. Riazanov, M. Shirley, A. Shraibman | Spiky Rank and Its Applications to Rigidity and Circuits | ECCC TR26-030; arXiv 2602.23503 | 2026 | https://arxiv.org/abs/2602.23503 | yes
- CKR22 | B. P. Cavalar, M. Kumar, B. Rossman | Monotone Circuit Lower Bounds from Robust Sunflowers | ECCC TR20-181 (journal 2022) | 2020/2022 | https://eccc.weizmann.ac.il/report/2020/181/ | yes
- LMMPZ22 | S. Lovett, R. Meka, I. Mertz, T. Pitassi, J. Zhang | Lifting with Sunflowers | ITCS 2022; ECCC TR20-111 | 2022 | https://eccc.weizmann.ac.il/report/2020/111/ | no (abstract opened; the 2^{Ω̃(√n)} statement only via search snippet)
- dRV25 | S. F. de Rezende, M. Vinyals | Lifting with Colourful Sunflowers | CCC 2025, LIPIcs 339:36 | 2025 | https://doi.org/10.4230/LIPIcs.CCC.2025.36 | yes
- PR17 | T. Pitassi, R. Robere | Strongly Exponential Lower Bounds for Monotone Computation | ECCC TR16-188 (STOC 2017, unverified) | 2017 | https://eccc.weizmann.ac.il/report/2016/188/ | yes
- CGRSS25 | B. P. Cavalar, M. Göös, A. Riazanov, A. Sofronova, D. Sokolov | Monotone Circuit Complexity of Matching | ECCC TR25-102 | 2025 | https://eccc.weizmann.ac.il/report/2025/102/ | yes
- Rao26 | A. Rao | Monotone Circuit Lower Bounds from Spread Matchings | ECCC TR26-129 | 2026 | https://eccc.weizmann.ac.il/report/2026/129/ | yes
- GMRS24 | M. Göös, G. Maystre, K. Risse, D. Sokolov | Supercritical Tradeoffs for Monotone Circuits | ECCC TR24-186 | 2024 | https://eccc.weizmann.ac.il/report/2024/186/ | yes
- CLSS26 | T. Choudhury, N. Limaye, K. Sreenivasaiah, S. Srinivasan | New and Improved Concrete Lower Bounds for Orthogonal Vectors | ECCC TR26-121 | 2026 | https://eccc.weizmann.ac.il/report/2026/121/ | yes
- BN26 | A. Beimel, O. Nir | The Power of Multislices in Monotone Computation | ECCC TR26-213 | 2026 | https://eccc.weizmann.ac.il/report/2026/213/ | yes
- Kan82 | R. Kannan | Circuit-Size Lower Bounds and Non-Reducibility to Sparse Sets | Information and Control 55 | 1982 | — | no
- Cai07 | J.-Y. Cai | S2P ⊆ ZPP^NP | JCSS 73(1):25–35 | 2007 | — | no
- Aar06 | S. Aaronson | Oracles Are Subtle But Not Malicious | CCC 2006; arXiv cs/0504048 | 2006 | https://arxiv.org/abs/cs/0504048 | yes
- San09 | R. Santhanam | Circuit Lower Bounds for Merlin–Arthur Classes | STOC 2007; SIAM J. Comput. 39(3):1038–1061 | 2009 | https://eccc.weizmann.ac.il/report/2007/005/ | yes
- FS06 | L. Fortnow, R. Santhanam (CCC 2009 version adds R. Williams) | Fixed-Polynomial Size Circuit Bounds | ECCC TR06-157; CCC 2009 | 2006/2009 | https://eccc.weizmann.ac.il/report/2006/157/ | yes (ECCC)
- CR06 | V. T. Chakaravarthy, S. Roy | Oblivious Symmetric Alternation | STACS 2006, LNCS 3884:230–241 | 2006 | — | no
- CMMW19 | L. Chen, D. McKay, C. Murray, R. Williams | Relations and Equivalences Between Circuit Lower Bounds and Karp–Lipton Theorems | ECCC TR19-075 (CCC 2019, unverified) | 2019 | https://eccc.weizmann.ac.il/report/2019/075/ | yes
- GLV24 | K. Gajulapalli, Z. Li, I. Volkovich | Oblivious (Complexity) Classes Revisited: Lower Bounds and Hierarchies | ECCC TR24-049; arXiv 2510.15268 | 2024/25 | https://arxiv.org/abs/2510.15268 | yes
- HVW26 | E. Hirsch, I. Volkovich, R. Williams | Input-oblivious Complexity Classes in the Second Level of the Polynomial Hierarchy | ECCC TR26-250 | 2026 | https://eccc.weizmann.ac.il/report/2026/250/ | yes
- HV26 | E. Hirsch, I. Volkovich | The Ultimate Karp–Lipton Collapse | ECCC TR26-328 | 2026 | https://eccc.weizmann.ac.il/report/2026/328/ | yes
- HV25 | E. Hirsch, I. Volkovich | Upper and Lower Bounds for the Linear Ordering Principle | ECCC TR25-142 | 2025 | https://eccc.weizmann.ac.il/report/2025/142/ | yes
- CGGM26 | N. Chukhin, K. Gajulapalli, A. Golovnev, I. Mihajlin | A Little Derandomization Goes a Long Way: Unconditional Circuit Lower Bounds using Low-Degree PIT | ECCC TR26-313; arXiv 2611.07972 | 2026 | https://arxiv.org/abs/2611.07972 | yes
- CHR24 | L. Chen, S. Hirahara, H. Ren | Symmetric Exponential Time Requires Near-Maximum Circuit Size | STOC 2024; arXiv 2309.12912 | 2024 | https://arxiv.org/abs/2309.12912 | yes
- Li24 | Z. Li | Symmetric Exponential Time Requires Near-Maximum Circuit Size: Simplified, Truly Uniform | STOC 2024; arXiv 2310.17762 | 2024 | https://arxiv.org/abs/2310.17762 | yes
- CLL24 | L. Chen, J. Li, J. Liang | Maximum Circuit Lower Bounds for Exponential-time Arthur Merlin | ECCC TR24-182 | 2024/26 | https://eccc.weizmann.ac.il/report/2024/182/ | yes
- RW26 | H. Ren, R. Williams | Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries | ECCC TR26-118; arXiv 2607.09963 | 2026 | https://arxiv.org/abs/2607.09963 | yes
- Hit26 | J. M. Hitchcock | Exponential-Size Circuit Complexity is Comeager in Symmetric Exponential Time | ECCC TR26-068; arXiv 2605.03306 | 2026 | https://arxiv.org/abs/2605.03306 | yes
- VW24 | N. Vyas, R. Williams | On Oracles and Algorithmic Methods for Proving Lower Bounds | ECCC TR24-113 | 2024 | https://eccc.weizmann.ac.il/report/2024/113/ | yes
- KKMP21 | R. Kleinberg, O. Korten, D. Mitropolsky, C. Papadimitriou | Total Functions in the Polynomial Hierarchy | ITCS 2021; ECCC TR20-153 | 2021 | https://eccc.weizmann.ac.il/report/2020/153/ | yes
- Kor21 | O. Korten | The Hardest Explicit Construction | FOCS 2021; arXiv 2106.00875 | 2021 | https://arxiv.org/abs/2106.00875 | yes
- RSW22 | H. Ren, R. Santhanam, Z. Wang | On the Range Avoidance Problem for Circuits | FOCS 2022; ECCC TR22-048 | 2022 | https://eccc.weizmann.ac.il/report/2022/048/ | yes
- CHLR23 | Y. Chen, Y. Huang, J. Li, H. Ren | Range Avoidance, Remote Point, and Hard Partial Truth Tables via Satisfying-Pairs Algorithms | ECCC TR23-072 | 2023 | https://eccc.weizmann.ac.il/report/2023/072/ | yes
- GGNS23 | K. Gajulapalli, A. Golovnev, S. Nagargoje, S. Saraogi | Range Avoidance for Constant-Depth Circuits: Hardness and Algorithms | ECCC TR23-021; arXiv 2303.05044 | 2023 | https://arxiv.org/abs/2303.05044 | yes
- GLW22 | V. Guruswami, X. Lyu, X. Wang | Range Avoidance for Low-depth Circuits and Connections to Pseudorandomness | RANDOM 2022; ECCC TR22-102 | 2022 | https://eccc.weizmann.ac.il/report/2022/102/ | no
- KuSa25 | N. Kuntewar, J. Sarma | Range Avoidance in Boolean Circuits via Turán-type Bounds | arXiv 2503.17114; ECCC TR25-034 | 2025 | https://arxiv.org/abs/2503.17114 | yes
- ILW23 | R. Ilango, J. Li, R. Williams | Indistinguishability Obfuscation, Range Avoidance, and Bounded Arithmetic | STOC 2023; ECCC TR23-038 | 2023 | https://eccc.weizmann.ac.il/report/2023/038/ | yes
- CLi24 | Yilei Chen, J. Li | Hardness of Range Avoidance and Remote Point for Restricted Circuits via Cryptography | STOC 2024; ECCC TR23-206 | 2024 | https://eccc.weizmann.ac.il/report/2023/206/ | yes
- HLZ25 | S. Huang, X. Li, Y. Zhong | Range Avoidance and Remote Point: New Algorithms and Hardness | ECCC TR25-049 | 2025 | https://eccc.weizmann.ac.il/report/2025/049/ | yes
- RWZ25 | H. Ren, Y. Wang, Y. Zhong | Hardness of Range Avoidance and Proof Complexity Generators from Demi-Bits | arXiv 2511.14061; ECCC TR25-191 | 2025 | https://arxiv.org/abs/2511.14061 | yes
- Ila25 | R. Ilango | The Oracle Derandomization Hypothesis is False (And More) Assuming No Natural Proofs | ECCC TR25-190 | 2025 | https://eccc.weizmann.ac.il/report/2025/190/ | yes
- GLSD25 | S. Ghentiyala, Z. Li, N. Stephens-Davidowitz | Range Avoidance, Arthur-Merlin, and TFNP | ECCC TR25-210 | 2025/26 | https://eccc.weizmann.ac.il/report/2025/210/ | yes
- HVo25 | E. Hirsch, I. Volkovich | A Note on Avoid vs MCSP | arXiv 2512.21764; ECCC TR25-220 | 2025 | https://arxiv.org/abs/2512.21764 | yes
- LRZ26 | X. Li, H. Ren, Y. Zhong | Many Proof Complexity Generators Inside One Demi-Bits Generator | arXiv 2609.23228; ECCC TR26-196 | 2026 | https://arxiv.org/abs/2609.23228 | yes
- KY26 | O. Korten, T. Yang | Tight Depth Lower Bounds for Stretch Amplification | ECCC TR26-302 (rev. 1) | 2026 | https://eccc.weizmann.ac.il/report/2026/302/ | yes
- KP24 | O. Korten, T. Pitassi | Strong vs. Weak Range Avoidance and the Linear Ordering Principle | FOCS 2024; ECCC TR24-076 | 2024 | https://eccc.weizmann.ac.il/report/2024/076/ | yes
- KoSa25 | O. Korten, R. Santhanam | How to Construct Random Strings | ECCC TR25-104 | 2025 | https://eccc.weizmann.ac.il/report/2025/104/ | yes
- LT26 | Z. Li, R. Tell | Trading Time, Space, and Alternations: General Plasticity for Algorithms from Hardness of Range Avoidance | ECCC TR26-233 | 2026 | https://eccc.weizmann.ac.il/report/2026/233/ | yes
- Li26 | Z. Li | Derandomizing (Fragments of) Arthur–Merlin with Range Avoidance | ECCC TR26-270 | 2026 | https://eccc.weizmann.ac.il/report/2026/270/ | yes
- Vol26 | B. L. Volk | Improved Algorithms for the Remote Point Problem | arXiv 2609.25765; ECCC TR26-203 | 2026 | https://arxiv.org/abs/2609.25765 | yes
- Ram20 | C. Ramya | Recent Progress on Matrix Rigidity – A Survey | arXiv 2009.09460 | 2020 | https://arxiv.org/abs/2009.09460 | yes
- AW17 | J. Alman, R. Williams | Probabilistic Rank and Matrix Rigidity | arXiv 1611.05558 | 2016/17 | https://arxiv.org/abs/1611.05558 | yes
- AC19 | J. Alman, L. Chen | Efficient Construction of Rigid Matrices Using an NP Oracle | FOCS 2019 | 2019 | — | no
- BHPT20 | A. Bhangale, P. Harsha, O. Paradise, A. Tal | Rigid Matrices From Rectangular PCPs | FOCS 2020; ECCC TR20-075 | 2020 | https://eccc.weizmann.ac.il/report/2020/075/ | yes
- DL19 | Z. Dvir, A. Liu | Fourier and Circulant Matrices are Not Rigid | ECCC TR19-129 | 2019 | https://eccc.weizmann.ac.il/report/2019/129/ | no
- Raz26 | R. Raz | A Note on Natural-Proofs for Super-Linear Lower Bounds for Linear Functions | ECCC TR26-008 | 2026 | https://eccc.weizmann.ac.il/report/2026/008/ | yes
- CKMS25 | N. Chukhin, A. Kulikov, I. Mihajlin, A. Smirnova | Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank Under NSETH and Beyond | ECCC TR25-038; arXiv 2411.02936 | 2025 | https://eccc.weizmann.ac.il/report/2025/038/ | yes
- MV15 | E. Miles, E. Viola | Substitution-Permutation Networks, Pseudorandom Functions, and Natural Proofs | J. ACM 62(6):46 (2015); ECCC TR11-076 | 2011/2015 | https://eccc.weizmann.ac.il/report/2011/076/ | yes
- OS18 | I. C. Oliveira, R. Santhanam | Hardness Magnification for Natural Problems | FOCS 2018; ECCC TR18-139 | 2018 | https://eccc.weizmann.ac.il/report/2018/139/ | yes
- OPS19 | I. C. Oliveira, J. Pich, R. Santhanam | Hardness Magnification near State-of-the-Art Lower Bounds | CCC 2019; ECCC TR18-158 | 2019 | https://eccc.weizmann.ac.il/report/2018/158/ | yes
- MMW19 | D. McKay, C. Murray, R. Williams | Weak Lower Bounds on Resource-Bounded Compression Imply Strong Separations of Complexity Classes | STOC 2019 | 2019 | https://people.csail.mit.edu/rrw/MCSP-MKTP-stoc19.pdf | yes
- CJW19 | L. Chen, C. Jin, R. Williams | Hardness Magnification for all Sparse NP Languages | ECCC TR19-118 (FOCS 2019, unverified) | 2019 | https://eccc.weizmann.ac.il/report/2019/118/ | yes
- CLY22 | L. Chen, J. Li, T. Yang | Extremely Efficient Constructions of Hash Functions, with Applications to Hardness Magnification and PRFs | ECCC TR22-086 | 2022 | https://eccc.weizmann.ac.il/report/2022/086/ | yes
- CHOPRS20 | L. Chen, S. Hirahara, I. C. Oliveira, J. Pich, N. Rajgopal, R. Santhanam | Beyond Natural Proofs: Hardness Magnification and Locality | ITCS 2020; J. ACM 2022; ECCC TR19-168; arXiv 1911.08297 | 2020 | https://eccc.weizmann.ac.il/report/2019/168/ | yes
- AM25 | A. Atserias, M. Müller | Simple General Magnification of Circuit Lower Bounds | arXiv 2503.24061 | 2025 | https://arxiv.org/abs/2503.24061 | yes
- JMV18 | H. Jahanjou, E. Miles, E. Viola | Local Reductions | ICALP 2015; Inf. Comput. 261:281–295 (2018); ECCC TR13-099 | 2015/2018 | https://eccc.weizmann.ac.il/report/2013/099/ | yes
- BV14 | E. Ben-Sasson, E. Viola | Short PCPs with Projection Queries | ICALP 2014, LNCS 8572:163–173 | 2014 | — | no (via JMV)
- CGIMPS16 | M. Carmosino, J. Gao, R. Impagliazzo, I. Mihajlin, R. Paturi, S. Schneider | Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility | ITCS 2016; ECCC TR15-148 | 2016 | https://eccc.weizmann.ac.il/report/2015/148/ | yes
- CRTY23 | L. Chen, R. Rothblum, R. Tell, E. Yogev | On Exponential-Time Hypotheses, Derandomization, and Circuit Lower Bounds | ECCC TR19-169 (J. ACM 2023) | 2019/2023 | https://eccc.weizmann.ac.il/report/2019/169/ | yes (abstract)
- Ant26 | Anthropic | A 2^{o(n)} Time Algorithm for 3-SAT | Hexagon 2610.00577v1 | 2026 | https://hexagonmath.org/2610.00577v1 | yes (abstract page)
- Ope26a | OpenAI | The Exponential Time Hypothesis is False | GitHub preprint (17 Oct, rev. 25 Oct 2026) | 2026 | https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026 | no
- MITHG26 | MIT Hardness Group (J. Brunner, E. D. Demaine, F. Frei, T. Gomez, M. Hecher, J. Li, J. Lynch) | ETH is Dead, Long Live SH | arXiv 2611.02650 | 2026 | https://arxiv.org/abs/2611.02650 | yes
- DL26 | F. Dias, Y. Lima | Limits and Constants of OpenAI's Claimed ETH Refutation | arXiv 2611.00517 | 2026 | https://arxiv.org/abs/2611.00517 | yes
- WW26 | M. Wu, M. Wang | Circuit Lower Bounds for Extended Gate Bases from Subexponential Counting | arXiv 2611.02560 | 2026 | https://arxiv.org/abs/2611.02560 | yes
- Xie26 | Y. Xie | What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics | arXiv 2610.17090 | 2026 | https://arxiv.org/abs/2610.17090 | yes (abstract, TOC)
- Wes26 | S. Wesonga | Formalizing PARITY Circuit Lower Bounds in Lean | arXiv 2609.24188 | 2026 | https://arxiv.org/abs/2609.24188 ; https://github.com/formalcs/circuit-complexity | yes
- Thi22 | R. Thiemann | Clique is not solvable by monotone circuits of polynomial size | Archive of Formal Proofs | 2022 | https://www.isa-afp.org/entries/Clique_and_Monotone_Circuits.html | yes
- Mor26 | G. Morse | Unrestricted Boolean Multiplicative Complexity of Four-Term Binary Polynomial Multiplication … | arXiv 2608.30238 | 2026 | https://arxiv.org/abs/2608.30238 | yes
- WilEss | R. R. Williams | Some Estimated Likelihoods for Computational Complexity | LNCS volume (essay) | — | https://people.csail.mit.edu/rrw/likelihoods.pdf | yes

---

## 11. Search log

All queries were run on 2026-11-23, one agent, sequentially.

**APIs and listings used**
- arXiv API via HTTPS (helper script): `all:"symmetric exponential time"`, `all:"range avoidance"`,
  `abs:"circuit lower bound" AND abs:"explicit function"`, `abs:"hardness magnification"`,
  `abs:"fixed-polynomial" AND abs:circuit`, `abs:"matrix rigidity" OR abs:"rigid matrices"`,
  `abs:"exponential time hypothesis" AND abs:false`, `ti:"hardest explicit construction"`,
  `ti:"rigid matrices using an NP oracle"` (no hit), `ti:"lifting with sunflowers"` (no hit),
  `abs:"formula" AND abs:"lower bound" AND abs:"De Morgan"`, `abs:"KRW"`, `abs:"superlinear" AND abs:"circuit lower bound"`,
  Lean/Isabelle/Coq formalization queries (`abs:formalization AND abs:"switching lemma"` found Wesonga), and
  ETH-consequence queries (`abs:"linear-size circuits" AND abs:ETH` etc., no hits). id_list lookups for
  2611.07972, 2607.09963, 2609.23228, 2512.21764, 2511.14061, 2503.17114, 2609.34029, 2604.23958, 2602.17942,
  2510.15268, 2503.24061, 2609.25765, 2602.23503, 2611.02650, 2611.01774, 2611.00517, 2611.06231, 2611.09764,
  2009.09460, 1611.05558, 1811.04828, 2106.00875, cs/0504048, 2609.24188, 2610.17090, 2608.30238, 2008.06805.
- ECCC: year listings https://eccc.weizmann.ac.il/year/{2002,2005–2026}/ parsed for titles, plus the RSS feed
  https://eccc.weizmann.ac.il/feeds/reports. Report pages /report/YYYY/NNN/ for: 2026/{008, 039, 118, 129, 167, 208,
  213, 220, 221, 241, 246, 248, 250, 260, 261, 270, 302, 313, 319, 328, 330, 233, 116, 121, 139}; 2025/{024, 033, 038,
  049, 102, 104, 142, 190, 210, 211}; 2024/{074, 076, 086, 113, 142, 182, 186}; 2023/{021, 038, 072, 206};
  2022/{048, 086, 183}; 2021/{003, 023}; 2020/{010, 065, 075, 111, 150, 153, 181}; 2019/{031, 075, 118, 168, 169};
  2018/{139, 158, 199}; 2017/188; 2016/{119, 188}; 2015/{148, 166, 188}; 2014/048; 2013/099; 2011/076; 2007/005;
  2006/157.
- PDFs opened in full or in part: ECCC TR26-260 rev.1 (Mishra–Santhanam), TR26-248 (Chukhin), TR26-039 (CTW),
  TR26-208 rev.1 (CHLLTV), TR13-099 rev.3 (JMV); arXiv 2611.02650 (MIT Hardness Group), cs/0504048 (Aaronson),
  2009.09460 (Ramya), 2610.17090 (Xie); Williams' site PDFs likelihoods.pdf, improved-algs-lbs2.pdf (Thm 6.1),
  acc-lbs-journal-final.pdf, easy-witness-nqp.pdf, MCSP-MKTP-stoc19.pdf.
- Other pages: https://hexagonmath.org/2610.00577v1 (Anthropic ETH abstract);
  https://www.isa-afp.org/entries/Clique_and_Monotone_Circuits.html;
  https://drops.dagstuhl.de/…/LIPIcs.CCC.2025.36 (de Rezende–Vinyals);
  https://github.com/formalcs/circuit-complexity (README via WebFetch).
- WebSearch: OpenAI ETH paper; consequences of the ETH refutation for E^NP (no 2026 write-up found);
  Shtetl-Optimized / Computational Complexity blog on ETH and E^NP (none found); "Lifting with sunflowers" abstract;
  the Isabelle AFP clique entry; a SAT-specific circuit lower bound (none found).

**Sources I could not open**
- DBLP API: bot-protection page (Anubis). Semantic Scholar API: HTTP 429 after one result.
- OpenAI GitHub preprints (ETH; depth-3): GitHub API access is not enabled for this session. These rows are
  `checked: no`, based on secondary arXiv/ECCC citations.
- IEEE Xplore page for FSW09 (CCC 2009): empty content. I used the ECCC Fortnow–Santhanam version instead.
- Not opened (primary): Kannan 1982; Håstad 1986/1998; Razborov 1985/1987; Smolensky 1987; Andreev 1987; Alon–
  Boppana 1987; Harnik–Raz 2000; Wilson 1985; Friedman 1993; Shokrollahi–Spielman–Stemann 1997; Blum 1984; Lachish–
  Raz 2001; Iwama–Morizumi 2002; Amano–Tarui 2011; Paul 1977; Stockmeyer 1977; Schnorr 1974; Alman–Chen 2019;
  Dvir–Liu 2019; IPS 1997; Tamaki 2016; Alman–Chan–Williams 2016; Hajnal et al. 1993; Forster 2002; Aaronson–
  Wigderson 2009; Allender–Koucký 2010; Lipton–Williams 2012; GLW 2022; Golovnev's thesis; Kulikov's CSR 2018
  open-problems paper; Pich 2022 (arXiv 2212.09285, title only).
- Williams' 23 Nov 2026 X/Bluesky thread: not accessible to me. I relied on the lead's notes in
  `research/survey/00-director-sources.md` (secondary).
- The "For claude" screenshots in the repo root are dated June/July 2026, not 23 Nov. I did not use them.
- Cross-check (read-only): `research/survey/01-eth-refutation.md`, written by the parallel ETH scout. It showed that
  the E^NP ⊄ SIZE[c·n·√log n] corollary is already in OpenAI's paper (Cor. 1.4/C.1) and in Anthropic §7, which my
  own searches had missed. It also pointed me to Wu–Wang (arXiv 2611.02560), which I then opened via the arXiv API.
  §4.5 was corrected accordingly.
