#!/usr/bin/env python3
"""Generate docs/lean_links.json: reader names and pinned GitHub lines for cited Lean.

The three manuscripts in docs/ name Lean objects in mathematical words and link each name
to the exact lines that state it, in the style

    the [headline theorem][thm-headline] ...

    [thm-headline]: https://github.com/wcook04/quartic-query-lean/blob/<commit>/lean/...#L328-L335

This program owns the link targets. CITATIONS below gives each label its reader
name and its Lean target: a declaration (found by parsing the file as it stands at
the pinned commit), a contiguous run of declarations, or a whole file or folder.
For declarations in a Comparator Challenge, the record from corpus/comparator_map.json
(its credit and the configuration that checks it) is copied beside the link.

Outputs:
  - docs/lean_links.json, the registry;
  - in each manuscript, the block of reference definitions between the markers
    `<!-- lean-links -->` and `<!-- /lean-links -->`, holding exactly the labels
    that manuscript uses.
  - in each shorter paper and its bibliography, links into docs/reasoning_record.md rewritten to
    RECORD_COMMIT, so a reader reaches the record text the paper was written
    against; an anchor missing at that commit is an error.

A target whose file is absent at the pinned commit is linked to the same lines on
`main` from the working tree and marked "pinned": false; --check reports these.
Bump COMMIT once those files are committed. Bump RECORD_COMMIT after committing
the revised record; this does not change its own Lean links or source bytes.
Labels are read from `][label]` uses in
the manuscripts; an unknown label is an error.

    python3 tools/build_lean_links.py [--check]
"""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_comparator_map  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/lean_links.json"
COMPARATOR_MAP = ROOT / "corpus/comparator_map.json"
PAPERS = ["docs/expert_companion.md", "docs/exposition.md", "docs/reasoning_record.md"]
RECORD_BIBLIOGRAPHIES = ["docs/expert_companion.bib"]
SCHEMA = "quartic-lean-links-v1"
REPOSITORY = "https://github.com/wcook04/quartic-query-lean"
# The commit the papers describe. Every pinned link resolves against this tree.
COMMIT = "8357f268732746d1575e05e7de8c888e20ad3793"
RECORD_COMMIT = "79d996f8f09bae7baa335f73bc11106d251af07e"
BEGIN, END = "<!-- lean-links -->", "<!-- /lean-links -->"
USE = re.compile(r"\]\[([A-Za-z0-9][A-Za-z0-9-]*)\]")
# The record edition is independent of the Lean source edition.
RECORD = "docs/reasoning_record.md"
RECORD_LINK = re.compile(re.escape(REPOSITORY) + r"/blob/([0-9a-f]{40}|main)/" + re.escape(RECORD)
                         + r"(?:#([A-Za-z0-9_.:-]+))?(?=[\s)<>\]}]|$)")

UNCONDITIONAL = "lean/QuarticCorpus/Unconditional/Challenge.lean"
Q = "QuarticQuery."

