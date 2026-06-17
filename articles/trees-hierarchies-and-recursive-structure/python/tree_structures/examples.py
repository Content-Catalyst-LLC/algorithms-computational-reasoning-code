from __future__ import annotations

from dataclasses import dataclass
import heapq


@dataclass
class Node:
    name: str
    children: list["Node"]


def preorder(node: Node) -> list[str]:
    result = [node.name]
    for child in node.children:
        result.extend(preorder(child))
    return result


def postorder(node: Node) -> list[str]:
    result: list[str] = []
    for child in node.children:
        result.extend(postorder(child))
    result.append(node.name)
    return result


def height(node: Node) -> int:
    if not node.children:
        return 0
    return 1 + max(height(child) for child in node.children)


def leaf_names(node: Node) -> list[str]:
    if not node.children:
        return [node.name]
    names: list[str] = []
    for child in node.children:
        names.extend(leaf_names(child))
    return names


def heap_priority_demo(items: list[tuple[int, str]]) -> list[str]:
    heap = list(items)
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]


def demo_tree() -> dict[str, object]:
    root = Node(
        "root",
        [
            Node("left", [Node("left.leaf", [])]),
            Node("right", [Node("right.a", []), Node("right.b", [])]),
        ],
    )
    return {
        "preorder": preorder(root),
        "postorder": postorder(root),
        "height": height(root),
        "leaves": leaf_names(root),
        "heap_priority_order": heap_priority_demo([(3, "routine"), (1, "urgent"), (2, "soon")]),
        "interpretation": "Traversal order changes what is seen first, height describes nesting, and heaps use tree structure to retrieve priority.",
    }
