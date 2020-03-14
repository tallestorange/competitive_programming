from collections import deque


def solve():
    N, M = map(int, input().split())
    V = {i:[] for i in range(1, N+1)}
    for _ in range(M):
        u, v = map(int, input().split())
        V[u].append(v)

    S, T = map(int, input().split())
    q = deque([(S, 0)])
    used = [[False]*3 for _ in range(N+1)]
    while q:
        a, dist = q.popleft()
        used[a][dist%3] = True
        if a==T and dist%3==0:
            break
        for b in V[a]:
            if used[b][(dist+1)%3]:continue
            q.append((b, dist+1))

    if a==T and dist%3==0:
        print(dist//3)
    else:
        print(-1)

if __name__ == "__main__":
    solve()