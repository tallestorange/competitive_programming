N, M = map(int, input().split())

l = []
for _ in range(M):
    a, b = map(int, input().split())
    c = tuple(map(int, input().split()))
    l.append((a, c))

inf = 10**12
dp = [inf]*(2**N)
dp[0] = 0

for i in range(2**N):
    for cost, j in l:
        v = sum(map(lambda x:2**(x-1), j))
        dp[i|v] = min(dp[i|v], dp[i]+cost)

print(dp[2**N-1] if dp[2**N-1]!=inf else -1)