# label: (reader name, path, declarations or None for the whole file or folder)
CITATIONS = {
    # The statement Comparator checks for Theorem 1, and its configuration.
    "statement-file": ("the statement file", UNCONDITIONAL, None),
    "statement-config": ("the Comparator configuration of the four theorems",
                         "lean/QuarticCorpus/Unconditional/comparator.json", None),
    "statement-receipt": ("the recorded paranoid Comparator run of the four theorems",
                          "corpus/receipts/comparator-Unconditional-2026-11-03T121735042729+0000.json", None),
    "statement-solution": ("the proofs Comparator checks against the statement file",
                           "lean/QuarticCorpus/Unconditional/Solution.lean", None),
    "def-partial": ("partial Boolean functions", UNCONDITIONAL, [Q + "PartialBool"]),
    "def-totalise": ("totalisation", UNCONDITIONAL, [Q + "totalise"]),
    "def-tree": ("decision trees and their depth", UNCONDITIONAL,
                 [Q + "QueryTree", Q + "QueryTree.eval", Q + "QueryTree.depth"]),
    "def-randomized": ("randomized algorithms", UNCONDITIONAL,
                       [Q + "RandomizedProgram", Q + "RandomizedProgram.depth",
                        Q + "RandomizedProgram.success"]),
    "def-RLe": ("the randomized budget test", UNCONDITIONAL, [Q + "RLe"]),
    "def-R": ("the definition of R", UNCONDITIONAL, [Q + "R"]),
    "def-basis": ("the basis states", UNCONDITIONAL, [Q + "Basis", Q + "State"]),
    "def-oracle": ("the bit oracle", UNCONDITIONAL, [Q + "bitOracle"]),
    "def-adaptive": ("quantum query algorithms", UNCONDITIONAL, [Q + "AdaptiveProgram"]),
    "def-querycap": ("the query cap", UNCONDITIONAL, [Q + "AdaptiveProgram.queryCap"]),
    "def-QLe": ("the quantum budget test", UNCONDITIONAL, [Q + "QLe"]),
    "def-Q": ("the definition of Q", UNCONDITIONAL, [Q + "Q"]),
    "def-numerator": ("the Forrelation numerator", UNCONDITIONAL, [Q + "forrelationNumerator"]),
    "def-P": ("the definition of P", UNCONDITIONAL, [Q + "P"]),
    "def-circuit": ("fan-in-two circuits", UNCONDITIONAL, [Q + "Gate", Q + "Circuit"]),
    "def-realises": ("exact circuits for P", UNCONDITIONAL, [Q + "CircuitRealises"]),
    "def-bitloc": ("the input bits of a column", UNCONDITIONAL, [Q + "BitLoc"]),
    "def-wins": ("the winning condition", UNCONDITIONAL, [Q + "WinsAt"]),
    "def-F": ("the definition of F", UNCONDITIONAL, [Q + "addressedF", Q + "Fkm"]),
    "def-comparison": ("the unused comparison predicate", UNCONDITIONAL,
                       [Q + "Tournament.IsComparison"]),
    "def-output-mass": ("the output probability of a quantum algorithm", UNCONDITIONAL,
                        [Q + "project", Q + "AdaptiveProgram.outputMass"]),
    "def-gate": ("gate consistency", UNCONDITIONAL, [Q + "GateConsistent"]),
    "def-pointer": ("pointer decoding", UNCONDITIONAL, [Q + "readPointerBit", Q + "pointerEquiv"]),
    "def-L": ("the definition of L", UNCONDITIONAL, [Q + "Lvalue"]),
    "def-G": ("the definition of G", UNCONDITIONAL, [Q + "Gvalue"]),
    "def-bansal-sinha": ("the Forrelation hardness statement", UNCONDITIONAL,
                         [Q + "BansalSinhaLower"]),
    "def-universal": ("the universal power bound", UNCONDITIONAL, [Q + "UniversalPower"]),
    "def-alpha": ("the definition of the optimal exponent", UNCONDITIONAL, [Q + "alphaTot"]),
    "thm-all": ("the four compared theorems", UNCONDITIONAL,
                [Q + "Checked.alpha_tot_eq_four", Q + "Checked.theorem_one_one",
                 Q + "Checked.cubic_bound_fails", Q + "Checked.forrelation_lower_bound"]),
    "thm-alpha": ("the exponent theorem", UNCONDITIONAL, [Q + "Checked.alpha_tot_eq_four"]),
    "thm-headline": ("the headline theorem", UNCONDITIONAL, [Q + "Checked.theorem_one_one"]),
    "thm-cubic": ("the failure of the cubic bound", UNCONDITIONAL,
                  [Q + "Checked.cubic_bound_fails"]),
    "thm-forrelation": ("the Forrelation lower bound", UNCONDITIONAL,
                        [Q + "Checked.forrelation_lower_bound"]),
    # Other compared statements.
    "cmp-lemma22": ("four facts about winners", "lean/QuarticCorpus/Construction/Challenge.lean",
                    None),
    "cmp-lemma22-full": ("Lemma 2.2 as one statement",
                         "lean/QuarticCorpus/Independent/ConstructionFull/Challenge.lean",
                         [Q + "Paper.construction_lemma_2_2_with_support"]),
    "cmp-eq11": ("the erased-zero identity with the bound 4G/m^2",
                 "lean/QuarticCorpus/Independent/Eq19/Challenge.lean",
                 [Q + "Independent.Eq19.checked_eq19"]),
    "cmp-negative": ("the five wrong solutions", "lean/QuarticCorpus/Negative", None),
    "cmp-amplifier": ("bounded amplification returning the good state",
                      "lean/QuarticCorpus/Independent/UniformAmplifier/Challenge.lean",
                      [Q + "Upper.uniformOpaqueAmplifier"]),
    "amplifier-config": ("the Comparator configuration of the amplifier statement",
                         "lean/QuarticCorpus/Independent/UniformAmplifier/comparator.json", None),
    "amplifier-solution": ("the proof checked against the amplifier statement",
                           "lean/QuarticCorpus/Independent/UniformAmplifier/Solution.lean", None),
    "cmp-direct-product": ("the direct product with independent randomness",
                           "lean/QuarticCorpus/Independent/RealizedCaps/Challenge.lean",
                           [Q + "direct_product_external_finite_realized_caps"]),
    "direct-product-config": ("the Comparator configuration of the direct-product statement",
                              "lean/QuarticCorpus/Independent/RealizedCaps/comparator.json", None),
    "def-compliant": ("success together with respecting the caps",
                      "lean/QuarticQuery/LowerBound/RealizedCaps.lean", [Q + "compliantSuccess"]),
    "def-hit": ("the hitting probability and expected count",
                "lean/QuarticCorpus/Independent/Eq19/Spec.lean",
                [Q + "Independent.Eq19.hitProbability", Q + "Independent.Eq19.expectedCount"]),
    "cmp-zero-cost": ("zero-cost characterisation of D, R and Q",
                      "lean/QuarticCorpus/Independent/ModelZero/Challenge.lean",
                      [Q + "Independent.ModelZero.checked_zero_query_characterization"]),
    "cmp-degree": ("degree conventions", "lean/QuarticCorpus/Independent/Degree/Challenge.lean",
                   [Q + "Independent.Degree.checked_degree_conventions"]),
    # Exact implementation statements used by the reasoning record.
    "src-equation-two": ("the construction-family equation", "lean/QuarticQuery/Paper/ConstructionFamily.lean", ["QuarticQuery.Paper.construction_equation_two"]),
    "src-q-bound": ("the quantum query bound with logarithmic exponent six", "lean/QuarticQuery/Upper/Bound.lean", ["QuarticQuery.Upper.Q_Fkm_le"]),
    "src-quantum-tournament": ("the quantum tournament bound", "lean/QuarticQuery/Paper/QuantumTournamentFacts.lean", ["QuarticQuery.Paper.quantumTournament"]),
    "src-construction-full": ("the construction lemma with physical-coordinate support", "lean/QuarticQuery/Paper/ConstructionFull.lean", ["QuarticQuery.Paper.construction_lemma_2_2_with_support"]),
    "src-amplification": ("the abstract bounded amplification statement", "lean/QuarticQuery/Amplification/Bounded.lean", ["QuarticQuery.Amplification.bounded_amplification"]),
    "src-opaque-amplifier": ("the opaque-preparation amplifier", "lean/QuarticQuery/Upper/UniformEndpoint.lean", ["QuarticQuery.Upper.uniformOpaqueAmplifier"]),
    "src-direct-product-average": ("the finite-seed averaged direct product", "lean/QuarticQuery/Paper/ClassicalDirectProduct.lean", ["QuarticQuery.Paper.classical_direct_product_average"]),
    "src-direct-product-caps": ("the direct product with realized caps", "lean/QuarticQuery/LowerBound/RealizedCapsExternal.lean", ["QuarticQuery.direct_product_external_finite_realized_caps"]),
    "src-equation-19": ("the whole erased-zero identity and bound", "lean/QuarticQuery/Paper/Eq19Whole.lean", ["QuarticQuery.Paper.eq19_whole"]),
    "src-universal-power": ("the universal quartic power bound", "lean/QuarticQuery/Appendix/TheoremA1.lean", ["QuarticQuery.universalPower_four"]),
    # Built theorems outside every Comparator configuration.
    "src-constants": ("Theorem 1 with the constants 6 and 1/400",
                      "lean/QuarticQuery/Paper/ConstructionFamily.lean",
                      [Q + "Paper.construction_family_named"]),
    "src-forrelation-uniform": ("the uniform Forrelation estimate",
                                "lean/QuarticQuery/ForrelationLower/Uniform.lean",
                                [Q + "forrelation_lower_uniform_sharp"]),
    "src-budget": ("the explicit quantum budget", "lean/QuarticQuery/Upper/Bound.lean",
                   [Q + "Upper.budget_le"]),
    "src-budget-exponential": ("the quantum bound with constant 2^53 k 2^(10k)",
                               "lean/QuarticQuery/Upper/Bound.lean", [Q + "Upper.Q_Fkm_le_exponential"]),
    "src-amplify-measured": ("bounded amplification of the measured label",
                             "lean/QuarticQuery/Upper/Amplify.lean", [Q + "Upper.Samples.amplify"]),
    "src-per-time": ("the per-time event", "lean/QuarticQuery/Paper/ClassicalPlanted.lean",
                     [Q + "Paper.eq_21"]),
    "src-zero-two": ("the bound 2G/m^2", "lean/QuarticQuery/Paper/ClassicalPlanted.lean",
                     [Q + "Paper.erasedZero_le_two"]),
    "src-zero-successor": ("the induction with |U|+1",
                           "lean/QuarticQuery/LowerBound/Planted/ZeroSearchSuccessor.lean",
                           [Q + "zero_search_sum_successor"]),
    "src-reach": ("the dependency printer", "lean/scripts/Reach.lean", None),
    # Further declarations named by the reasoning record.
    "def-DLe": ("the deterministic budget test", UNCONDITIONAL, [Q + "DLe"]),
    "def-D": ("the definition of D", UNCONDITIONAL, [Q + "D"]),
    "def-bit-input": ("bit inputs", UNCONDITIONAL, [Q + "BitInput"]),
    "def-reindex": ("renaming the coordinates of a partial function", UNCONDITIONAL, [Q + "reindex"]),
    "cmp-le-iff": ("the compared equivalences between complexity bounds and budget tests",
                   "lean/QuarticCorpus/Foundations/Challenge.lean",
                   [Q + "Checked.R_le_iff", Q + "Checked.Q_le_iff", Q + "Checked.D_le_iff"]),
    "cmp-winners": ("the four compared winner theorems", "lean/QuarticCorpus/Construction/Challenge.lean",
                    [Q + "Checked.winsAt_unique", Q + "Checked.existsUnique_gateConsistent",
                     Q + "Checked.winner_no_incoming_zero", Q + "Checked.winner_finds_zero"]),
    "src-le-iff-classical": ("the classical equivalences between complexity bounds and budget tests",
                             "lean/QuarticQuery/Model/Classical.lean", [Q + "D_le_iff", Q + "R_le_iff"]),
    "src-le-iff-quantum": ("the quantum equivalence between complexity bounds and budget tests",
                           "lean/QuarticQuery/Model/Quantum.lean", [Q + "Q_le_iff"]),
    "src-complexitylib": ("the agreement of deterministic complexity with complexitylib",
                          "lean/QuarticQuery/Bridge/DecisionTree.lean", [Q + "D_totalise_eq_complexity"]),
    "src-fixed-sequence": ("the fixed-sequence normal form", "lean/QuarticQuery/Bridge/Deferred.lean",
                           [Q + "exists_fixedSequence"]),
    "src-construction-models": ("the domain wrappers of the construction",
                                "lean/QuarticQuery/Paper/ConstructionModels.lean", None),
    "src-query-oracle": ("the bit-oracle identities", "lean/QuarticQuery/Paper/ConstructionModels.lean",
                         [Q + "Paper.construction_query_oracle"]),
    "src-repetitions": ("the repetition count of the Forrelation sampler",
                        "lean/QuarticQuery/Forrelation/Repetition.lean", [Q + "Forrelation.repetitions"]),
    "src-walsh": ("the Walsh definitions", "lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean",
                  [Q + "Paper.construction_walsh_definitions"]),
    "src-forr-product": ("the alternating product and its threshold",
                         "lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean",
                         [Q + "Paper.construction_equation_3"]),
    "src-forr-promise": ("the complete Forrelation promise",
                         "lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean",
                         [Q + "Paper.construction_equation_4"]),
    "src-forr-integer": ("the integer form of the Forrelation numerator",
                         "lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean",
                         [Q + "Paper.construction_N_phi"]),
    "src-forr-tests": ("the integer comparisons and output rules",
                       "lean/QuarticQuery/Paper/ConstructionForrelationDefinitions.lean",
                       [Q + "Paper.construction_integer_tests"]),
    "src-forr-output-bits": ("the output rules of the constructed circuit",
                             "lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean",
                             [Q + "Paper.construction_forr_output_bits"]),
    "src-lemma21-ii": ("the coherent physical implementation of Lemma 2.1(ii)",
                       "lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean",
                       [Q + "Paper.construction_lemma_2_1_ii_complete"]),
    "src-forr-circuit-exists": ("the existence of the Forrelation circuit",
                                "lean/QuarticQuery/Forrelation/Circuit.lean", [Q + "Forrelation.exists_circuit"]),
    "src-lemma21-iii": ("the circuit bound of Lemma 2.1(iii)",
                        "lean/QuarticQuery/Paper/ConstructionForrelationCircuit.lean",
                        [Q + "Paper.construction_lemma_2_1_iii"]),
    "src-forr-census": ("the finite census of small Forrelation instances",
                        "lean/QuarticQuery/Forrelation/Sanity.lean", None),
    "src-lemma21": ("Lemma 2.1 as one statement", "lean/QuarticQuery/Paper/ConstructionForrelationComplete.lean",
                    [Q + "Paper.construction_lemma_2_1_complete"]),
    "src-forr-circuit": ("the canonical Forrelation circuit", "lean/QuarticQuery/Forrelation/Circuit.lean",
                         [Q + "Forrelation.forrCircuit"]),
    "src-forr-implementation": ("the proof of the Forrelation lower bound",
                                "lean/QuarticQuery/ForrelationLower/Main.lean",
                                [Q + "ForrelationLower.bansalSinhaLower"]),
    "src-construction-complete": ("the complete evaluator theorem for Lemma 2.2",
                                  "lean/QuarticQuery/Paper/ConstructionComplete.lean",
                                  [Q + "Paper.construction_lemma_2_2_complete"]),
    "src-pointer-support": ("the essential coordinates of the pointer tests",
                            "lean/QuarticQuery/Paper/ConstructionPointerSupport.lean",
                            [Q + "Paper.construction_pointer_every_physical_coordinate"]),
    "src-transcript": ("consistent transcripts are true evaluations",
                       "lean/QuarticQuery/Construction/Transcript.lean", [Q + "gateConsistent_iff_eq_circuitEval"]),
    "src-winner-unique": ("the uniqueness of the winning pair", "lean/QuarticQuery/Construction/Winner.lean",
                          [Q + "winsAt_unique"]),
    "src-winner-tests": ("winning as the conjunction of the local tests",
                         "lean/QuarticQuery/Construction/LocalTests.lean", [Q + "winsAt_iff_localTests"]),
    "src-winner-paper": ("the formal winning condition is the paper's",
                         "lean/QuarticQuery/Construction/LocalTests.lean", [Q + "winsAt_iff_paperWinsAt"]),
    "src-proc": ("abstract amplification procedures", "lean/QuarticQuery/Amplification/Procedure.lean",
                 [Q + "Amplification.Proc"]),
    "src-samples": ("coherent samplers", "lean/QuarticQuery/Upper/Sampler.lean", [Q + "Upper.Samples"]),
    "src-runs": ("bit-query programs with a given output law", "lean/QuarticQuery/Upper/Compile.lean",
                 [Q + "Upper.Runs"]),
    "src-coherent-amplify": ("the coherent trial loop of Lemma 3.1",
                             "lean/QuarticQuery/Paper/QuantumAmplification.lean",
                             [Q + "Paper.quantum_amplify_samples"]),
    "src-equation-15": ("the tensor preparation of equation (15)", "lean/QuarticQuery/Paper/QuantumTensor.lean",
                        [Q + "Paper.equation_15"]),
    "src-common-workspace": ("a common workspace for finitely many samplers",
                             "lean/QuarticQuery/Paper/QuantumWorkspace.lean",
                             [Q + "Paper.quantumWorkspace_uniformize"]),
    "src-tensor-stage": ("the tensor stage built from samplers", "lean/QuarticQuery/Paper/QuantumTensor.lean",
                         [Q + "Paper.quantumTensorStage_of_samples"]),
    "src-stage-sampler": ("the stage sampler of the tournament", "lean/QuarticQuery/Upper/Tournament.lean",
                          [Q + "Upper.stage_samples"]),
    "src-tournament-runs": ("the acceptance guarantee of the tournament", "lean/QuarticQuery/Upper/Tournament.lean",
                            [Q + "Upper.tournament_runs"]),
    "src-decoder": ("the correctness of the decoder", "lean/QuarticQuery/Paper/QuantumComparison.lean",
                    [Q + "Paper.quantumDecode_correct"]),
    "src-comparison-state": ("the comparison state", "lean/QuarticQuery/Paper/QuantumComparison.lean",
                             [Q + "Paper.quantumComparison_state"]),
    "src-winner-dominates": ("the dominance of the winner", "lean/QuarticQuery/Paper/QuantumComparison.lean",
                             [Q + "Paper.quantumWinner_dominates"]),
    "src-verifier": ("the verifier", "lean/QuarticQuery/Paper/QuantumComparison.lean",
                     [Q + "Paper.quantumVerify"]),
    "src-error-bound": ("the error bound of the complete algorithm",
                        "lean/QuarticQuery/Paper/QuantumComparison.lean", [Q + "Paper.quantumError_bound"]),
    "src-prop33": ("Proposition 3.3 as an algorithm for the canonical circuit",
                   "lean/QuarticQuery/Upper/Bound.lean", [Q + "Upper.Fkm_forrCircuit_QLe"]),
    "src-budget-constant": ("the constant of the explicit quantum budget", "lean/QuarticQuery/Upper/Bound.lean",
                            [Q + "Upper.budgetConst"]),
    "src-direct-product-module": ("the weighted direct-product development",
                                  "lean/QuarticQuery/LowerBound/DirectProduct.lean", None),
    "src-direct-product": ("the weighted direct product", "lean/QuarticQuery/LowerBound/DirectProduct.lean",
                           [Q + "direct_product"]),
    "src-conditional-value-module": ("the conditional-value development",
                                     "lean/QuarticQuery/Paper/ClassicalDirectProduct.lean", None),
    "src-direct-product-capped": ("the capped direct product by conditional values",
                                  "lean/QuarticQuery/Paper/ClassicalDirectProduct.lean",
                                  [Q + "Paper.classical_direct_product"]),
    "src-complies": ("compliance with the caps", "lean/QuarticQuery/LowerBound/RealizedCaps.lean",
                     [Q + "OutTree.actualComplies"]),
    "src-count": ("the number of queries to each instance", "lean/QuarticQuery/LowerBound/RealizedCaps.lean",
                  [Q + "OutTree.actualCount"]),
    "src-erased-zero-identity": ("the identity Pr[hit] = E Z/m",
                                 "lean/QuarticQuery/Paper/ClassicalPlanted.lean",
                                 [Q + "Paper.erasedZero_eq_expectedZeros_div"]),
    "src-erased-zero-bound": ("the erased-zero bound with coefficient four",
                              "lean/QuarticQuery/Paper/ClassicalPlanted.lean", [Q + "Paper.eq_19"]),
    "src-equation-19-expectation": ("the erased-zero identity with the bound on E Z/m",
                                    "lean/QuarticQuery/Paper/Eq19Complete.lean", [Q + "Paper.eq_19_complete"]),
    "src-dummy": ("the dummy input", "lean/QuarticQuery/LowerBound/Planted/Inputs.lean", [Q + "dummy"]),
    "src-found-zero": ("the event that the dummy run finds a zero",
                       "lean/QuarticQuery/LowerBound/Planted/ZeroSearch.lean", [Q + "foundZero"]),
    "src-coupled-average": ("the joint average over the addresses, zeros and planted column",
                            "lean/QuarticQuery/LowerBound/Planted/Main.lean", [Q + "coupledAvg"]),
    "src-discovered-zeros": ("the number of discovered zeros", "lean/QuarticQuery/Paper/ClassicalPlanted.lean",
                             [Q + "Paper.discoveredZeros"]),
    "src-expected-zeros": ("the expected number of discovered zeros",
                           "lean/QuarticQuery/Paper/ClassicalPlanted.lean", [Q + "Paper.expectedZeros"]),
    "src-uniform-zero": ("the uniform position of an unseen zero",
                         "lean/QuarticQuery/Paper/ClassicalUniformZero.lean",
                         [Q + "Paper.uniform_zero_given_transcript"]),
    "src-expected-zeros-bound": ("the bound E Z <= 4G/m", "lean/QuarticQuery/Paper/ClassicalPlanted.lean",
                                 [Q + "Paper.expectedZeros_le_four"]),
    "src-prop42": ("Proposition 4.2, for every realising circuit and for the canonical circuit",
                   "lean/QuarticQuery/Paper/Section4.lean", [Q + "Paper.prop_4_2", Q + "Paper.prop_4_2_forrCircuit"]),
    "src-planted-core": ("the conditional planted lower bound", "lean/QuarticQuery/LowerBound/Planted/Main.lean",
                         [Q + "Gvalue_lt_R_Fkm"]),
    "src-ratio-arithmetic": ("the finite quotient calculation", "lean/QuarticQuery/Paper/ClassicalAsymptotics.lean",
                             [Q + "Paper.classical_ratio_arithmetic"]),
    "src-ratio-abstract": ("the exponent ratio for abstract sequences",
                           "lean/QuarticQuery/Paper/ClassicalAsymptotics.lean",
                           [Q + "Paper.classical_exponent_ratio"]),
    "src-ratio-family": ("the exponent ratio for the named family",
                         "lean/QuarticQuery/Paper/ClassicalAsymptotics.lean", [Q + "Paper.classical_Fkm_ratio"]),
    "src-eventual-comparison": ("the eventual strict comparison of powers",
                                "lean/QuarticQuery/Results/Exponent.lean", [Q + "eventually_gt_rpow"]),
    "src-exponent-choice": ("the choice of k beating a given exponent",
                            "lean/QuarticQuery/Results/Exponent.lean", [Q + "exists_nat_exponent"]),
    "src-no-smaller-exponent": ("the exclusion of exponents below four",
                                "lean/QuarticQuery/Results/Exponent.lean", [Q + "not_universalPower_of_family"]),
    "src-alpha-infimum": ("the infimum argument for the exponent",
                          "lean/QuarticQuery/Results/Exponent.lean", [Q + "alphaTot_eq_four_of"]),
    "src-alpha": ("the unconditional exponent theorem", "lean/QuarticQuery/Results/Unconditional.lean",
                  [Q + "alphaTot_eq_four_unconditional"]),
    "src-theorem": ("the unconditional Theorem 1.1", "lean/QuarticQuery/Results/Unconditional.lean",
                    [Q + "theorem_1_1_unconditional"]),
    "src-cubic": ("the unconditional failure of the cubic bound", "lean/QuarticQuery/Results/Unconditional.lean",
                  [Q + "cubic_bound_fails_unconditional"]),
    "src-family-conditional": ("the family bounds under the lower-bound premise",
                               "lean/QuarticQuery/Results/Conditional.lean", [Q + "family_bounds"]),
    "src-theorem-conditional": ("Theorem 1.1 under the Forrelation hardness hypothesis",
                                "lean/QuarticQuery/Results/Conditional.lean", [Q + "theorem_1_1"]),
    "src-lemma-a2": ("the spectral-adversary lemma", "lean/QuarticQuery/Paper/AppendixASpectralAdversary.lean",
                     [Q + "Paper.appendixA_lemmaA2"]),
    "src-lemma-a3": ("the star and sensitivity estimates", "lean/QuarticQuery/Paper/AppendixAStar.lean",
                     [Q + "Paper.appendixA_lemmaA3_adversary"]),
    "src-lemma-a4": ("the degree bound through spectral sensitivity",
                     "lean/QuarticQuery/Paper/AppendixAHuangRoute.lean", [Q + "Paper.appendixA4_paper_route"]),
    "src-lemma-a5": ("the bridge to Midrijanis's bound", "lean/QuarticQuery/Paper/AppendixASensitivity.lean",
                     [Q + "Paper.appendixA_lemmaA5"]),
    "src-quartic-cap": ("the quartic bound at a quantum query cap", "lean/QuarticQuery/Paper/AppendixA.lean",
                        [Q + "Paper.appendixA_D_le_of_QLe"]),
    "src-quartic-minimum": ("the quartic bound at the attained quantum minimum",
                            "lean/QuarticQuery/Paper/AppendixA.lean", [Q + "Paper.appendixA_D_le_Q_pow_four"]),
    "src-theorem-a1": ("Theorem A.1 in its displayed form", "lean/QuarticQuery/Paper/AppendixA.lean",
                       [Q + "Paper.appendixA_theoremA1"]),
    "src-quartic-older": ("the quartic bound with coefficient 20736", "lean/QuarticQuery/Appendix/TheoremA1.lean",
                          [Q + "D_le_Q_pow_four"]),
    "src-quartic-hybrid": ("the hybrid quartic bound with coefficient 19600",
                           "lean/QuarticQuery/Paper/AppendixA.lean", [Q + "Paper.appendixA_D_le_Q_pow_four_hybrid"]),
}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def at_commit(path, commit=None):
    """The kind and file text at the selected revision, or (None, None)."""
    commit = COMMIT if commit is None else commit
    kind = git("cat-file", "-t", f"{commit}:{path}")
    if kind.returncode:
        return None, None
    kind = kind.stdout.strip()
    if kind != "blob":
        return kind, None
    shown = git("show", f"{commit}:{path}")
    if shown.returncode:
        raise SystemExit(f"cannot read {path} at {commit}: {shown.stderr.strip()}")
    return kind, shown.stdout


