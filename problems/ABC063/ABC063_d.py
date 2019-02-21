from math import ceil

N,A,B=map(int,input().split())
h=[int(input()) for _ in range(N)]

def f(k):
    g=lambda x:ceil((x-B*k)/(A-B))
    return(sum(filter(lambda x:x>0,map(g,h)))<=k)

l,r=0,ceil(max(h)/B)

while r-l>1:
    if f((l+r)//2):
        r=(l+r)//2
    else:
        l=(l+r)//2

print(r)