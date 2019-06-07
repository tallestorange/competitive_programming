N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    print(-1 if a==b else abs(a-b))