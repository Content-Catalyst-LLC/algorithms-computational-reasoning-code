def objective(x: float) -> float:
    return (x - 2.0) ** 2 + 1.0


def finite_grid(start=-3, stop=5, step=1):
    x = start
    rows = []
    while x <= stop:
        rows.append({"x": x, "objective": objective(x)})
        x += step
    return rows


if __name__ == "__main__":
    rows = finite_grid()
    print(min(rows, key=lambda row: row["objective"]))
