from functools import lru_cache
import sys
sys.setrecursionlimit(9000000)

@lru_cache(maxsize=None)
def f(l, r):
    if l==r: return a[r]
    return max(a[l]-f(l+1, r),  a[r]-f(l, r-1))

N = int(input())
*a, = map(int, input().split())
print(f(0, N-1))