/-
UNELABORATED regression fixture for the pinned Lean v4.36.0-rc2 environment.
This fixture has not been compiled in the audit environment.

After importing this module into the environment read by Reach.lean, start at
QuarticQuery.ReachRegression.publicRoot. A complete traversal must reach
QuarticQuery.ReachRegression.publicLeaf through the private wrapper.
The raw dependency graph should retain the private declaration's actual name;
the presentation graph may hide it only after taking the complete closure.
-/
module

public import Mathlib

public section
namespace QuarticQuery.ReachRegression

theorem publicLeaf : (1 : Nat) = 1 := rfl

private theorem privateWrapper : (1 : Nat) = 1 := by
  exact publicLeaf

theorem publicRoot : (1 : Nat) = 1 := by
  exact privateWrapper

end QuarticQuery.ReachRegression
