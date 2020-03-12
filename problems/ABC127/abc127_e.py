N, M, K = map(int, input().split())

MOD = 10**9+7
n = N*M-2
fac = [1]*(n+1)
rev = [1]*(n+1)
 
for i in range(1,n+1):
  fac[i] = i*fac[i-1]%MOD
  rev[i] = pow(fac[i], MOD-2, MOD)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%MOD

C = comb(N*M-2, K-2)
ans = 0
for d in range(N):
    ans += d*(N-d)*(M**2)*C
    ans %= MOD

for d in range(M):
    ans += d*(M-d)*(N**2)*C
    ans %= MOD

print(ans)