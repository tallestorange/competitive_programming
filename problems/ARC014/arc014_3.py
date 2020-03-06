from collections import deque

N = int(input())
S = input()
dp = [[[] for _ in range(N+1)] for _ in range(N+1)]

for l in range(N+1):
    for r in range(N+1):
        if l==0 and r==0:continue
        if not l+r-1<N:continue
        a, b = [], []

        if dp[l-1][r]:
            a = dp[l-1][r][1:] if dp[l-1][r][0] == S[l+r-1] else [S[l+r-1]]+dp[l-1][r]
        else:
            a = [S[l+r-1]]
        
        if dp[l][r-1]:
            b = dp[l][r-1][:-1] if dp[l][r-1][-1] == S[l+r-1] else dp[l][r-1]+[S[l+r-1]]
        else:
            b = [S[l+r-1]]

        if len(a) > len(b):
            dp[l][r] = b if r else b
        else:
            dp[l][r] = a if l else b

ans = N
for l in range(N+1):
    for r in range(N+1):
        if l==0 and r==0:continue
        if not l+r==N:continue
        ans = min(ans, len(dp[l][r]))

print(ans)