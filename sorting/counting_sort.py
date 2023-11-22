# Time Complexity (BEST | WORST | AVG): O(n  + k) | O(n  + k) | O(n + k)
# Space Complexity : O(max)
# Stability? : YES

def counting_sort(T, k):
    n = len(T)
    C = [0] * k
    output = [0] * n

    for i in range(n):
        C[T[i]] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        output[ C[ T[i] ] - 1 ] = T[i]
        C[ T[i] ] -= 1

    return output