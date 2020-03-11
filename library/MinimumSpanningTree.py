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


V, E = map(int, input().split())
uft = UnionFind(V)
l = [tuple(map(int, input().split())) for _ in range(E)]
l.sort(key=lambda x:x[2])

ans = 0
for s, t, w in l:
    s += 1; t += 1
    if not uft.isunited(s, t):
        ans += w
        uft.unite(s, t)

print(ans)