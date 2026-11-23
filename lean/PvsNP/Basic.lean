/-
PvsNP lab — smoke-test module.

Purpose: confirm that the toolchain, Mathlib dependency and prebuilt cache work,
and that the relevant Mathlib computability definitions are importable.
Nothing in this file is a research claim.
-/
import Mathlib.Computability.TuringMachine.Computable
import Mathlib.Computability.Encoding

namespace PvsNP

/-- Mathlib's polynomial-time computability notion is available. -/
example : Type 1 := Turing.FinTM2

#check @Turing.TM2ComputableInPolyTime
#check @Turing.TM2ComputableInTime
#check @Turing.idComputableInPolyTime

/-- A trivially true sanity theorem, used to check the `#print axioms` pipeline. -/
theorem sanity : (2 : ℕ) + 2 = 4 := rfl

end PvsNP

#print axioms PvsNP.sanity
