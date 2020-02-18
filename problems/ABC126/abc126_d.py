from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

d = defaultdict(list)
cost = defaultdict(int)
N = int(input())

for _ in range(N-1):
    u, v, w = map(int, input().split())
    d[u].append(v)
    d[v].append(u)
    cost[(u, v)] = w

visited = [False]*(N+1)
color = [-1]*(N+1)
color[1] = 0

def dfs(x):
    visited[x]=True
    for y in d[x]:
        if visited[y]:continue
        c = cost[(x, y) if x<y else (y, x)]
        color[y] = color[x]^1 if c%2 else color[x]  
        dfs(y)

dfs(1)
print(*color[1:], sep="\n")