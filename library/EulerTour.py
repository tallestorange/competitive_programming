from collections import defaultdict, deque, Counter

G = defaultdict(list)

def euler_tour(G, N, root):
    euler = []
    q, q2 = [(root, 0)], []
    visited = [0] * (N+1)
    depth = {}
    idx = {}
    cnt = 0

    while q:
        u, d = q.pop()
        euler += [(u, d)]
        idx[u] = cnt
        cnt += 1
        depth[u] = d

        if visited[u]:
            continue
        for v in G[u]:
            if visited[v]:
                q += [(v, depth[v])]
            else:
                q2 += [(v, d+1)]
   
        q.extend(q2)
        q2 = []
        visited[u] = 1
    return euler, idx


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
    
    et, idx = euler_tour(G, 5, 1)