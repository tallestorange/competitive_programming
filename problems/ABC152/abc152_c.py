N = int(input())
*P, = map(int, input().split())

m = P[0]
ans = 0

for p in P:
    m = min(m, p)
    if p <= m:
        ans += 1

print(ans)