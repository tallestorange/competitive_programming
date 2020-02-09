S = input()
mod = 10**9+7
dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1

for i, s in enumerate(S[::-1], start=1):
    m = pow(10, i-1, 13)
    if s=="?":
        for j in range(10):
            for k in range(13):
                dp[i][(j*m+k)%13] += dp[i-1][k]
    else:
        j = int(s)
        for k in range(13):
            dp[i][(j*m+k)%13] += dp[i-1][k]
    
    for j in range(13):
        dp[i][j] %= mod

print(dp[-1][5])