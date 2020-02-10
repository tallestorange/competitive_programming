N = int(input())
*C, = map(int, input().split())
C.sort(reverse=True)

mod = 10**9+7

ans = 0
for i,c in enumerate(C, start=1):
    ans += (c*(i+1))
ans *= (4**(N-1))
ans %= mod
print(ans)