# Cross-check of survey 01 "eth-refutation"

- Reviewed file: `research/survey/01-eth-refutation.md` (lit-scout, 2026-11-23)
- Reviewer: independent cross-checker (red-team role), 2026-11-23. I did not write the survey and did not edit it.
- Method: I opened the primary sources (PDFs rendered page by page, the OpenAI LaTeX source, Lean statement files,
  arXiv abstract pages, blog posts and their comment RSS feeds, GitHub PRs and files), then searched arXiv, ECCC,
  the ethdiscussion.blog feeds, the complexity blogs and the web for Oct–Nov 2026 work.
- Verdict: **DAMAGED-REPAIRABLE** (structured verdict: needs-corrections). The frontier table is accurate. The
  open-problem table and the formalization section are out of date or mis-framed in three places that matter for
  what the lab works on next.

---

## 0. Plain-language summary

1. **The citations are good.** Every row of the frontier table (F1–F15) and every follow-up paper I opened says
   what the survey says. Authors, dates, bounds, constants and verbatim quotes match. I found no invented citation.
   All the problems are small (wrong source post, wrong version label, a dropped qualifier). The one exception is
   that #ETH is called a "stronger" assumption than ETH, which is backwards.
2. **One open problem is already half-solved (O3).** On 16–17 Nov 2026 Szeider posted v2 of his note.
   - It claims 2^{o(n)}-size IPS refutations for every unsatisfiable 3-CNF, over every field whose characteristic
     is not 2.
   - It says this bound is proved in Lean 4, building on Anthropic's Lean development.
   - It gives the Extended Frege case only under a condition: Extended Frege would have to simulate IPS.
   - The survey says no source covers Extended Frege, and it does not mention the Lean proof.
   - The lab should not spend weeks on the IPS half. The Extended Frege half is much harder than T = 3 suggests.
3. **The Lean formalization landscape is underreported (O1, §7).** The repository `cslib-community/cslib-frontier`
   (formerly "complexitylib") already contains:
   - its own from-scratch Lean proof `not_ETH : ¬ETH` on a standard multitape Turing machine, plus ¬#ETH and
     ¬Gap-ETH;
   - Cook–Levin (`CookLevin.SAT_npComplete`), NP-completeness of 3SAT, and Baker–Gill–Solovay;
   - partial work toward the E^NP circuit lower bound.

   This bears on the lab's mission item 4 ("first serious Lean formalization of P, NP, Cook–Levin"). The survey's
   "unverified" cslib PRs #2509/#2510 are in that repository, not in leanprover/cslib, and both were merged on
   6 Nov 2026.
4. **The top "realistic" recommendation (O2) has a ceiling the survey does not state.** A short rank argument
   (mine, §2.3) shows Anthropic's "pieces" can never go below ρ = 1/2. So the best this route can give is #k-SAT in
   2^{O(km/log m)} and an E^NP lower bound of about c·n·log n, compared with c·n·√log n today. The survey also
   points the lab to a novelty check against Hrubeš / Naslund. By Anthropic's own conversion, that route cannot get
   below ρ = 3/4, so it cannot beat the existing ρ = 1/√2.
5. **No new flaw, verdict or improved exponent found.**
   - Nobody has reported an error in either proof as of 23 Nov 2026.
   - The organisers (Impagliazzo, Paturi, Williams) have posted no verdict.
   - Wikipedia says the claim "has not gone through academic review."
   - I found no improvement of 2^{n/(log n)^{1/2+o(1)}}.
   - I found no resolution of O4–O11.
   - The Orthogonal Vectors hypothesis still stands (Chukhin, 4 Nov: "remains open even for k=2").

---

## 1. Row-by-row check

Legend: VALID = matches the source I opened; INCOMPLETE = right but missing a hypothesis or qualifier;
MISQUOTE / WRONG = error; NOT CHECKED = I could not open it.

### 1.1 Frontier table §2.1

