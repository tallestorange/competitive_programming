import sys
sys.setrecursionlimit(1000000)

class SegTree():
    def __init__(self, l, INF):
        self.inf = INF

        N = len(l)
        v = 1
        while v<N:
            v *= 2

        self.size = v
        self.node = [self.inf] * (2*self.size-1)
        for i in range(N): # 最下段を埋める
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = min(self.node[2*i+1], self.node[2*i+2]) # 上段の更新をする

    def get(self, left, right, k=0, l=0, r=-1):
        if r < 0:
            r = self.size

        if (r <= left or right <= l):
            return self.inf
        if (left <= l and r <= right):
            return self.node[k]

        vl = self.get(left, right, 2*k+1, l, (l+r)//2)
        vr = self.get(left, right, 2*k+2, (l+r)//2, r)
        return min(vl, vr)

    def update(self, x, v):
        x += self.size-1
        self.node[x] = v

        while x>0:
            x = (x-1)//2
            self.node[x] = min(self.node[2*x+1], self.node[2*x+2])


class LCA():
    def __init__(self, N, G):
        self.depth = [0] * (N+1)
        self.euler_tour = []
        self.G = G
        self._dfs(0, 0, 0)

        self.idx = {i:-1 for i in range(1, N+1)}
        for i,j in enumerate(self.euler_tour):
            self.idx[j[1]] = i
        
        self.tree = SegTree(self.euler_tour, (2**31-1, 2**31-1))
    
    def _dfs(self, v, p, d):
        self.euler_tour.append((d, v))
        self.depth[v] = d
        for u in self.G[v]:
            if u==p:continue
            self._dfs(u, v, d+1)
            self.euler_tour.append((d, v))
    
    def get(self, u, v):
        a, b = self.idx[u], self.idx[v]
        a, b = (a, b) if a<b else (b, a)
        return self.tree.get(a, b+1)[1]


if __name__ == "__main__":
    n = int(input())
    G = {i:[] for i in range(n)}
    for i in range(n):
        k, *l = map(int, input().split())
        G[i] = l
        for j in l:
            G[j].append(i)
    lca = LCA(n, G)
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print(lca.get(u, v))