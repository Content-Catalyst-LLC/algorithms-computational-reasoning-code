from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv


@dataclass(frozen=True)
class Number:
    value: float


@dataclass(frozen=True)
class Add:
    left: object
    right: object


@dataclass(frozen=True)
class Multiply:
    left: object
    right: object


def evaluate_expression(node: object) -> float:
    if isinstance(node, Number):
        return node.value
    if isinstance(node, Add):
        return evaluate_expression(node.left) + evaluate_expression(node.right)
    if isinstance(node, Multiply):
        return evaluate_expression(node.left) * evaluate_expression(node.right)
    raise TypeError(f"unknown expression node: {node!r}")


def tokenize_expression(expression: str) -> list[str]:
    return expression.replace("+", " + ").replace("*", " * ").split()


def demo_interpreter(article_root: Path | None = None) -> dict[str, object]:
    tree = Add(Number(2), Multiply(Number(3), Number(4)))
    payload: dict[str, object] = {
        "expression": "2 + 3 * 4",
        "tokens": tokenize_expression("2 + 3 * 4"),
        "ast": "Add(Number(2), Multiply(Number(3), Number(4)))",
        "result": evaluate_expression(tree),
        "interpretation": "The interpreter evaluates an abstract syntax tree by recursively applying node rules.",
    }
    if article_root is not None:
        path = article_root / "data" / "synthetic_compiler_pipeline_taxonomy.csv"
        if path.exists():
            with path.open(newline="", encoding="utf-8") as handle:
                payload["pipeline_stage_count"] = len(list(csv.DictReader(handle)))
    return payload
