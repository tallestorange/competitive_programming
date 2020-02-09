N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())

bef = sum(A)
for i, n in enumerate(B):
    if n>A[i]:
        n-=A[i]
        A[i]=0
        
        if n>A[i+1]:
            n-=A[i+1]
            A[i+1]=0
        else:
            A[i+1]-=n
            n=0
    else:
        A[i]-=n
        n=0

print(bef-sum(A))