# Time Complexity (BEST | WORST | AVG): O(n + k) | O(n + k) | O(n + k)
# Space Complexity : O(max)
# Stability? : YES

def custom_counting_sort(array, place):
    n = len(array)
    output = [0] * n
    C = [0] * 10

    # Calculate count of elements
    for i in range(n):
        index = array[i] // place
        C[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        C[i] += C[i - 1]

    # Place the elements in sorted order
    i = n - 1
    while i >= 0:
        index = array[i] // place
        output[C[index % 10] - 1] = array[i]
        C[index % 10] -= 1
        i -= 1

    for i in range(0, n):
        array[i] = output[i]


def radix_sort(T):
    maxT = max(T)
    place = 1
    while maxT // place > 0:
        custom_counting_sort(T, place)
        place *= 10

