import math

def calculate_uict(m_planck: float, kappa: float, n: int) -> float:
    """Calcule la masse via UICT : m = m_Planck * κ^n"""
    return m_planck * (kappa ** n)

def calculate_ceml(coherence: float, entropy: float, epsilon: float = 1e-6) -> float:
    """Calcule le score CEML : C(Ψ)/(H(Ψ) + ε)"""
    # guardrails: clamp coherence and entropy to reasonable ranges
    C = max(0.0, min(1.0, float(coherence)))
    H = max(0.0, float(entropy))
    return C / (H + epsilon)

def calculate_hscale(C: float, E: float, R: float, D: float) -> float:
    """Calcule H-Scale : 0.3C + 0.2E + 0.3R + 0.2D"""
    # Clamp inputs to [0,1]
    Cc = max(0.0, min(1.0, float(C)))
    Ee = max(0.0, min(1.0, float(E)))
    Rr = max(0.0, min(1.0, float(R)))
    Dd = max(0.0, min(1.0, float(D)))
    return 0.3*Cc + 0.2*Ee + 0.3*Rr + 0.2*Dd
