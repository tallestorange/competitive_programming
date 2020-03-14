from collections import deque

def bfs(s, t, n, V):
    q = deque([(s, 0)])
    used = [False] * (n+1)
    while q:
        a, dist = q.popleft()
        used[a] = True
        if a==t:
            break
        for b in V[a]:
            if used[b]:continue
            q.append((b, dist+1))
    if a!=t:
        return -1
    else:
        return -1 if dist%3 else dist//3


def solve():
    INF = 10**25
    N, M = map(int, input().split())
    V = {i:[] for i in range(1, 3*N+1)}
    for _ in range(M):
        u, v = map(int, input().split())
        V[u].append(v+(N))
        V[u+(N)].append(v+(2*N))
        V[u+(2*N)].append(v)

    S, T = map(int, input().split())
    dist = bfs(S, T, 3*N, V)
    print(dist)
    print(V)


if __name__ == "__main__":
    solve()