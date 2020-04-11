from collections import defaultdict
import sys
input=sys.stdin.readline


def get_dist(s, d, N):
    dist = [-1]*(N+1)
    dist[s] = 0
    q = [s]
    while q:
        a = q.pop()
        for b in d[a]:
            if dist[b]!=-1:
                continue
            dist[b] = dist[a] + 1
            q.append(b)
    return dist


def solve():
    N, u, v = map(int, input().split())
    d = defaultdict(list)
    for _ in range(N-1):
        A, B = map(int, input().split())
        d[A].append(B)
        d[B].append(A)
    du, dv = get_dist(u, d, N), get_dist(v, d, N)
    ds = [(i, j) for i, j in zip(du, dv) if i<j]
    ds.sort(key=lambda x:-x[1])
    print(ds[0][1]-1)


if __name__ == "__main__":
    solve()
