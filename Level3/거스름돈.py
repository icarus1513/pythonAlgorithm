def solution(n, money):
    answer = 0
    dp = [0] * 100001
    dp[0] = 1
    for i in money:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    answer = dp[n]
    return answer