from collections import Counter

N = int(input())
*D, = map(int, input().split())
mod = 998244353
c = Counter(D)
v = max(D)

if c[0]!=1 or D[0]!=0:
    print(0)
else:
    ans = 1
    for i in range(1, v+1):
        ans *= pow(c[i-1], c[i], mod)
        ans %= mod
    print(ans)