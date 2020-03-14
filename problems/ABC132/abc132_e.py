from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
V = {i:[] for i in range(N)}

for _ in range(M):
    u, v = map(int, input().split())
    V[u-1].append((1, v-1))

S, T = map(int, input().split())


def dijkstra1(V, source):
    # O(ElogV)

    n = len(V)
    inf = float("inf")
    dist = [inf] * n
    dist[source] = 0
    q = [(0, source)]

    while q:
        cost, u = heappop(q)
        if dist[u] < cost:
            continue
        for c, v in V[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                heappush(q, (dist[v], v))

    return dist

a = dijkstra1(V, S-1)
b = dijkstra1(V, T-1)

st, ts = a[T-1], b[S-1]

if st==0 and ts==0:
    print(-1)
elif (st+ts)%3==0 and st%3:
    print(-1)
else:
    p = 0
    while 1:
        v = (st+ts)*p+st
        if v%3==0:
            print(v//3)
            break
        p += 1