X, Y = map(int, input().split())

mod = 10**9+7
N = 1333334
fac = [1]*(N+1)
rev = [1]*(N+1)
 
for i in range(1,N+1):
  fac[i] = i*fac[i-1]%mod
  rev[i] = pow(fac[i], mod-2, mod)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%mod

a, b = (2*X-Y)//3, (2*Y-X)//3
if a<0 or b<0 or (2*X-Y)%3 or (2*Y-X)%3:
    print(0)
else:
    print(comb(a+b, a))