| id | result | what I opened |
|---|---|---|
| F1 | VALID | OAI26 p. 2, Thm 1.1: n ≥ 20; (n+m)^{O_k(1)}2^{O_k(n log log n/√log n)} bit ops; (n+m)^{O_k(1)} space; m ≤ Dn gives 2^{O_{k,D}(n/√log n)}. p. 1 footnote: "17 October 2026, revised 25 October 2026". "log" is natural (p. 1). |
| F2 | VALID | p. 2 remark (ρ(n) = n(log log n)²/√log n). p. 7 names "Proposition 6.4". |
| F3 | VALID | LaTeX `thm:overview-sparse-polynomials`: m_test ≤ cn, ≤ (log n)^c monomials of degree ≤ k, 2^{O_{k,c}(n(log log n)²/√log n)} bit ops, n^{O_{k,c}(1)} space. |
| F4 | INCOMPLETE (minor) | p. 53, Thm D.1. The row omits two hypotheses: the number of vertices is bounded by a fixed polynomial in s, and every entry is computable in time (s+L)^b·2^{A s^{9/10}} and space (s+L)^b. |
| F5 | VALID | `SubexponentialSAT.lean`: ∃ machine, C, A, S, d, e > 0 per k ≥ 2; runtime C·(L+1)^d·2^{A·n(log log(n+16))²/√log(n+16)}; visited-space bound at every prefix; unary `encodeNat`. 378.md confirms that the Lean bound is the (log log n)² version. The challenge file carries `sorry`, as Comparator challenge files do. |
| F6 | VALID | Ant26 p. 1–2: Theorem 1 with an absolute constant; footnote 1 gives 2^{O(kn/√log n)} for sparse inputs. Title "A 2^{o(n)} Time Algorithm for 3-SAT", author line "CLAUDE / ANTHROPIC", date 26 Oct 2026. |
| F7 | VALID | Ant26 Thm 2 (proof ends p. 20). |
| F8 | VALID | Ant26 Thm A(d), p. 28. |
| F9 | VALID except one label | `MainResults.lean` listing (pp. 41–43) and README confirm the theorem names `MainResults.mainTheorem` / `MainResults.ethIsFalse`, axioms [propext, Classical.choice, Quot.sound], and "about 8 minutes on 24 virtual CPUs … about 7 GB of memory". **"Mathlib v4.33.1" is not what the manifest says:** `lake-manifest.json` pins Mathlib by commit `0df444a3…` (inputRev is the commit; no tag). |
| F10 | VALID | OAI26 p. 4 ("Theorem 1.1 refutes ETH, SETH, Gap-ETH, and NSETH"; randomized versions; regular resolution; MA-SETH [Wil16]). Ant26 p. 20 Cor 5 and p. 21 (NSETH, Cor 6 #ETH). |
| F11 | VALID | OAI26 Cor 1.3 (p. 2); Ant26 Cor 7 (p. 21). |
| F12 | VALID | OAI26 Cor 1.2 (p. 2). |
| F13 | VALID | OAI26 Cor C.2 (p. 52); "This does not rule out one-wayness against polynomial-time algorithms." (p. 53). |
| F14 | VALID | Cor 1.4 (p. 3), Cor C.1 and the proof of 1.4 (pp. 51–52), using constant-density 3-SAT in V^b·2^{AV/√log₂V} with η < 1/(12A). OpenAI cites the local reductions as [JMV13] (ECCC TR13-099; ICALP 2015). |
| F15 | VALID | Williams manuscript (May 4, 2010): Thm 6.1 on p. 20 and footnote 5 on p. 2, both verbatim. |

Verbatim anchors: I re-read all of them except the HackerNoon / TechCrunch / WIRED quotes, and they match. This
includes the OpenAI abstract and reductions sentence, the App. C.1 sentence, 378.md, Ant26 p. 1–2 (P vs NP, OV,
thresholds, provenance, ">800 papers"), the OpenAI announcement (16th/17th October) and Paturi's prompt post.

### 1.2 Expositions §2.2 and follow-ups §2.3

- **Expositions.**
  - E1 (O'Donnell): VALID. Thm 6.1, Thm B.1, App. A, NTIME(T) ⊆ DTIME(2^{O(T(log log T)³/√log T)}), the LLM
    footnote, and the date 30 Oct 2026.
  - E2 (Kintali, 26 Oct): VALID.
  - E4 (Porat, draft 12 Nov): VALID.
  - E5 (Rozhoň, 13 Nov): quotes VALID.
  - E6 (Zhuang README): VALID.
  - E7 (Nederlof 5 Nov; Nelson = Shtetl comment #75): VALID.
- **Follow-ups.** I checked each abstract for C1–C16. Authors, dates and every number listed match.
  - Majdoddin: 2^{33858}→2^{420}; 2^{2.2·10^{12}}→2^{8.6·10^9}; 2^{6000}; (log₂K)^{−3}; N^{23/6}.
  - Dias–Lima: 10^{32}, 10^{126}, 10^{3517}; log₂(n+m) > 10^9; 2^{Ω(√tw)}, 2^{Ω(√n)} above density 3,
    2^{Ω(n^{1/3})}.
  - The VW–Zamir "distilled … with a publicly available AI model's assistance" sentence is VALID (p. 3).
  - Alman et al. Remark 1 and the "no Sparsification Lemma … Max-kSAT" / "evidently says nothing" sentences are
    VALID.
- **§2.4 limits.**
  - L1 is VALID (Ant26 p. 3 and p. 45: "e below about 2/9, which is 4/9 of the e = 1/2").
  - L5, L6, L7 and L8 are VALID against Ant26 pp. 2, 14, 29, 40 and OpenAI p. 4.

### 1.3 Secondary items the survey marked checked: no that I could check

- **Aaronson (Shtetl ?p=10239).** Comment #18 ties a subexponential CircuitSAT algorithm to a P=NP estimate of
  20–30%. Comment #31 says the same 20–30% if **Weak ETH** also fell. The survey cites only #18; #31 is relevant to
  O8.
- **Williams' likelihoods.pdf (forwarded by the director).** Table 1 gives ETH 70%, SETH 25%, NSETH 15%,
  P ≠ NP 80%. VALID.
- **Fortnow.** "applies to k-SAT but not to NP problems in general" and the 2^{n^{o(1)}} sentence are in For26
  (28 Oct). The reply "if A => B and A is false, that doesn't make B false" is dated 31 Oct. Both VALID.
  - **"It will never beat CDCL" is from a different post**: "Another Step Towards Optiland" (4 Nov 2026), which
    is not in the bibliography.

---

## 2. Issues found

### 2.1 SERIOUS: O3 is half superseded, and the survey misstates the state of the Extended Frege half

- **Source.** S. Szeider, "Consequences of the ETH refutations for proof complexity and knowledge compilation", v2.
  Published 16 Nov 2026; Zenodo record created 17 Nov (DOI 10.5281/zenodo.24243987 → record 24299623). It was
  announced in an ethdiscussion.blog comment on 17 Nov. Per the Zenodo description:
  - the weighted model count of every 3-CNF on n variables has a smooth, decomposable arithmetic circuit of size
    2^{o(n)};
  - every unsatisfiable 3-CNF has a 2^{o(n)} **IPS** refutation over every field of characteristic ≠ 2;
  - both are "proved in Lean, building on Anthropic's published Lean development". In v2 the earlier assumptions
    were removed ("Propositions 1 and 2 now have no hypotheses from the preprint");
  - **Extended Frege: conditional.** If EF polynomially simulates IPS over F_p for some odd prime p, then EF has
    refutations of the same size;
  - no such bound holds for resolution, Res(k), polynomial calculus or sum-of-squares.
- **What the survey says instead.**
  - O3 says "EF: no source found stating it; novelty check required."
  - The IPS claim appears only as an unverified blog-comment item, without the characteristic-≠-2 restriction and
    without the Lean proof.
- **Consequences.**
  - The IPS half of O3 is claimed solved, with a machine-checked proof by the claimant.
  - The EF half now reduces to whether EF simulates IPS. That is a long-standing open question, tied to short EF
    proofs of polynomial-identity-testing axioms, so T = 3 is too high (§5).
  - Characteristic 2 is left open by Szeider and is a small, concrete leftover.

### 2.2 SERIOUS: missing Lean prior art; O1 and §7 are out of date

- **Repository.** `github.com/cslib-community/cslib-frontier` (renamed from complexitylib on 2026-11-08). I fetched
  these files on `main`; I did not build them.
- **ETH refutations.**
  - `FineGrained/CountingNativeEndpoint.lean` has `public theorem not_ETH : ¬ETH`, docstring "The native counting
    construction refutes the Exponential Time Hypothesis". It runs on `Turing.MultiTapeTM` with `encCNF` and cites
    OpenAI §§3–6 and App. A–B.
  - `FineGrained/RatesNativeEndpoint.lean` has `not_SharpETH`, `not_GapETH`, `not_rGapETH`, and
    `decidableInSingleSubexpTime_KSAT`.
  - Toledo's page calls this "D1 … a native re-proof on a standard machine" of OpenAI's Prop. 6.4 route. It reports
    nanoda accepting all 49,025 declarations beneath `not_eth` and marks it CERTIFIED.
  - **This is a third, independent formal proof (AI-written), not a re-run.** The survey mentions only "A word-RAM
    version is in 'complexitylib'".
- **Cook–Levin and barriers.** The Arora–Barak audit `results/arora-barak-2007.md` lists:
  - `CookLevin.SAT_npComplete : NPComplete encCNF SAT` and `ThreeSAT_npComplete` as covered (native
    polynomial-time model, "upstream: candidate");
  - `P_subset_NP`, `NP_subset_EXP` and `baker_gill_solovay` as covered;
  - the time hierarchies as partial.
- **E^NP lower bound.** `FineGrained/CircuitLowerBoundBudget.lean` proves the counting budget for circuits of size
  about n·√log n / (12A). Its docstring says "The class separation itself is not proved in this module", with the
  rest tracked in their issue #1539. This refines the survey's lead-scout remark that the Williams/JMV part is not
  formalized: it is partly formalized, and work is ongoing.
- **cslib PRs.**
  - #2509 ("feat(WordRAM): simulate space-bounded multi-tape machines at logarithmic word size"): merged 6 Nov 2026
    via the merge queue; approved by edemaine and by a reviewer agent.
  - #2510 ("feat(TM2): one TM2 step and the clocked run in degrees that do not depend on the program"): merged
    6 Nov 2026; the PR notes the proofs are AI-written and not independently human-reviewed.
  - The survey's 404 came from looking in `leanprover/cslib`. Toledo's own page still says "merge pending", which
    is stale.
- **Consequences.**
  - O1's "Machine-check the word-RAM ↔ TM simulations" and "Reuse the definitions in the lab's P/NP/Cook–Levin
    formalization" are largely overtaken. A native standard-machine proof exists, and the lab has no P/NP
    formalization of its own yet.
  - Under CLAUDE.md ("do not re-derive known things"), the formalization track should first decide whether to build
    on or contribute to cslib-frontier. This is a mission-level fact that §7 should state.

### 2.3 SERIOUS: O2 has a hard ceiling, and its "stated open in" pointer is a dead end

- **Ceiling (lead-red-team argument, status: informal-argument).**
  - The crossing [x=v][y=u] on λ-bit strings is a 2^{2λ}×2^{2λ} permutation matrix both row-wise ((x,y) vs (u,v))
    and column-wise ((x,u) vs (y,v)), so it has full rank 2^{2λ} in both arrangements.
  - With |I| ≤ (2λ)^c pieces summing to d times the crossing, some piece has c_i^row ≥ 2λ − c·log(2λ).
  - Since c_i^col ≥ 0, Def. 7(b) (c_i^row + c_i^col ≤ 4ρλ + c·log 2λ) forces ρ ≥ 1/2 − O(log λ/λ).
  - Def. 7 itself already restricts to 1/2 ≤ ρ < 1.
- **Payoff at best.** α′ = log₂(1/ρ) ≤ 1. By Thm A(c) the route gives at best #k-SAT in 2^{O(km/log m)}, and through
  the Cor 1.4 argument at best E^NP ⊄ SIZE(c·n·log n) infinitely often.
  - The survey's "[Maj26]'s class bound (log K)^{−3} leaves room" is true but misleading: everything beyond α′ = 1
    is out of reach for pieces.
- **Wrong lead.** O2's "stated open in" column cites Naslund's Problem 12 (whether P(N) ≥ N^{1+ε}) and Hrubeš's
  P(N) = O(N^{1.62}). That is the wrong direction (a lower-bound question) and the wrong object:
  - Ant26 App. G (p. 46) converts P(N) ≤ N^c into ρ = (2+c)/4. Hrubeš's c = 1.62 gives ρ ≈ 0.905.
  - Since P(N) ≥ N, this route can never get below ρ = 3/4. It cannot beat the existing ρ = 1/√2 ≈ 0.707.
  - The "novelty check against Hrubeš" before investing is therefore wasted effort.
- **The actual lead is in Ant26 App. H (p. 49).** A graded space with log dim V_E ≈ E^α would give ρ = 2^{α−1}.
  Partitions give α = 1/2 and hence ρ = 1/√2. Any improvement needs α < 1/2 together with the
  operator-locality structure (Heisenberg/Fock).

### 2.4 MINOR (14)

1. **§1, "stronger assumptions built on it (SETH, NSETH, Gap-ETH, #ETH)".** #ETH is *weaker* than ETH (ETH ⇒ #ETH).
   It falls only because both algorithms count. SETH, NSETH and Gap-ETH are correctly called stronger.
2. **Fortnow's "It will never beat CDCL"** is from "Another Step Towards Optiland", 4 Nov 2026 (trap 6), not For26.
   Add it to the bibliography.
3. **F9 / §7 "Mathlib v4.33.1"** should read: Mathlib pinned at commit 0df444a3…; Lean v4.33.1.
4. **F4** omits Thm D.1's vertex-count and entry-computability hypotheses (§1.1).
5. **O8 paraphrase of O'Donnell.** It omits the second half: "I personally disbelieve it, but there is a much higher
   chance of it being true now." Aaronson #31 (Weak ETH falling → 20–30% for P=NP) is also relevant to O8.
6. **§1 example of re-using the algebraic trick.** "subexponential simulation of nondeterministic Turing machines"
   is cited as an example. Strassle–Subercaseaux use the 3-SAT algorithms through encodings ("from the published
   3-SAT algorithms" plus "a stronger consequence of their proof"), not the low-rank decomposition. Better examples:
   VW–Zamir, Jabal Ameli–Mohrin–Nederlof, and Alman et al. (Remark 1).
7. **§1 plain-language E^NP bound** drops "for infinitely many n" and the constant c.
8. **§2.5 ledger.** Alman–VW also claim refutations of the Directed Unweighted APSP hypothesis and the real-valued
   3SUM/APSP hypotheses. Their paper states that "Claude also verified this paper's main results using the Lean 4
   proof assistant with the Mathlib library". Neither is recorded.
9. **§2.5, Gap-ETH "claimed refuted (both papers)".** Only OpenAI states Gap-ETH explicitly; for Anthropic it is
   implied but not claimed.
10. **O7's "(or formulas)".** Non-trivial #SAT for de Morgan formulas of size up to n^{3−ε}, with 2^{n−n^{Ω(1)}}
    time, has been known since 2010–2015 (Santhanam; Chen–Kabanets–Kolokolova–Shaltiel–Zuckerman; Tal). It does
    not beat the known n^{3−o(1)} formula lower bounds. As stated, the parenthetical misrepresents the frontier;
    drop it or explain. (Recalled from memory; these classical papers were not opened in this review.)
11. **§2.3, Szeider bullet** "every unsatisfiable 3-CNF has an IPS refutation …" lacks "over fields of
    characteristic ≠ 2" (see 2.1).
12. **§8 prior-baseline row.** Cui–Liu–Yu, arXiv:2611.16814 (12 Nov 2026), give deterministic 3-SAT in 1.32736^n,
    beating Liu18's 1.32793^n. The survey lists it as "title only, out of scope". Because the 2^{o(n)} algorithms
    are galactic, this is the practical deterministic record and belongs in the baseline row.
13. **§2.4 limits table.** It misses Szeider's knowledge-compilation limit:
    - monotone circuits (no negative constants) for weighted model counts yield DNNFs;
    - some 3-CNFs with O(n) clauses need 2^{Ω(n)}-size DNNFs, so any 2^{o(n)} counting circuit must use
      cancellation;
    - Tseitin formulas on degree-3 expanders separate the two.

    This is a formal version of trap 9.
14. **Bibliography `Wil19`** lacks the venue details: LNCS 10000, pp. 9–26, Springer 2019 (as cited in Ant26).

Not an error, but useful: VW–Zamir also give **Max-2-CSP / Max-Cut in 2^{(ω/3−c)n+o(n)}** (p. 3), the first
improvement on Williams 2005. The survey lists Jabal Ameli–Mohrin–Nederlof's polynomial-space Max-Cut O(1.994^n)
but not this.

---

## 3. Search for 2023–2026 work that improves a listed bound or solves a listed open problem

**Sources searched (Oct–23 Nov 2026):**
- arXiv API: "exponential time hypothesis", abs:ETH, subexponential∧SAT, Hurwitz/eight-square, and the latest
  cs.CC (≥ 17 Nov) and cs.DS (≥ 12 Nov) listings. Several later queries were rate-limited (HTTP 429), so I covered
  those topics with web search instead.
- ECCC 2026 listing up to TR26-336.
- All five ethdiscussion.blog posts and three comment feeds.
- The Computational Complexity blog (all posts 25 Oct–19 Nov) and Shtetl-Optimized (posts 21 Oct–20 Nov).
- Toledo's page, the cslib-frontier PRs and files.
- Wikipedia, plus web searches for errors and verdicts, OV, Weak ETH/SH, k-Clique n^{o(k)}, Max-kSAT
  sparsification, and EF/IPS.

| item | status found |
|---|---|
| F1/F6 exponents | Not improved. Nothing beats n/(log n)^{1/2+o(1)}. Straub's audit (11 Nov) suggests, conditionally, "exponents up to c < 3/5" and claims no algorithm. |
| Proof status | No error reported. The organisers' kickoff post has no update ("should not be taken as certification"); the last comment on it is 12 Nov. Wikipedia: "As of November 2026, the claim has not gone through academic review." |
| O1 | **Largely superseded**: see 2.2. Remaining work: the textbook-ETH reading of cslib's definition, and a v4.36.0 (not -rc2) pin. |
| O2 | No progress found beyond Majdoddin. Ceiling ρ ≥ 1/2 (see 2.3). |
| O3 | **IPS half claimed solved with a Lean proof** (Szeider v2, 16–17 Nov). The EF half is reduced to "EF p-simulates IPS over F_p" (2.1). Characteristic 2 is open. |
| O4 | Not resolved. I could not locate Cruz's repository; the blog's RSS feed exposes only the latest 10 of 30 comments. See §4 for context. |
| O5 | Open. O'Donnell (13 Nov): "only … when the matrix is sparse". |
| O6 | Open. Alman–VW (5 Oct) exclude CNF-SAT and OV from their speedups. Chukhin (4 Nov): the k-OV conjecture "remains open even for k=2". |
| O7 | Nothing found. |
| O8 | Nothing found. MITHG26 v2 (16 Nov) calls SH "plausible". |
| O9 | Nothing found. Alman et al. and Majdoddin both say no Max-kSAT sparsification lemma is known. |
| O10 | Nothing found. |
| O11 | Nothing found. Szeider (9 Nov) notes that VW–Zamir give k^{(ω/3−c)k} for k×k Clique and that his hypothesis stands. |

---

## 4. Important results missing from the survey (with citations)

1. **cslib-frontier formalizations.**
   - Native `not_ETH`, `not_SharpETH`, `not_GapETH` on a multitape TM.
   - Cook–Levin (`CookLevin.SAT_npComplete`), `ThreeSAT_npComplete`, `baker_gill_solovay`.
   - The E^NP budget lemma (#1539).
   - PRs cslib-community/cslib-frontier #2509 and #2510, merged 6 Nov 2026.

   I did not build or audit any of these; the repository describes them as AI-built and AI-reviewed, so treat them as
   claims.
2. **Szeider v2** (Zenodo 10.5281/zenodo.24243987): Lean-proved 2^{o(n)} weighted-model-count circuits and IPS
   refutations (characteristic ≠ 2), the conditional EF statement, and the DNNF/monotone limit.
3. **VW–Zamir, arXiv:2611.09764, p. 3**: Max-2-CSP and Max-Cut in 2^{(ω/3−c)n+o(n)}, with c independent of ω.
4. **Alman–VW, arXiv:2610.06783, pp. 1–4**: Directed Unweighted APSP hypothesis and real-valued 3SUM/APSP refuted;
   Claude found the algorithm and Lean-verified the main results.
5. **Cui–Liu–Yu, arXiv:2611.16814**: deterministic 3-SAT in 1.32736^n (practical baseline).
6. **Context for O4: Williams, "Simulating Time With Square-Root Space", arXiv:2502.17779 (STOC 2025).**
   - It gives TIME[t] ⊆ SPACE[√(t log t)], hence DSPACE(n) ⊄ DTIME(n^{2−ε}).
   - Sanity facts for red-teaming Cruz (my derivation): NTIME(n) = DSPACE(n) would imply NP = PSPACE by padding,
     and also DTIME(n^{2−ε}) ⊆ NTIME(n).
   - I found no cheap derivation of NTIME(n) ⊊ DSPACE(n) from ¬ETH. All combinations of the ¬ETH simulation with
     known simulations that I tried were consistent.
7. **Ant26 App. H's remark** that ρ = 2^{α−1} when log dim V_E grows like E^α. This is the real lead for O2.
8. **An earlier unrefereed claim**: G. Camerani, "The #ETH is False, #k-SAT is in Sub-Exponential Time",
   arXiv:2102.02624 (3 Feb 2021; randomized; single version; not accepted). Record it for history and novelty
   checks, so it is not mistaken for prior art.
9. **Neighbouring AI-result expositions on ECCC** (for other scouts): TR26-281 (Shpilka, ω ≤ 9/4), TR26-298
   (B. Li), TR26-287 (border determinantal complexity of the permanent, extending OpenAI's cubic lower bound) and
   TR26-258 (PARITY ∉ QAC⁰). The last two touch the lab's lower-bound mission.

---

## 5. Calibration of the tractability × impact scores

| # | survey T×I | my view |
|---|---|---|
| O1 | 4×3 | Port-and-bridge work is mostly done elsewhere (2.2). As written, I = 2. Replace it with "evaluate and adopt cslib-frontier for mission item 4" (T4, I4). Keep "formalize E^NP ⊄ SIZE(c·n·√log n)" as a separate task (T3, I3) after checking issue #1539. |
| O2 | 3×3 | Keep T = 3. State the ceiling: at best n·log n instead of n·√log n. I = 2–3. Remove the Hrubeš/Naslund novelty gate; replace it with App. H. |
| O3 | 3×3 | The IPS part is claimed done; a check would be T = 5, I = 1 (verify Szeider's Lean). Characteristic 2 is T2–3, I2. The EF part is T = 1: it is the EF-versus-IPS / PIT-in-EF question. |
| O4 | 4×2 | Fine. |
| O5–O11 | — | Reasonable. For O7, drop "(or formulas)" (2.4 item 10). |
| Recommendation list | — | "O2 is the best realistic-publishable candidate" should be qualified by the ceiling. "O1 is a safe formalization-track task" should become "first audit cslib-frontier". |

---

## 6. What I did NOT check

- **The mathematics of the proofs.** I did not red-team the algorithms themselves. I did not build any Lean
  development (OpenAI, Anthropic, cslib-frontier, Szeider, Zhuang). I did not inspect transitive imports for
  `sorry` or check OpenAI's Comparator config (nanoda disabled?).
- **Unreachable comments.** Older ethdiscussion comments (Cruz, Chukhin, Gheorghiu–Gupte, Sukruth, Hirsch on
  Fortnow's blog): the RSS feed shows only the latest 10 of 30.
- **Secondary and private sources.** Google Drive, Zenodo notes other than Szeider v2's description, Straub's
  artifact, formalize.now, Gupte's spreadsheet, HackerNoon / TechCrunch / WIRED quotes, Gödel's Lost Letter, and
  O'Donnell's YouTube lectures.
- **Partly checked papers.** Sellke's slides (existence only, via the "Links To Other Work" post). Pass and DLSW
  abstracts. The date of OpenAI's ω ≤ 9/4 preprint (2 Oct). I confirmed the Unique Games preprint date
  (23 Sep 2026) only through OpenAI's bibliography.
- **Classical references** (IP01, IPZ01, CIP06, BI13, AKK22, LY22, CHR24, Li24, Wil16, JMV15, Hrubeš, Naslund),
  except as cited inside the primary papers.
- **Barrier audit.** I did not resolve the question in §3.4 about an oracle relative to which E^NP ⊆ SIZE(O(n)),
  nor naturalness. A pointer to consult (not opened here): Williams, "Natural Proofs Versus Derandomization",
  STOC 2013, which relates NEXP lower bounds to constructive natural properties.

---

## 7. Sources opened (all accessed 2026-11-23)

- **OpenAI paper and Lean.**
  - Paper PDF:
    https://raw.githubusercontent.com/openai/math/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
    (pp. 1–8, 51–54).
  - LaTeX source: `…/build/main_full_version.tex`.
  - https://raw.githubusercontent.com/openai/math/main/lean/docs/378.md
  - `…/lean/ComparatorChallenges/SubexponentialSAT.lean`
  - `…/history.md`
- **Anthropic paper and Lean.** Commit 16a5ce4: `eth/paper.pdf` (pp. 1–3, 12–17, 20–31, 38–49), `eth/README.md`,
  `eth/lake-manifest.json`.
- **arXiv abstracts.** 2611.11832, 2610.41622, 2611.00517, 2610.41048, 2611.00994, 2611.02548, 2611.02560,
  2611.02650 (v2 PDF pp. 1–3), 2611.09764 (PDF pp. 1–3), 2611.05082 (HTML), 2611.03880, 2611.06813, 2611.24750,
  2611.06231 (HTML), 2611.26080, 2610.06783 (PDF pp. 1–4), 2610.42012, 2611.24611, 2611.14892, 2611.16814,
  1611.05991 (v3), 2102.02624, 2611.01774.
- **Expositions.**
  - O'Donnell: https://www.cs.cmu.edu/~odonnell/some_eth_false_exposition.pdf (pp. 1–3, 11–20)
  - Kintali: https://shivakintali.github.io/papers/ETH.pdf (p. 1)
  - Porat: https://eitanporat.github.io/papers/ksat.pdf (pp. 1–2)
  - Rozhoň interview: https://vasekrozhon.substack.com/p/ryan-odonnell-on-the-exponential
  - Zhuang: https://github.com/suquark/NotETHSimplified
- **Williams.**
  - https://people.csail.mit.edu/rrw/improved-algs-lbs2.pdf (pp. 1–3, 20–24)
  - https://people.csail.mit.edu/rrw/likelihoods.pdf (pp. 1–4)
- **ethdiscussion.blog.** Home page; kickoff post; "Links To Other Work"; Nov 12 post; comment feeds of the kickoff
  post, "Lean Replications" and "New Results Related to ETH" (`/2026/11/01/announce-your-results/feed/`).
- **Blogs.**
  - Fortnow, 28 Oct: https://blog.computationalcomplexity.org/2026/10/the-exponential-time-refutation.html
  - Fortnow, 4 Nov: https://blog.computationalcomplexity.org/2026/11/another-step-towards-optiland.html
  - Gasarch, 1 Nov: https://blog.computationalcomplexity.org/2026/11/3sum-and-apsp-and-eth-oh-my.html
  - Aaronson: https://scottaaronson.blog/?p=10239
- **OpenAI announcement.** https://openai.com/index/building-scientific-understanding-with-academic-communities/
- **Formalization.**
  - Toledo: https://carlostoledo.co/eth/
  - cslib-frontier PRs: https://github.com/cslib-community/cslib-frontier/pull/2509 and `/pull/2510`
  - cslib-frontier files: `CslibFrontier/Computability/Complexity/FineGrained/{CountingNativeEndpoint,RatesNativeEndpoint,CircuitLowerBoundBudget}.lean`,
    `CslibFrontier/Computability/Complexity/CookLevin/Completeness.lean`, `results/arora-barak-2007.md`.
- **Szeider v2.** https://zenodo.org/doi/10.5281/zenodo.24243987
- **ECCC.** https://eccc.weizmann.ac.il/year/2026/ and TR26-331.
- **Wikipedia.** https://en.wikipedia.org/wiki/Exponential_time_hypothesis
