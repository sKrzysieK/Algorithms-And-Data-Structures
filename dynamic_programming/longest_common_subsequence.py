def lcs(T1, T2):
    inf = float("inf")
    n = len(T1)
    m = len(T2)
    dp = [ [ -1 for _ in range(m + 1) ] for _ in range(n + 1) ]

    for i in range(n):
        dp[i][0] = 0

    for i in range(m):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if T1[i - 1] == T2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = n
    j = m
    lcs = ""
    while i > 0 and j > 0:
        if T1[i - 1] == T2[j - 1]:
            lcs += str(T1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = lcs[::-1]
    print("LCS: ", lcs)

    return dp[n][m]