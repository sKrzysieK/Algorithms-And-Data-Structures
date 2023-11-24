def lis(T):
    n = len(T)
    F = [-1] * n
    P = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if T[i] > T[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    return max(F), F.index(max(F)), P


def print_seq(T, P, i):
    if P[i] != -1:
        print_seq(T, P, P[i])
    print(T[i])