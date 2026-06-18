from __future__ import annotations

def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return list(values)
    mid=len(values)//2
    return merge(merge_sort(values[:mid]), merge_sort(values[mid:]))

def merge(left: list[int], right: list[int]) -> list[int]:
    out=[]; i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]

def quicksort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return list(values)
    pivot=values[len(values)//2]
    less=[x for x in values if x < pivot]
    equal=[x for x in values if x == pivot]
    greater=[x for x in values if x > pivot]
    return quicksort(less)+equal+quicksort(greater)

def binary_search(values: list[int], target: int) -> int:
    lo, hi=0, len(values)-1
    while lo <= hi:
        mid=(lo+hi)//2
        if values[mid] == target: return mid
        if values[mid] < target: lo=mid+1
        else: hi=mid-1
    return -1
