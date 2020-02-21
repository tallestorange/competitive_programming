from heapq import heappop, heappush

def dijkstra1(g, source):
    # O(ElogV)

    n = len(g)
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

def dijkstra2(g, source):
    # O(V^2)

    n = len(V)
    inf = float("inf")
    used = [False] * n
    dist = [inf] * n
    dist[0] = 0
    
    for _ in range(n):
        c1, u = min([(dist[i], i) for i in range(n) if not used[i]])
        used[u] = True
        for c2, v in V[u]:
            if v==u: continue
            dist[v] = min(dist[v], c1+c2)
    return dist


if __name__ == "__main__":
    n = int(input())
    V = [[] for _ in range(n)]

    for _ in range(n):
        u, k, *vc = map(int, input().split())
        for i in range(0, 2*k, 2):
            v, c = vc[i], vc[i+1]
            V[u].append((c, v))

    d = dijkstra2(V, 0)
    for i, j in enumerate(d):
        print(i, j)
