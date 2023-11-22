# Time Complexity (BEST | WORST | AVG): O(n + k) | O(n^2) | O(n)
# Space Complexity : O(n + k)
# Stability? : YES

from quick_sort import quicker_quick_sort


def bucket_sort(T):
    n = len(T)
    buckets_num = 10
    buckets = []

    for i in range(buckets_num):
        buckets.append([])

    for element in T:
        bucket_index = int(buckets_num * element)
        buckets[bucket_index].append(element)

    for i in range(buckets_num):
        quicker_quick_sort(buckets[i], 0, len(buckets[i]) - 1)

    k = 0
    for i in range(buckets_num):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k += 1
    return T




