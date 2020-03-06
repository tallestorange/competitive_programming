N, K = map(int, input().split())

n = N + K
MOD = 10**9+7
fac = [1]*(n+1)
rev = [1]*(n+1)
 
for i in range(1,n+1):
  fac[i] = i*fac[i-1]%MOD
  rev[i] = pow(fac[i], MOD-2, MOD)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%MOD

if K>=N:
    print(comb(N, K%N))
else:
    print(comb(N+K-1, K))