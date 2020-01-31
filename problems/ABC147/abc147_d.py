N = int(input())
*A, = map(int, input().split())

d1 = [[0]*60 for _ in range(N+1)]
mod = 10**9+7

for i, n in enumerate(A, start=1):
    for j in range(60):
        d1[i][j] = d1[i-1][j] + ((n>>j)&1)

ans = 0
for i, n in enumerate(A, start=1):
    for j in range(60):
        a = d1[N][j]-d1[i][j] # 1
        if (n>>j)&1:
            a = N-a-i # 0

        ans += a*(1<<j)

print(ans%mod)
