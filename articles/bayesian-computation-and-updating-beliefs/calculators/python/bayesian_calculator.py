from __future__ import annotations
import argparse, json, math
from pathlib import Path

def beta_mean(alpha: float, beta: float) -> float:
    return alpha / (alpha + beta)

def beta_variance(alpha: float, beta: float) -> float:
    return (alpha * beta) / (((alpha + beta) ** 2) * (alpha + beta + 1.0))

def beta_pdf_unnormalized(x: float, alpha: float, beta: float) -> float:
    if x <= 0.0 or x >= 1.0: return 0.0
    return (x ** (alpha - 1.0)) * ((1.0 - x) ** (beta - 1.0))

def beta_cdf(x: float, alpha: float, beta: float, grid_size: int = 5000) -> float:
    if x <= 0.0: return 0.0
    if x >= 1.0: return 1.0
    step = 1.0 / grid_size
    total = partial = 0.0
    for i in range(1, grid_size + 1):
        midpoint = (i - 0.5) * step
        density = beta_pdf_unnormalized(midpoint, alpha, beta)
        total += density
        if midpoint <= x: partial += density
    return 0.0 if total == 0.0 else partial / total

def beta_quantile(q: float, alpha: float, beta: float) -> float:
    lo, hi = 0.0, 1.0
    for _ in range(50):
        mid = (lo + hi) / 2.0
        if beta_cdf(mid, alpha, beta) < q: lo = mid
        else: hi = mid
    return (lo + hi) / 2.0

def calculate(alpha: float, beta: float, successes: int, failures: int, threshold: float) -> dict[str, float]:
    post_alpha = alpha + successes
    post_beta = beta + failures
    variance = beta_variance(post_alpha, post_beta)
    return {"prior_alpha": alpha, "prior_beta": beta, "successes": successes, "failures": failures, "posterior_alpha": post_alpha, "posterior_beta": post_beta, "posterior_mean": beta_mean(post_alpha, post_beta), "posterior_sd": math.sqrt(variance), "credible_interval_90_lower": beta_quantile(0.05, post_alpha, post_beta), "credible_interval_90_upper": beta_quantile(0.95, post_alpha, post_beta), "threshold": threshold, "probability_above_threshold": 1.0 - beta_cdf(threshold, post_alpha, post_beta)}

def main() -> None:
    parser = argparse.ArgumentParser(description="Beta-binomial Bayesian updating calculator.")
    parser.add_argument("--alpha", type=float, default=2.0)
    parser.add_argument("--beta", type=float, default=2.0)
    parser.add_argument("--successes", type=int, default=113)
    parser.add_argument("--failures", type=int, default=72)
    parser.add_argument("--threshold", type=float, default=0.60)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "outputs" / "bayesian_calculator_output.json")
    args = parser.parse_args()
    payload = calculate(args.alpha, args.beta, args.successes, args.failures, args.threshold)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
if __name__ == "__main__": main()
