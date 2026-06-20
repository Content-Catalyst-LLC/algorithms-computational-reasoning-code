from __future__ import annotations

try:
    from .audit import brute_force_linear_program, convex_quadratic_example
except ImportError:  # Allows direct script execution.
    from audit import brute_force_linear_program, convex_quadratic_example


def main() -> None:
    lp = brute_force_linear_program()
    best = lp["best_solution"]
    print("Best two-variable LP teaching solution:")
    print(best)
    print("Convex quadratic minimum row:")
    print([row for row in convex_quadratic_example() if row["is_global_minimum"]][0])


if __name__ == "__main__":
    main()
