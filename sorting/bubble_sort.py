# Time Complexity (BEST | WORST | AVG): O(n) | O(n^2) | O(n^2)
# Space Complexity : O(1)
# Stability? : YES

def bubble_sort(T):
    length = len(T)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                swapped = True
        if not swapped:
            break
