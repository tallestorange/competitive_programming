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

N, M = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(M)]
ans = []
uft = UnionFind(N)

c = 0
ans.append(N*(N-1)//2)
for a, b in l[1:][::-1]:
    if not uft.isunited(a, b):
        ba, bb = uft.getsize(a), uft.getsize(b)
        pa, pb = ba*(ba-1)//2, bb*(bb-1)//2
        
        uft.unite(a, b)

        bc = uft.getsize(a)
        pc = bc*(bc-1)//2
        c += pc - pa - pb
    ans.append(N*(N-1)//2-c)

for i in ans[::-1]:
    print(i)