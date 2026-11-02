import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "tools/return_checks/semantic_controls.py"
SPEC = importlib.util.spec_from_file_location("semantic_controls", PATH)
CONTROLS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONTROLS)


class SemanticControlsTests(unittest.TestCase):
    def test_constant_mixture_uses_one_probability_for_all_promised_inputs(self):
        self.assertFalse(CONTROLS.constant_mixture_succeeds((False, True), Fraction(2, 3)))
        self.assertTrue(CONTROLS.constant_mixture_succeeds((False, True), Fraction(1, 2)))
        self.assertTrue(CONTROLS.constant_mixture_succeeds((None, True), Fraction(2, 3)))
        self.assertTrue(CONTROLS.input_dependent_constant_succeeds((False, True), Fraction(2, 3)))

    def test_inclusive_or_witness_has_the_expected_exact_probabilities(self):
        self.assertEqual(CONTROLS.or_two_mixture_successes(), {
            "00": Fraction(2, 3), "01": Fraction(2, 3),
            "10": Fraction(2, 3), "11": Fraction(1),
        })

    def test_four_point_walsh_witness_distinguishes_promise_cases(self):
        phi = CONTROLS.phi_two_four((-1, 1, 1, 1), (-1, 1, 1, 1))
        self.assertEqual(phi, -1)
        self.assertIsNone(CONTROLS.promise_value(phi))
        self.assertTrue(CONTROLS.promise_value(phi, absolute_high=True))
        self.assertFalse(CONTROLS.promise_value(Fraction(0)))
        self.assertTrue(CONTROLS.promise_value(Fraction(1)))

    def test_each_deliberate_mutation_breaks_its_expected_answer(self):
        self.assertEqual(CONTROLS.mismatches(CONTROLS.observe()), [])
        for mutation, intended_case in CONTROLS.MUTATIONS.items():
            with self.subTest(mutation=mutation):
                self.assertEqual(CONTROLS.mismatches(CONTROLS.observe(mutation)), [intended_case])

    def test_agreement_of_two_shared_bad_toy_specs_does_not_ensure_nonvacuity(self):
        report = CONTROLS.report()["toy_shared_bad_spec"]
        self.assertTrue(report["finite_truth_tables_agree"])
        self.assertFalse(report["has_valid_comparison"])
        self.assertFalse(report["comparator_executed"])
        self.assertTrue(any(CONTROLS.comparison_truth_table()))

    def test_invalid_mutation_is_not_silently_treated_as_the_baseline(self):
        with self.assertRaises(ValueError):
            CONTROLS.observe("not_a_real_mutation")


if __name__ == "__main__":
    unittest.main()
