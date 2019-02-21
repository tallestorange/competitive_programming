N=int(input())
*p,=map(int,input().split())

l=[i for i,j in enumerate(p,start=1) if i==j]
n=len(l)
p=0
ans=0

if not l:
    print(0)
else:
    while p<n:
        if p<n-1:
            if l[p]+1==l[p+1]:
                p+=2
            else:
                p+=1
        else:
            p+=1
        ans+=1

    print(ans)