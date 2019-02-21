from itertools import permutations

N,M,R=map(int,input().split())
*r,=map(int,input().split())
inf=float("inf")
d=[[inf]*N for _ in range(N)]

for _ in range(M):
    A,B,C=map(int,input().split())
    d[A-1][B-1]=C
    d[B-1][A-1]=C

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])

ans=inf
for i in permutations(r):
    v=0
    for j in range(R-1):
        v+=d[i[j]-1][i[j+1]-1]
    ans=min(ans,v)

print(ans)