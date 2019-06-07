s=set()
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    s.add((a,b) if a>b else (b,a))
print(len(s))