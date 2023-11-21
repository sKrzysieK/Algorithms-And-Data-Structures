# Time Complexity (BEST | WORST | AVG): O(n * log n) | O(n * log n) | O(n^2)
# Space Complexity : O(n * log n)
# Stability? : NO

from util.partiton import randomized_partition


# with tail recursion
def quick_sort(T, p, r):
    if p < r:
        q = randomized_partition(T, p, r)
        quick_sort(T, p, q - 1)
        quick_sort(T, q + 1, r)


# without tail recursion
def quicker_quick_sort(T, p, r):
    while p < r:
        q = randomized_partition(T, p, r)
        quick_sort(T, p, q - 1)
        p = q + 1
