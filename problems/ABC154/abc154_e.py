K = input()
N = len(K)

KK = int(input())
dp = [[[0]*(5) for _ in range(2)] for _ in range(N+1)]
dp[0][0][0] = 1

for i, s in enumerate(K):
    a = ord(s)-48
    for j in range(4):
        for k in range(10):
            p = j+1 if k else j
            dp[i+1][1][p] += dp[i][1][j]
            if k<a:
                dp[i+1][1][p] += dp[i][0][j]

    for j in range(4):
        p = j+1 if a else j
        dp[i+1][0][p] += dp[i][0][j]

print(dp[N][0][KK]+dp[N][1][KK])