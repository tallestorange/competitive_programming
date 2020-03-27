from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijkstra1(V, n, inf, source):
    dist = [inf] * (n+1)
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


def solve():
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    inf = 10**15
    o = {i:[] for i in range(1, n+1)}

    for _ in range(m):
        x, y, d = map(int, input().split())
        o[x].append((d, y))
        o[y].append((d, x))

    for i in range(1, n+1):
        if i==s or i==t:continue
        dj = dijkstra1(o, n, inf, i)
        ds, dt = dj[s], dj[t]
        if ds==inf or dt==inf:continue
        if ds==dt:
            print(i)
            break
    else:
        print(-1)


if __name__ == "__main__":
    solve()