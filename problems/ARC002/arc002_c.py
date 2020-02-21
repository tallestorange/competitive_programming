from itertools import product

N = int(input())
S = input()
c = "ABXY"

ans = 1000
for l1, l2, r1, r2 in product(c, repeat=4):
    dp = [[10**12]*2 for _ in range(N+1)]
    dp[1][0] = 1
    dp[1][1] = 1

    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1])+1
        if (S[i-1]==l1 and S[i-2]==l2) or (S[i-1]==r1 and S[i-2]==r2):
            dp[i][1] = dp[i-1][0]
    ans = min(ans, min(dp[N]))

print(ans)