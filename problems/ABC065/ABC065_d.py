class UnionFind(object):
  def __init__(self,n):
    self.parent={i:i for i in range(1,n+1)}
    self.size={i:1 for i in range(1,n+1)}
  def find(self,a):
    if self.parent[a]!=a:
      self.parent[a]=self.find(self.parent[a])
    return self.parent[a]
  def unite(self,a,b):
    a=self.find(a)
    b=self.find(b)
    if a==b:return
    if self.size[a]>self.size[b]:
      self.size[a]+=self.size[b]
      self.parent[b]=a
    else:
      self.size[b]+=self.size[a]
      self.parent[a]=b
  def isunited(self,a,b):
    return self.find(a)==self.find(b)

# 方針
# 最小全域木じゃん！おしまい！

N=int(input())
l=[[i+1]+list(map(int,input().split())) for i in range(N)]
o=[]

l.sort(key=lambda x:x[1]) # xでソート
for i in range(N-1):
    o.append((l[i][0],l[i+1][0],l[i+1][1]-l[i][1]))

l.sort(key=lambda x:x[2]) # yでソート
for i in range(N-1):
    o.append((l[i][0],l[i+1][0],l[i+1][2]-l[i][2]))

o.sort(key=lambda x:x[2])

ans=0
uft=UnionFind(N)
for town1,town2,cost in o:
    if not uft.isunited(town1,town2):
        uft.unite(town1,town2)
        ans+=cost

print(ans)