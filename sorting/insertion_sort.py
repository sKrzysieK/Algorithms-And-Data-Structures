# Time Complexity (BEST | WORST | AVG): O(n) | O(n^2) | O(n^2)
# Space Complexity : O(1)
# Stability? : YES

def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        curr = i - 1

        while curr >= 0 and key < T[curr]:
            T[curr + 1] = T[curr]
            curr -= 1

        T[curr + 1] = key
    return T