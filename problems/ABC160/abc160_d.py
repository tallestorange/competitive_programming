from collections import defaultdict
import sys
input=sys.stdin.readline


def solve():
    N, X, Y = map(int, input().split())
    d = defaultdict(list)
    for i in range(1, N):
        d[i].append(i+1)
        d[i+1].append(i)
    d[X].append(Y)
    d[Y].append(X)
    ans = [0]*N

    for i in range(1, N+1):
        dist = [-1]*(N+1)
        dist[i] = 0
        q = [i]

        while q:
            s = q.pop()
            for t in d[s]:
                if dist[t]==-1 or dist[t] > dist[s]+1:
                    dist[t] = dist[s]+1
                    q.append(t)
        for j in range(i+1, N+1):
            ans[dist[j]] += 1

    for i in range(1, N):
        print(ans[i])


if __name__ == "__main__":
    solve()
