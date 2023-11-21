from math import log2


def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2
def heap_height(T): return int(log2(len(T)) + 1)


def extract_max(T):
    n = len(T)
    if n < 1:
        return None
    max_val = T[0]
    T[0] = T[n - 1]
    T.pop()
    heapify(T, 0, n - 1)
    return max_val


def insert(T, element):
    T.append(element)
    n = len(T)
    i = n - 1
    while i > 0 and T[parent(i)] < element:
        T[i] = T[parent(i)]
        i = parent(i)
    T[i] = element


def heapify(T, i, n):
    l = left(i)
    r = right(i)
    max_index = i
    if l < n and T[l] > T[max_index]:
        max_index = l
    if r < n and T[r] > T[max_index]:
        max_index = r
    if max_index != i:
        T[i], T[max_index] = T[max_index], T[i]
        heapify(T, max_index, n)


def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, i, n)