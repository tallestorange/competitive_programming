mod = 10**9+7
fac = [1]*(N+1)
rev = [1]*(N+1)
 
for i in range(1,N+1):
  fac[i] = i*fac[i-1]%mod
  rev[i] = pow(fac[i], mod-2, mod)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%mod