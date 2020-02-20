from heapq import heappop, heappush

def dijkstra(g, source):
    n = len(g)
    dist = [inf] * n
    dist[source] = 0
    q = [(0, source)]

    while q:
        cost, u = heappop(q)
        for c, v in V[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                heappush(q, (dist[v], v))

    return dist


if __name__ == "__main__":
    n = int(input())
    V = [[] for _ in range(n)]
    inf = float("inf")

    for _ in range(n):
        u, k, *vc = map(int, input().split())
        for i in range(0, 2*k, 2):
            v, c = vc[i], vc[i+1]
            V[u].append((c, v))

    d = dijkstra(V, 0)
    for i, j in enumerate(d):
        print(i, j)