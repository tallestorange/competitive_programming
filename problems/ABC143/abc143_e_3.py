import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
inf = 10**15
V = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, input().split())
    if C>L:continue
    V[A-1].append((B-1, C))
    V[B-1].append((A-1, C))

dists = []
for i in range(N):
    dist = [(inf,inf)] * N
    dist[i] = (0, 0)
    u = [False] * N
    for _ in range(N):
        (charged, used), j = min([(dist[i], i) for i in range(N) if not u[i]])
        u[j] = True
        for k, next_cost in V[j]:
            if j==k: continue
            c = (charged+1, next_cost) if used+next_cost>L else (charged, used+next_cost)
            if dist[k] > c:
                dist[k] = c
    dists.append(dist)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    ans = dists[s-1][t-1][0]
    print(ans if ans!=inf else -1)
