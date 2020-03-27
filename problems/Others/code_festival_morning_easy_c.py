n, m = map(int, input().split())
s, t = map(int, input().split())
inf = float("inf")
o = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, d = map(int, input().split())
    o[x][y] = d
    o[y][x] = d

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            o[i][j] = min(o[i][j], o[i][k]+o[k][j])

for i in range(1, n+1):
    if s==i or i==t:continue
    if o[s][i]==o[i][t] and o[s][i]!=inf and o[s][i]!=inf:
        print(i)
        break
else:
    print(-1)
