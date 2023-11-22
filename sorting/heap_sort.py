# Time Complexity (BEST | WORST | AVG): O(nlog n) | O(nlog n) | O(nlog n)
# Space Complexity : O(1)
# Stability? : No

from sorting.util.heap import build_heap, heapify


def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)
    return T
