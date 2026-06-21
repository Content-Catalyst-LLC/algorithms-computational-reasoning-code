from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def f(x: float) -> float:
    return math.sin(x) + 0.25 * x * x


def finite_difference(x: float, h: float, method: str = "central") -> float:
    if method == "forward":
        return (f(x + h) - f(x)) / h
    if method == "central":
        return (f(x + h) - f(x - h)) / (2 * h)
    raise ValueError("method must be forward or central")


def trapezoid(a: float, b: float, n: int) -> float:
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def bisection_root(a: float, b: float, tol: float = 1e-8) -> float:
    def g(x: float) -> float:
        return x * x - 2.0
    fa = g(a)
    fb = g(b)
    if fa * fb > 0:
        raise ValueError("Root is not bracketed")
    while 0.5 * abs(b - a) > tol:
        m = 0.5 * (a + b)
        fm = g(m)
        if fa * fm <= 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    return 0.5 * (a + b)


def euler_growth(y0: float, rate: float, t_end: float, h: float) -> float:
    y = y0
    t = 0.0
    while t < t_end - 1e-12:
        y += h * rate * y
        t += h
    return y


def main() -> None:
    parser = argparse.ArgumentParser(description="Numerical approximation calculators")
    parser.add_argument("--x", type=float, default=1.0)
    parser.add_argument("--h", type=float, default=0.01)
    parser.add_argument("--n", type=int, default=100)
    args = parser.parse_args()
    payload = {
        "finite_difference_central": finite_difference(args.x, args.h, "central"),
        "finite_difference_forward": finite_difference(args.x, args.h, "forward"),
        "trapezoid_0_pi": trapezoid(0.0, math.pi, args.n),
        "bisection_sqrt2": bisection_root(1.0, 2.0),
        "euler_growth": euler_growth(1.0, 0.3, 5.0, 0.1),
    }
    (OUT / "python_calculator_results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
