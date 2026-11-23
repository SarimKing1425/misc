# Sources forwarded by the director (2026-11-23) + lead's first notes

Status of everything here: secondary/unverified unless marked. To be verified at primary sources in Stage 1.

## 1. R. Ryan Williams, "Some Estimated Likelihoods for Computational Complexity" (essay, LNCS volume)
URL: https://people.csail.mit.edu/rrw/likelihoods.pdf — read by the lead (checked: yes, text extracted).
- Table 1 (his personal estimates): EXP^NP ≠ BPP 99%; NEXP ⊄ P/poly 97%; L ≠ NP 95%; NP ⊄ SIZE(n^k) 93%;
  BPP ⊆ SUBEXP 90%; P ≠ PSPACE 90%; **P ≠ NP 80%**; **ETH 70%**; NC1 ≠ TC0 50%; NEXP ≠ EXP 45%; SETH 25%;
  NEXP ≠ coNEXP 20%; NSETH 15%; L ≠ RL 5%.
- Concrete stepping stones he names:
  - CAPP: deterministic O(2^n·poly(s)/α(n)) time for any super-polynomial α would imply NEXP ⊄ P/poly [Wil10].
  - L vs NP: SAT/Vertex Cover/Independent Set need n^{2cos(π/7)} time with n^{o(1)} space; 2cos(π/7) < 1.81, and
    current techniques provably cannot improve this exponent [Buss–Williams 2012]. He believes L ≠ NP will be proved
    long before P vs NP, but needs "extraordinarily clever" new ideas.
  - P vs PSPACE: no n^{1.0001} time lower bound is known for QBF (a linear-space PSPACE-complete problem) — "call to arms".
  - NP ⊄ SIZE(n^k): known for Σ2P (Kannan), ZPP^NP, MA/1 (Santhanam 2007); open for NP.
  - Notes that complexity theorists are more often wrong about lower-bound conjectures than upper-bound ones
    (e.g. non-rigidity of Hadamard matrices, Alman–Williams 2017).

## 2. Ryan Williams thread on X/Bluesky, 23 Nov 2026 (screenshots supplied by the director; secondary)
- (1) If P vs NP is resolved soon (next few months), he thinks that requires P = NP — and then "polynomial time"
  may not fit intuition; a refined, more "ultrafinitist" formulation would be wanted.
- (2) If P ≠ NP, he doubts it will be proved soon; we almost certainly must first resolve the "easier" P ≠ PSPACE or
  LOGSPACE ≠ NP; NP ⊄ P/poly is further out. "Prove that SAT on instances of length L doesn't have L^(1.01) size
  circuits first!" Expects AI to speed up building the needed literature "by orders of magnitude".
- (3) Independence from ZFC: the least likely option in his view; NP ⊄ P/poly might be more vulnerable to such issues.

## 3. Claimed refutation of ETH (found by the lead's web search; MUST be verified at primary sources)
Secondary source: HackerNoon, "OpenAI and Anthropic claim AI has disproved a 27-year-old computer science
hypothesis" (as of 29 Oct 2026): https://hackernoon.com/openai-and-anthropic-claim-ai-has-disproved-a-27-year-old-computer-science-hypothesis
- Claimed: on 16 Oct 2026, AI models at OpenAI and at Anthropic independently found a 2^{o(n)}-time algorithm for
  (counting) 3-SAT, refuting ETH (Impagliazzo–Paturi 1999). OpenAI paper "The Exponential Time Hypothesis is False"
  (67 pp.); Anthropic paper (49 pp., author line "Claude, Anthropic"), announced 26 Oct 2026.
- Both proofs reported checked in Lean; Anthropic reports only Lean's three standard axioms and an independent second
  checker, and notes "no machine checks that this file says what the paper says". OpenAI's Lean file reportedly
  proves a slightly weaker bound than its paper's headline, still enough to refute ETH.
- Community review organised by Impagliazzo, Paturi and Williams; they state their involvement "should not be taken
  as certification of the claim".
- Reported to be a galactic algorithm (no gain until astronomically large n).
- Consequences if correct (lead's inference, to be checked): SETH ⇒ ETH, so SETH and NSETH-type assumptions would also
  fall; hundreds of ETH-conditional lower bounds lose their basis; P vs NP itself is NOT resolved by this.
- Why it matters for the lab: (a) the P = NP-side direction now has real momentum; (b) Williams' algorithmic method
  turns non-trivial SAT algorithms for circuit classes into circuit lower bounds — does the new technique extend
  beyond 3-CNF? (c) the Lean artifacts likely contain formalized running-time arguments reusable by our
  formalization track.

## 4. Not used
- A tweet by @JFeltsy (cosmology speculation mentioning P ≠ NP): no mathematical content usable by the lab.
