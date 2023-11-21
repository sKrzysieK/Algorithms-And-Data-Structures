# Time Complexity (BEST | WORST | AVG): O(n * log n) | O(n * log n) | O(n * log n)
# Space Complexity : O(n)
# Stability? : YES

def merge_sort(T):
    n = len(T)
    if n <= 1:
        return

    p = n // 2
    T1 = T[0:p]
    T2 = T[p:n]
    merge_sort(T1)
    merge_sort(T2)

    i = j = k = 0

    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            T[k] = T1[i]
            i += 1
        else:
            T[k] = T2[j]
            j += 1
        k += 1

    while i < len(T1):
        T[k] = T1[i]
        i += 1
        k += 1

    while j < len(T2):
        T[k] = T2[j]
        j += 1
        k += 1

    return T