from heapq import heappush, heappop
from collections import defaultdict

N, M, L = map(int, input().split())
inf = 10**20
c = [[inf]*N for _ in range(N)]
d = defaultdict(list)

for i in range(N):
    for j in range(N):
        if i==j:
            c[i][j]=0

for _ in range(M):
    A, B, C = map(int, input().split())
    c[A-1][B-1] = C
    c[B-1][A-1] = C
    d[A-1].append(B-1)
    d[B-1].append(A-1)

Q = int(input())
l = [tuple(map(int, input().split())) for _ in range(Q)]
charged_dict = [[inf]*N for _ in range(N)]

for j in range(N):
    q = []
    heappush(q, (0, -L, 0, j))
    while q:
        charged, fuel, cost, pos = heappop(q)

        if charged_dict[j][pos] < charged:
            continue

        charged_dict[j][pos] = charged

        for i in d[pos]:
            next_cost = c[pos][i]
            if -fuel-next_cost<0:
                heappush(q, (charged+1, -(L-next_cost), next_cost+cost, i))
            else:
                heappush(q, (charged, -(-fuel-next_cost), next_cost+cost, i))

for s, t in l:
    ans = charged_dict[s-1][t-1]
    print(ans if ans!=inf else -1)
