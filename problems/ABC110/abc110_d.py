def factorize(n):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(2, int(n**0.5)+1):
        while n%i==0:
            d[i] += 1
            n //= i
        if not n:
            break
    if n>1:
        d[n] += 1
    return d


N, M = map(int, input().split())
d = factorize(M)

MOD = 10**9+7
n = N+30
fac = [1]*(n+1)
rev = [1]*(n+1)
 
for i in range(1,n+1):
  fac[i] = i*fac[i-1]%MOD
  rev[i] = pow(fac[i], MOD-2, MOD)
 
comb = lambda a,b:(fac[a]*rev[a-b]*rev[b])%MOD

v = 1
for i in d.values():
    v *= comb(i+N-1, i)
    v %= MOD
print(v)