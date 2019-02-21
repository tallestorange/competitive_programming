H,W=map(int,input().split())
N=int(input())
*a,=map(int,input().split())

ans=[[0]*W for _ in range(H)]
x,y,d=0,0,1

for (i,j) in enumerate(a,start=1):
    for k in range(j):
        ans[y][x]=i
        
        y+=d
        if not 0<=y<H:
            y-=d
            x+=1
            d*=-1

for i in ans:
    print(*i)
