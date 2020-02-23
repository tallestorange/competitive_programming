K = input()
N = len(K)

dp = [[[0]*(2) for _ in range(2)] for _ in range(N+1)]
dp[0][0][1] = 1

for i, s in enumerate(K):
    a = ord(s)-48

    # 0 -> 1 1-> other

    for k in range(10):
        if k == 1:
            dp[i+1][1][0] += dp[i][1][1]
            if k<a:
                dp[i+1][1][0] += dp[i][0][1]
        else:
            dp[i+1][1][1] += dp[i][1][0]
            if k<a:
                dp[i+1][1][1] += dp[i][0][0]

        

    dp[i+1][0][a==1] += dp[i][0][a!=1]
    # dp[i+1][0][a] += dp[i][0][a]

# print(dp[N][0][KK]+dp[N][1][KK])