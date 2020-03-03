import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline


class SegTree():
    def __init__(self, l, INF):
        self.inf = INF

        N = len(l)
        self.size = N
        self.node = [self.inf] * (2*self.size-1)
        for i in range(N): # 最下段を埋める
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = min(self.node[2*i+1], self.node[2*i+2]) # 上段の更新をする
    
    def update(self, k, x):
        k += self.size-1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = min(self.node[2*k+1], self.node[2*k+2])

    def get(self, l, r):
        x = self.inf
        l += self.size
        r += self.size

        while l<r:
            if l&1:
                x = min(x, self.node[l-1])
                l += 1
            if r&1:
                r -= 1
                x = min(x, self.node[r-1])
            l >>= 1
            r >>= 1
        return x


class LCA():
    def __init__(self, N, G):
        self.depth = {}
        self.tour = []    
        self.idx = {}
        self.tree = SegTree(self.euler_tour(G, N, 1), (2**31-1, 2**31-1))

    def euler_tour(self, G, N, root):
        q, q2 = [(root, 0)], []
        visited = [0] * (N+1)
        cnt = 0
        et = []

        while q:
            u, d = q.pop()
            et += [(d, u)]
            self.idx[u] = cnt
            cnt += 1
            self.depth[u] = d

            if visited[u]:
                continue
            for v in G[u]:
                if visited[v]:
                    q += [(v, self.depth[v])]
                else:
                    q2 += [(v, d+1)]
    
            q.extend(q2)
            q2 = []
            visited[u] = 1
        return et
    
    def get(self, u, v):
        a, b = self.idx[u], self.idx[v]
        a, b = (a, b) if a<b else (b, a)
        return self.tree.get(a, b+1)[1]


if __name__ == "__main__":
    N = int(input())
    G = {i:[] for i in range(1, N+1)}
    for _ in range(N-1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    
    lca = LCA(N, G)
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        c = lca.get(a, b)
        ans = lca.depth[a]+lca.depth[b]-2*lca.depth[c]+1
        print(ans)