N, K = map(int, input().split())

mod = 10**9+7
fac = [1]*(N+1)
rev = [1]*(N+1)
 
for i in range(1,N+1):
  fac[i] = i*fac[i-1]%mod
  rev[i] = pow(fac[i], mod-2, mod)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%mod
for i in range(1, K+1):
    ans = (comb(K-1, i-1)*comb(N-K+1, i))%mod if N-K+1>=i else 0
    print(ans)