N, K = map(int, input().split())
*A, = map(int, input().split())
A.sort()

mod = 10**9+7
fac = [1]*(N+1)
rev = [1]*(N+1)
 
for i in range(1,N+1):
  fac[i] = i*fac[i-1]%mod
  rev[i] = pow(fac[i], mod-2, mod)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%mod

maxA, minA = 0, 0

for i in range(N-K+1):
    minA += A[i]*comb(N-i-1, K-1)

for j in range(K-1, N):
    maxA += A[j]*comb(j, K-1)

print((maxA-minA)%mod)