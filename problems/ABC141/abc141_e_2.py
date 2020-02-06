N = int(input())
S = input()
dp = [[0]*(N+1) for _ in range(N+1)]

for l in range(N)[::-1]:
    for r in range(l+1, N)[::-1]:
        dp[l][r] = dp[l+1][r+1]+1 if S[l]==S[r] else 0

ans = 0 
for l in range(N)[::-1]:
    for r in range(l+1, N)[::-1]:
        ans = max(ans, min(r-l, dp[l][r]))
print(ans)