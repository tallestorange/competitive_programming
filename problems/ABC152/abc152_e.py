from fractions import gcd
from functools import reduce

N = int(input())
*A, = map(int, input().split())
mod = 10**9 + 7

lcm = reduce(lambda a,b: a*b//gcd(a,b), A)

print(sum(map(lambda x: lcm//x, A))%mod)