def comparator_rows():
    data = json.loads(COMPARATOR_MAP.read_text(encoding="utf-8"))
    rows = {}
    for challenge in data["challenges"]:
        configs = [c for c in challenge["configurations"] if c["role"] == "positive"]
        for block in challenge["blocks"]:
            rows[(challenge["path"], block["name"])] = {
                "credit": block["comparison"]["credit"],
                "configurations": [c["path"] for c in configs],
                "map_lines": [block["line_start"], block["line_end"]],
            }
    return rows


def locate(text, names, path):
    blocks = {b["name"]: b for b in build_comparator_map.lean_blocks(text)}
    found = []
    for name in names:
        if name not in blocks:
            raise SystemExit(f"{path}: no declaration {name}")
        found.append(blocks[name])
    order = sorted(found, key=lambda b: b["line_start"])
    return order[0]["line_start"], statement_end(order[-1])


def statement_end(block):
    """Last line of a theorem's statement (its proof is not linked); a definition's last line."""
    if block["kind"] not in ("theorem", "lemma"):
        return block["line_end"]
    cut = proof_start(block["text"])
    if cut < 0:
        return block["line_end"]
    return block["line_start"] + block["text"][:cut].count("\n")


def proof_start(text):
    """Offset of the `:=` that begins a theorem's proof, or -1.

    A statement can itself contain `let x := e` or `have h := e` bindings, so the
    proof begins at the first `:=` outside brackets whose line has not opened such
    a binding before it.
    """
    depth = 0
    for index, char in enumerate(text):
        if char in "([{⟨":
            depth += 1
        elif char in ")]}⟩":
            depth -= 1
        elif text.startswith(":=", index) and depth == 0:
            line = text[text.rfind("\n", 0, index) + 1:index]
            if not re.search(r"(^|[\s(;])(let|have)\s", line):
                return index
    return -1


