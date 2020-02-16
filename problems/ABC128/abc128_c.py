from itertools import product

N, M = map(int, input().split())
d = {}
for i in range(M):
    k, *s, = map(int, input().split())
    d[i] = s
    
*p, = map(int, input().split())

ans = 0
for k in product(range(2), repeat=N):
    a = 0
    for i, m in d.items():
        v = 0
        for j in m:
            v += k[j-1]
        if v%2 == p[i]:
            a += 1
    if a==M:
        ans += 1

print(ans)