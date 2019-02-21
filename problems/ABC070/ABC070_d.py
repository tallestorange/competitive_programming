from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
d=defaultdict(list)

N=int(input())
for _ in range(N-1):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

Q,K=map(int,input().split())

# Kを中心とした距離を求める
dists=[None]*(N+1)
isused=[False]*(N+1)
dists[K]=0
isused[K]=True

def dfs(n):
    for i,j in d[n]:
        if isused[i]:continue
        isused[i]=True
        dists[i]=dists[n]+j
        dfs(i)

dfs(K)
for _ in range(Q):
    x,y=map(int,input().split())
    print(dists[x]+dists[y])