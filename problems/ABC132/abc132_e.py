from heapq import heappush, heappop

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


def solve():
    INF = 10**25
    N, M = map(int, input().split())
    V = {i:[] for i in range(1, 3*N+1)}
    for _ in range(M):
        u, v = map(int, input().split())
        V[u].append((1, v+(N)))
        V[u+(N)].append((1, v+(2*N)))
        V[u+(2*N)].append((1, v))

    S, T = map(int, input().split())
    dist = dijkstra1(V, 3*N, INF, S)[T]
    print(-1 if dist==INF else dist//3)


if __name__ == "__main__":
    solve()