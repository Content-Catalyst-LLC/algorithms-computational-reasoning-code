from itertools import product


def solve_two_variable_integer_lp(labor_limit=8, material_limit=8):
    candidates = []
    for x, y in product(range(0, 10), range(0, 10)):
        labor = 2 * x + y
        material = x + 2 * y
        if labor <= labor_limit and material <= material_limit:
            candidates.append({
                "x": x,
                "y": y,
                "objective": 3 * x + 4 * y,
                "labor_used": labor,
                "material_used": material,
                "labor_slack": labor_limit - labor,
                "material_slack": material_limit - material,
            })
    return max(candidates, key=lambda row: row["objective"])


if __name__ == "__main__":
    print(solve_two_variable_integer_lp())
