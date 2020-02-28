MOD = 10**9+7
n = 10**5
fac = [1]*(n+1)
rev = [1]*(n+1)
 
for i in range(1,n+1):
  fac[i] = i*fac[i-1]%MOD
  rev[i] = pow(fac[i], MOD-2, MOD)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%MOD


if __name__ == "__main__":
  print(comb(6, 2))