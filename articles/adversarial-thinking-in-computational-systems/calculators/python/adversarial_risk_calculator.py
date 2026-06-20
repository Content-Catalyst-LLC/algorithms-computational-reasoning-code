# adversarial_risk_calculator.py
# Educational calculator for adversarial readiness, evasion, and residual risk.

from __future__ import annotations

from pathlib import Path
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ARTICLE_ROOT / "calculators" / "outputs"


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def readiness_score(threat_model: float, attack_surface: float, monitoring: float, defense_depth: float, incident_response: float, governance: float) -> float:
    return clamp(100.0 * (
        0.18 * threat_model
        + 0.18 * attack_surface
        + 0.18 * monitoring
        + 0.18 * defense_depth
        + 0.14 * incident_response
        + 0.14 * governance
    ))


def attack_success_probability(capability: float, exposure: float, control_strength: float) -> float:
    return clamp(100.0 * capability * exposure * (1.0 - control_strength))


def residual_risk(initial_risk: float, mitigation_effectiveness: float) -> float:
    return clamp(initial_risk * (1.0 - mitigation_effectiveness))


def threshold_evasion(original_score: float, adversarial_shift: float, threshold: float) -> dict[str, object]:
    shifted = original_score + adversarial_shift
    return {
        "original_score": original_score,
        "adversarial_shift": adversarial_shift,
        "threshold": threshold,
        "shifted_score": round(shifted, 6),
        "original_flagged": original_score >= threshold,
        "after_shift_flagged": shifted >= threshold,
        "evasion_success": original_score >= threshold and shifted < threshold,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    scenarios = [
        {
            "scenario": "strong_defense",
            "readiness": readiness_score(0.86, 0.82, 0.88, 0.82, 0.80, 0.78),
            "attack_success_probability": attack_success_probability(0.72, 0.62, 0.82),
            "residual_risk": residual_risk(78, 0.64),
        },
        {
            "scenario": "partial_defense",
            "readiness": readiness_score(0.62, 0.58, 0.54, 0.50, 0.46, 0.48),
            "attack_success_probability": attack_success_probability(0.76, 0.70, 0.44),
            "residual_risk": residual_risk(82, 0.38),
        },
        {
            "scenario": "weak_defense",
            "readiness": readiness_score(0.28, 0.34, 0.24, 0.20, 0.18, 0.22),
            "attack_success_probability": attack_success_probability(0.86, 0.78, 0.18),
            "residual_risk": residual_risk(90, 0.16),
        },
    ]

    evasion = threshold_evasion(0.72, -0.05, 0.70)

    with (OUT_DIR / "adversarial_risk_calculator_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["scenario", "readiness", "attack_success_probability", "residual_risk"])
        writer.writeheader()
        writer.writerows(scenarios)

    payload = {"scenarios": scenarios, "threshold_evasion_example": evasion}
    (OUT_DIR / "adversarial_risk_calculator_results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("Adversarial risk calculator complete.")
    print(OUT_DIR / "adversarial_risk_calculator_results.csv")


if __name__ == "__main__":
    main()
