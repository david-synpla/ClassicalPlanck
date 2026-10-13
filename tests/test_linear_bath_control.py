"""Sanity checks for the closed-form active-bath control (standard-library unittest)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from linear_bath_control import active_energy, ratio


class LinearBathTests(unittest.TestCase):
    def test_zero_external_drive(self):
        self.assertEqual(active_energy(1, .05, .65, 0), 0)
        self.assertEqual(ratio(.12, 0), 1)

    def test_positive_background_raises_ratio(self):
        u0 = active_energy(1, .05, .65, .3)
        self.assertGreater(u0, 0)
        self.assertGreater(ratio(.12, u0), 1)

    def test_high_frequency_has_less_extra_energy(self):
        u1 = active_energy(1, .05, .65, .3)
        u8 = active_energy(8, .05, .65, .3)
        self.assertGreater(u1, u8)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            ratio(0, .1)


if __name__ == "__main__":
    unittest.main()
