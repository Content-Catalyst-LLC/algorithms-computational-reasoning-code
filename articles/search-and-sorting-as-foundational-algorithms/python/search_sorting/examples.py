from __future__ import annotations
from collections import deque

def linear_search(values: list[int], target: int) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search(values: list[int], target: int) -> int:
    low, high = 0, len(values)-1
    while low <= high:
        mid=(low+high)//2
        if values[mid] == target: return mid
        if values[mid] < target: low=mid+1
        else: high=mid-1
    return -1

def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return list(values)
    mid=len(values)//2
    left=merge_sort(values[:mid]); right=merge_sort(values[mid:])
    out=[]
    while left and right:
        out.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return out + left + right

def bfs_reachable(graph: dict[str, list[str]], start: str) -> list[str]:
    seen={start}; q=deque([start]); order=[]
    while q:
        node=q.popleft(); order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)
    return order
