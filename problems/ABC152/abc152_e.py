from functools import reduce

def gcd(x, y):
    if (y==0):return x
    else:return gcd(y, x%y)

N = int(input())
*A, = map(int, input().split())
mod = 10**9 + 7
lcm = reduce(lambda a,b: a*b//gcd(a,b), A)

print(sum(map(lambda x: lcm//x, A))%mod)