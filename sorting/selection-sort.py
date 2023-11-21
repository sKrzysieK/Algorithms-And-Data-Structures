# Time Complexity (BEST | WORST | AVG): O(n^2) | O(n^2) | O(n^2)
# Space Complexity : O(1)
# Stability? : NO

def selection_sort(T):
    n = len(T)
    for i in range(n):
        target_index = i

        for j in range(i + 1, n):
            if T[target_index] > T[j]:
                target_index = j
        T[i], T[target_index] = T[target_index], T[i]
    return T