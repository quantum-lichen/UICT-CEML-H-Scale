import unittest
from main import Particle

class TestUICT(unittest.TestCase):
    def test_electron_mass_property(self):
        electron = Particle("Électron", 43)
        # Ensure mass is computed and is a float
        self.assertIsInstance(electron.mass, float)
        self.assertGreater(electron.mass, 0.0)

    def test_proton_mass_property(self):
        proton = Particle("Proton", 33)
        self.assertIsInstance(proton.mass, float)
        self.assertGreater(proton.mass, 0.0)

if __name__ == "__main__":
    unittest.main()
