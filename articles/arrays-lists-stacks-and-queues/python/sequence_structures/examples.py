from __future__ import annotations

from collections import deque


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.data: list[str | None] = [None] * capacity
        self.head = 0
        self.size = 0

    def append(self, value: str) -> None:
        index = (self.head + self.size) % self.capacity
        if self.size == self.capacity:
            self.data[self.head] = value
            self.head = (self.head + 1) % self.capacity
        else:
            self.data[index] = value
            self.size += 1

    def values(self) -> list[str]:
        return [self.data[(self.head + i) % self.capacity] for i in range(self.size) if self.data[(self.head + i) % self.capacity] is not None]


def stack_order(items: list[str]) -> list[str]:
    stack: list[str] = []
    for item in items:
        stack.append(item)
    return [stack.pop() for _ in range(len(stack))]


def queue_order(items: list[str]) -> list[str]:
    q = deque(items)
    return [q.popleft() for _ in range(len(q))]


def array_index_demo(items: list[str], index: int) -> str:
    return items[index]


def demo_sequence_structures() -> dict[str, object]:
    buffer = CircularBuffer(3)
    for item in ["a", "b", "c", "d"]:
        buffer.append(item)
    return {
        "array_index_demo": array_index_demo(["zero", "one", "two"], 1),
        "stack_order": stack_order(["first", "second", "third"]),
        "queue_order": queue_order(["first", "second", "third"]),
        "circular_buffer_values_after_overwrite": buffer.values(),
        "interpretation": "Arrays emphasize index, lists emphasize sequence, stacks emphasize recency, queues emphasize service order, and circular buffers emphasize bounded recent history.",
    }
