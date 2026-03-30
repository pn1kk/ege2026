# рекурсивное решение

def alg(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return alg(x + 1, y) + alg(x + 2, y) + alg(2 * x, y)

# динамика, работает быстрее

def dp(x, y):
    dp = [0] * (y + 1)
    dp[x] = 1
    for i in range(x, y):
        if i + 1 <= y:
            dp[i + 1] += dp[i]
        if i + 2 <= y:
            dp[i + 2] += dp[i]
        if 2 * i <= y:
            dp[2 * i] += dp[i]

    return dp[y]

# из 2 в 10, содержащие 5, не содержащие 8 
print(alg(2, 5) * (alg(5, 10) -  alg(5, 8) * alg(8, 10))
print(dp(2, 5) * (dp(5, 10) - dp(5, 8) * dp(8, 10))
