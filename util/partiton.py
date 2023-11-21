from random import randint


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def randomized_partition(T, p, r):
    rand_num = randint(p, r)
    T[r], T[rand_num] = T[rand_num], T[r]
    return partition(T, p, r)