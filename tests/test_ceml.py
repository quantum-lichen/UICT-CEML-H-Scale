import unittest
from utils.math_utils import calculate_ceml

class TestCEML(unittest.TestCase):
    def test_ceml_basic(self):
        score = calculate_ceml(0.8, 0.1)
        self.assertGreater(score, 0.0)
        # score should be roughly 8.0 (0.8 / 0.1)
        self.assertAlmostEqual(score, 0.8 / 0.1, places=3)

if __name__ == "__main__":
    unittest.main()
