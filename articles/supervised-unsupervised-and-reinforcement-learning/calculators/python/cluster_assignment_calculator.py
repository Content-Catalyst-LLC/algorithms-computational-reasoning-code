from __future__ import annotations
import argparse
import math


def main() -> None:
    parser = argparse.ArgumentParser(description="Assign a point to the nearest of three default centroids.")
    parser.add_argument("--x", type=float, required=True)
    parser.add_argument("--y", type=float, required=True)
    args = parser.parse_args()
    centers = [(0.20, 0.75), (0.65, 0.55), (0.55, 0.20)]
    distances = [(math.sqrt((args.x - cx) ** 2 + (args.y - cy) ** 2), idx) for idx, (cx, cy) in enumerate(centers)]
    distance, cluster = min(distances)
    print(f"cluster={cluster}")
    print(f"distance={distance:.6f}")


if __name__ == "__main__":
    main()
