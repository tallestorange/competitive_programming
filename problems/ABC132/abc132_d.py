N, K = map(int, input().split())

mod = 10**9+7
fac = [1]*(N+1)
rev = [1]*(N+1)
 
for i in range(1,N+1):
  fac[i] = i*fac[i-1]%mod
  rev[i] = pow(fac[i], mod-2, mod)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%mod

for i in range(1, K+1):
    v1 = comb(K-1, i-1)
    v2 = 0

    if i == 1:
        v2 = N-K+1
    else:
        for j in range(i-1, N-K+1):
            v2 += comb(j-1, i-2) * (N-K-j+1)
    print((v1*v2)%mod)