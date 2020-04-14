import sys
input=sys.stdin.readline


class UnionFind(object):
    def __init__(self, n):
        self.parent={i:i for i in range(1,n+1)}
        self.size={i:1 for i in range(1,n+1)}
    def find(self, a):
        if self.parent[a]!=a:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]
    def getsize(self, a):
        return self.size[self.find(a)]
    def unite(self, a, b):
        a=self.find(a)
        b=self.find(b)
        if a==b:return
        if self.size[a]>self.size[b]:
            self.size[a]+=self.size[b]
            self.parent[b]=a
        else:
            self.size[b]+=self.size[a]
            self.parent[a]=b
    def isunited(self, a, b):
        return self.find(a)==self.find(b)


def solve():
    N, M, K = map(int, input().split())
    uft = UnionFind(N)
    d = {i:set() for i in range(1, N+1)}
    e = {i:0 for i in range(1, N+1)}
    f = {i:0 for i in range(1, N+1)}

    for _ in range(M):
        A, B = map(int, input().split())
        d[A].add(B)
        d[B].add(A)
        f[A] += 1
        f[B] += 1
        uft.unite(A, B)

    for _ in range(K):
        C, D = map(int, input().split())
        if uft.isunited(C, D):
            if D not in d[C]:
                e[C] += 1
            if C not in d[D]:
                e[D] += 1
    
    g = lambda x:uft.getsize(x)-e[x]-f[x]-1
    print(*map(g, range(1, N+1)))


if __name__ == "__main__":
    solve()
