from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def dijkstra1(V, n, inf, source):
    # O(ElogV)

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

def dijkstra2(V, n, inf, source):
    # O(V^2)

    used = [False] * (n+1)
    dist = [inf] * (n+1)
    dist[0] = 0
    
    for _ in range(n):
        c1, u = min([(dist[i], i) for i in range(n) if not used[i]])
        used[u] = True
        for c2, v in V[u]:
            if v==u: continue
            dist[v] = min(dist[v], c1+c2)
    return dist


if __name__ == "__main__":
    V, E, r = map(int, input().split())
    inf = float("inf")
    costs = {i:[] for i in range(V)}
    
    for _ in range(E):
        s, t, d = map(int, input().split())
        costs[s].append((d, t))

    for i in dijkstra1(costs, r):
        print(i if i!=inf else "INF")