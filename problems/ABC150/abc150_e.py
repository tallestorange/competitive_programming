from itertools import combinations

N = int(input())
*C, = map(int, input().split())
C.sort()
mod = 10**9+7

ans = 0
for k in range(1, N+1):
    for m in combinations(C, k):
        for j, p in enumerate(m):
            ans += (k-j)*p

ans *= pow(2, N, mod)
ans %= mod
print(ans)