# Time Complexity (BEST | WORST | AVG): O(n^2) | O(n^2) | O(n^2)
# Space Complexity : O(1)
# Stability? : NO

def selection_sort(T):
    length = len(T)
    for i in range(length):
        target_index = i

        for j in range(i + 1, length):
            if T[target_index] > T[j]:
                target_index = j
        T[i], T[target_index] = T[target_index], T[i]