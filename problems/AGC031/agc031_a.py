from collections import Counter

N = int(input())
S = input()
c = Counter(S)
mod = 10**9+7

ans = 1
for i in c.values():
    ans *= (i+1)
    ans %= mod
print(ans-1)