# Bibliography

Every source the lab cites. Never invent an entry. `checked: yes` means someone opened the source and confirmed
the cited statement. Merged by the lead from agents' proposed entries.

## Barriers (named in CLAUDE.md; to be checked in Stage 1)
- [BGS75] T. Baker, J. Gill, R. Solovay. "Relativizations of the P =? NP Question." SIAM J. Comput. 4(4), 1975. — checked: no
- [RR97] A. Razborov, S. Rudich. "Natural Proofs." J. Comput. Syst. Sci. 55(1), 1997. — checked: no
- [AW09] S. Aaronson, A. Wigderson. "Algebrization: A New Barrier in Complexity Theory." ACM TOCT 1(1), 2009. — checked: no
- [CHOPRS20] L. Chen, S. Hirahara, I. Oliveira, J. Pich, N. Rajgopal, R. Santhanam. "Beyond Natural Proofs: Hardness Magnification and Locality." ITCS 2020 / J. ACM 2022. — checked: no
- [BIP19] P. Bürgisser, C. Ikenmeyer, G. Panova. "No occurrence obstructions in geometric complexity theory." J. AMS 32(1), 2019. — checked: no

## Textbooks
- [AB09] S. Arora, B. Barak. Computational Complexity: A Modern Approach. Cambridge University Press, 2009. — checked: no
- [Sip12] M. Sipser. Introduction to the Theory of Computation, 3rd ed. Cengage, 2012. — checked: no

## Software
- [Mathlib] The mathlib Community. Mathlib4, tag v4.36.0, commit fc4f59e577feb1a4956671bc04ac18aaaf8cd842. https://github.com/leanprover-community/mathlib4 — checked: yes (installed)

## From `research/survey/01-eth-refutation.md` (merged 2026-11-23; verify against the cross-check before citing)
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

## From `research/survey/02-circuit-lower-bounds.md` (merged 2026-11-23; verify against the cross-check before citing)
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

## Formalization
- [cslib-frontier] cslib-community. cslib-frontier: frontier formalization library for CSLib (Lean 4). https://github.com/cslib-community/cslib-frontier, commit 1435284b4705d38060dcf36e73212e644193f3f4 (2026-11-23). — checked: yes (cloned)