def build():
    rows = comparator_rows()
    links = {}
    unpinned = []
    for label, (reader, path, names) in sorted(CITATIONS.items()):
        kind, text = at_commit(path)
        pinned = kind is not None
        if not pinned:
            local = ROOT / path
            if not local.exists():
                raise SystemExit(f"{label}: {path} exists neither at {COMMIT[:12]} nor in the checkout")
            kind = "tree" if local.is_dir() else "blob"
            text = local.read_text(encoding="utf-8") if kind == "blob" else None
            unpinned.append(label)
        ref = COMMIT if pinned else "main"
        entry = {"reader_name": reader, "path": path, "pinned": pinned}
        if names:
            start, end = locate(text, names, path)
            entry["declarations"] = names
            entry["lines"] = [start, end]
            anchor = f"#L{start}" if start == end else f"#L{start}-L{end}"
            entry["url"] = f"{REPOSITORY}/blob/{ref}/{path}{anchor}"
            compared = [rows[(path, n)] for n in names if (path, n) in rows]
            if compared:
                entry["comparator"] = {
                    "credit": sorted({r["credit"] for r in compared}),
                    "configurations": sorted({c for r in compared for c in r["configurations"]}),
                }
                stale = [n for n in names if (path, n) in rows
                         and rows[(path, n)]["map_lines"][0] != locate(text, [n], path)[0]]
                if stale:
                    entry["comparator"]["map_lines_differ"] = stale
        else:
            entry["url"] = f"{REPOSITORY}/{kind}/{ref}/{path}"
        links[label] = entry
    registry = {
        "schema": SCHEMA,
        "generated_by": "tools/build_lean_links.py",
        "repository": REPOSITORY,
        "commit": COMMIT,
        "boundary": ("Reading aid: plain names and line links for Lean objects cited in "
                     "docs/expert_companion.md, docs/exposition.md and docs/reasoning_record.md. Line ranges are read from "
                     "the pinned commit; an entry with \"pinned\": false points at main and must "
                     "be re-pinned once its file is committed. No Lean or Comparator run is "
                     "implied by an entry."),
        "links": links,
    }
    return registry, unpinned


