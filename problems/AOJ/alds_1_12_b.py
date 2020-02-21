from heapq import heappop, heappush
from collections import defaultdict
V = defaultdict(list)

n = int(input())
inf = float("inf")
cost = [[inf]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            cost[i][j] = 0

for _ in range(n):
    u, k, *l = map(int, input().split())
    for i in range(0, 2*k, 2):
        v, c = l[i], l[i+1]
        V[u].append(v)
        V[v].append(u)
        cost[u][v] = c
        cost[v][u] = c

for i in range(n):

    q = []
    d = [inf]*n
    d[0] = 0

    heappush(q, (0, 0))
    while q:
        c, pos = heappop(q)
        if d[pos] < c:
            continue
        for p in V[pos]:
            if d[p] > d[pos] + cost[pos][p]:
                d[p] = d[pos] + cost[pos][p]
                heappush(q, (d[p], p))

    print(i, d[i])