# BCP Simulator - main.py
"""
BCP Protocol v1.0
Copyright (c) 2025 Bryan Ouellette
Licence : CC-BY-NC-ND 4.0
"""
from dataclasses import dataclass
from typing import Any
import yaml
import os

from utils.math_utils import calculate_uict, calculate_ceml, calculate_hscale

# Default constants (can be overridden by config)
PLANCK_MASS = 2.176e-8  # kg
GOLDEN_RATIO = 1.61803398875
KAPPA = 0.9997  # Coefficient de compression UICT

# Try to load config if present
CONFIG_PATH = os.path.join("config", "bcp_config.yaml")
if os.path.exists(CONFIG_PATH):
    try:
        with open(CONFIG_PATH, "r") as f:
            _cfg = yaml.safe_load(f)
            PLANCK_MASS = float(_cfg.get("planck_mass", PLANCK_MASS))
            GOLDEN_RATIO = float(_cfg.get("golden_ratio", GOLDEN_RATIO))
            KAPPA = float(_cfg.get("kappa", KAPPA))
    except Exception:
        # conservative: keep defaults on failure
        pass

@dataclass
class Particle:
    name: str
    n: int  # Profondeur topologique
    mass: float = None  # Calculée via UICT

    def __post_init__(self):
        self.mass = calculate_uict(PLANCK_MASS, KAPPA, self.n)

@dataclass
class CognitiveSystem:
    coherence: float
    entropy: float
    resonance: float
    durability: float

    def ceml_score(self) -> float:
        return calculate_ceml(self.coherence, self.entropy)

    def hscale_score(self) -> float:
        # For H-Scale, we map input resonance/durability to E,R,D values.
        E = self.entropy if isinstance(self.entropy, float) else 0.0
        return calculate_hscale(self.coherence, E, self.resonance, self.durability)

def demo():
    # --- Simulation UICT ---
    electron = Particle("Électron", 43)
    proton = Particle("Proton", 33)
    print(f"Masse Électron (UICT) : {electron.mass:.6e} kg (référence: 9.109e-31 kg)")
    print(f"Masse Proton (UICT)  : {proton.mass:.6e} kg (référence: 1.672e-27 kg)")

    # --- Simulation CEML / H-Scale ---
    system = CognitiveSystem(
        coherence=0.85,
        entropy=0.15,
        resonance=0.9,
        durability=0.8
    )
    print(f"CEML Score : {system.ceml_score():.3f} (Seuil stable : > 0.618)")
    print(f"H-Scale     : {system.hscale_score():.3f} (Seuil éthique : > 0.618)")

if __name__ == "__main__":
    demo()
