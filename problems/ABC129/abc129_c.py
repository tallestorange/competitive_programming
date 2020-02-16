from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
mod = 10**9+7

a = [1] * (N+1)
for _ in range(M):
    a[int(input())] = 0

@lru_cache()
def f(x):
    v = 0
    if x<0:
        return 0
    if x == 0:
        return 1
    if a[x-1]:
        v += f(x-1)
    if a[x-2]:
        v += f(x-2)
    v %= mod
    return v

print(f(N))