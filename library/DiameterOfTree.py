import sys
input = sys.stdin.readline


def dfs(V, start):
    q = [(start, 0)]
    used = [False] * (n+1)
    farthest = 0
    pos = 0

    while q:
        s, cost = q.pop()
        if farthest < cost:
            pos = s
            farthest = cost
        used[s] = True
        for t, c in V[s].items():
            if used[t]:
                continue
            q.append((t, cost + c))
    
    return farthest, pos


if __name__ == "__main__":
    n = int(input())
    V = {i:dict() for i in range(n)}

    for _ in range(n - 1):
        s, t, w = map(int, input().split())
        V[s][t] = w
        V[t][s] = w

    print(dfs(V, dfs(V, 0)[1])[0])
