from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
inf = 10**20
d = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    d[A-1].append((B-1, C))
    d[B-1].append((A-1, C))

charged_dict = [[(inf,inf)]*N for _ in range(N)]
for j in range(N):
    charged_dict[j][j] = (0, 0)
    q = [(0, 0, j)]
    while q:
        charged, used, u = heappop(q)
        for v, next_cost in d[u]:
            c = (charged+1, next_cost) if used+next_cost>L else (charged, used+next_cost)
            if charged_dict[j][v] > c:
                charged_dict[j][v] = c
                heappush(q, c+(v,))

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    ans = charged_dict[s-1][t-1][0]
    print(ans if ans!=inf else -1)