# Known-results registry (novelty gate)

**Check here before working on any idea.** If an idea matches an entry (or is a special case of one), it is not
new — build on it or move on. Entries are merged by the lead from lit-scout surveys and novelty-checker reports.
Format: `- [area] precise statement — Authors (Year), venue/arXiv — checked: yes/no — source file`

(populated in Stage 1)

## !! Lean formalization prior art (verified by the lead, 2026-11-23, by cloning the repo)
- [formalization] **cslib-frontier** (https://github.com/cslib-community/cslib-frontier, Lean 4 v4.36.0-rc2 on CSLib + Mathlib,
  AI-assisted, ~12.6k .lean files, commit 1435284b, 23 Nov 2026) already defines `P`, `NP`
  (`CslibFrontier/Computability/Complexity/Classes/{P,NP}.lean`) and proves `SAT_npComplete` (Cook–Levin,
  `.../CookLevin/Completeness.lean`), `ThreeSAT_npComplete`, `baker_gill_solovay` (`.../Classes/Oracle/Collapse.lean`),
  `not_ETH` (`.../FineGrained/CountingNativeEndpoint.lean`), plus (per cross-checks, not yet audited by us) Håstad, Smolensky,
  Razborov P ⊄ AC0[2], Khrapchenko, Andreev n^{2.5−o(1)}, Kannan, B2 affine-disperser 4n − 9d gate elimination.
  Public roadmap targets: Williams NEXP ⊄ ACC0 (#889), Kabanets–Impagliazzo (#891), VNP-completeness of the permanent (#321),
  metacomplexity/magnification (#798), E^NP ⊄ SIZE(O(n)) from the ETH refutation (#1539). — checked: yes (cloned, grepped)
  ⇒ Mission item 4 ("first serious Lean formalization of P, NP, Cook–Levin, barriers") is NOT novel. Do not duplicate; build on it.

## ETH refutation (Oct 2026) and consequences
Source: `research/survey/01-eth-refutation.md`. Corrections/disputes: `research/reviews/survey-01-eth-refutation.crosscheck.md` (read it before relying on an entry).
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

## Boolean circuit lower bounds & explicit constructions
Source: `research/survey/02-circuit-lower-bounds.md`. Corrections/disputes: `research/reviews/survey-02-circuit-lower-bounds.crosscheck.md` (read it before relying on an entry).
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
