N = int(input())
*A, = map(int, input().split())

ans = []
x = sum((-1)**i*j for i,j in enumerate(A))
ans.append(x)

for i in A[:-1]:
    x = i*2-x
    ans.append(x)

print(*ans)