def render(value):
    return json.dumps(value, indent=1, ensure_ascii=False) + "\n"


def paper_block(text, links, paper):
    # Every `][label]` use needs a definition: from the registry, or written by hand
    # elsewhere in the paper.
    defined_by_hand = set(re.findall(r"^\[([^\]]+)\]:", text, re.M))
    used = sorted(set(USE.findall(text)) - defined_by_hand)
    unknown = [u for u in used if u not in links]
    if unknown:
        raise SystemExit(f"{paper}: unknown Lean link labels {', '.join(unknown)}")
    lines = [BEGIN] + [f"[{label}]: {links[label]['url']}" for label in used] + [END]
    return "\n".join(lines)


def record_anchors(text):
    """Explicit anchors and Pandoc heading identifiers of the record."""
    found = set(re.findall(r"<a\s+(?:id|name)=\"([^\"]+)\"", text)) | set(re.findall(r"\{#([^}\s]+)", text))
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*(?:\{[^}]*\})?$", text):
        found.add(re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-"))
    return found


def pin_record_links(text, paper):
    """Point record links at their own edition and check anchors in those bytes."""
    _, record = at_commit(RECORD, RECORD_COMMIT)
    if record is None:
        raise SystemExit(f"{RECORD} is absent at {RECORD_COMMIT[:12]}")
    known = record_anchors(record)
    missing = sorted({m.group(2) for m in RECORD_LINK.finditer(text) if m.group(2)} - known)
    if missing:
        raise SystemExit(f"{paper}: record anchors absent at {RECORD_COMMIT[:12]}: {', '.join(missing)}")
    return RECORD_LINK.sub(lambda m: f"{REPOSITORY}/blob/{RECORD_COMMIT}/{RECORD}"
                           + (f"#{m.group(2)}" if m.group(2) else ""), text)


def updated_paper(paper, links):
    text = (ROOT / paper).read_text(encoding="utf-8")
    if paper != RECORD:
        text = pin_record_links(text, paper)
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    body = pattern.sub("", text)
    block = paper_block(body, links, paper)
    if pattern.search(text):
        return pattern.sub(lambda _: block, text, count=1)
    return text.rstrip("\n") + "\n\n" + block + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true",
                        help="fail if docs/lean_links.json or a paper's link block is stale")
    args = parser.parse_args()
    registry, unpinned = build()
    outputs = {OUTPUT: render(registry)}
    for paper in PAPERS:
        outputs[ROOT / paper] = updated_paper(paper, registry["links"])
    for bibliography in RECORD_BIBLIOGRAPHIES:
        outputs[ROOT / bibliography] = pin_record_links(
            (ROOT / bibliography).read_text(encoding="utf-8"), bibliography)
    if unpinned:
        print(f"lean links not pinned to {COMMIT[:12]} (file absent there): {', '.join(unpinned)}",
              file=sys.stderr)
    if args.check:
        stale = [p.relative_to(ROOT).as_posix() for p, text in outputs.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            raise SystemExit("stale: " + ", ".join(stale) + "; run python3 tools/build_lean_links.py")
        print(f"lean links current: {len(registry['links'])} labels at {COMMIT[:12]}")
        return
    for path, text in outputs.items():
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(registry['links'])} labels)")


if __name__ == "__main__":
    main()
