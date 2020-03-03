from collections import defaultdict

euler_tour = []
n = 5
depth = [0]*(n+1)
G = defaultdict(list)

def dfs(v, p, d):
    euler_tour.append(v)
    depth[v] = d
    for u in G[v]:
        if u==p:continue
        dfs(u, v, d+1)
        euler_tour.append(v)

def lca(u, v):
    # O(n)
    a, b = euler_tour.index(u), euler_tour.index(v)
    a, b = (a, b) if a<b else (b, a)
    cost = 10**20
    ans = 0

    for i in range(a, b+1):
        p = euler_tour[i]
        d = depth[p]
        if cost > d:
            ans = p
            cost = d
    
    return ans


if __name__ == "__main__":
    l = [
        (1, 2),
        (1, 3),
        (2, 4),
        (2, 5)
    ]

    for u, v in l:
        G[u].append(v)
        G[v].append(u)
    
    dfs(1, 0, 0)

    idx = {i:-1 for i in range(1, n+1)}
    for i,j in enumerate(euler_tour):
        idx[j] = i
    
    r = [depth[i] for i in euler_tour]