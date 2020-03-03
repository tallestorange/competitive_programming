N, K = map(int, input().split())
MOD = 10**9+7
*A, = map(int, input().split())
ans = 0

for i,bi in enumerate(A):
    a, b = 0, 0
    
    for j in range(N):
        print(i,j)
        if bi>A[j]:
            a += 1
        if i>j and bi>A[j]:
            b += 1
    
    ans += a*K+b
    ans %= MOD

print(ans)