def coin_change(coins, coin_sum):
    dp = [0] * (coin_sum + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, coin_sum + 1):
            dp[i] += dp[i - coin]
    return dp[coin_sum]