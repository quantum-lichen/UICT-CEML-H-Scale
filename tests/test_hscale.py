import unittest
from utils.math_utils import calculate_hscale

class TestHScale(unittest.TestCase):
    def test_hscale_example(self):
        H = calculate_hscale(0.8, 0.7, 0.9, 0.8)
        self.assertAlmostEqual(H, 0.814, places=3)

if __name__ == "__main__":
    unittest.main()
