H, N = map(int, input().split())
a, b = zip(*(list(map(int, input().split())) for _ in range(N)))
maxA = max(a)

inf = float("inf")
dp = [inf] * (H+maxA+1)
dp[0] = 0

for j in range(N):
    for i in range(a[j], H+maxA+1):
        dp[i] = min(dp[i], dp[i-a[j]]+b[j])

print(min(dp[H:]))