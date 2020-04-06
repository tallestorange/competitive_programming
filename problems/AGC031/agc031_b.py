from collections import defaultdict

N = int(input())
l = [int(input()) for _ in range(N)]
dp = [0] * (N+1)
pos = defaultdict(lambda: -1)
dp[0] = 1
MOD = 10**9+7

for i in  range(1, N+1):
    p = pos[l[i-1]]
    if i-p>1 and p!=-1:
        dp[i] += dp[p]
    pos[l[i-1]] = i
    dp[i] += dp[i-1]
    dp[i] %= MOD
    
print(dp[-1])