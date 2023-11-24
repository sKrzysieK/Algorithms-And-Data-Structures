def factorial(n):
    F = [1] * (n + 1)
    F[2] = 2
    for i in range(2, n + 1):
        F[i] = F[i - 1] * i
    return F[n]