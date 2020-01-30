from fractions import gcd
from functools import reduce

N, M = map(int, input().split())
*a, = map(int, input().split())
lcm = reduce(lambda x,y:x*y//gcd(x,y), a)

for i in map(lambda x:lcm//x, a):
    if i%2==0:
        print(0)
        break
else:
    start = lcm//2
    print((M-start)//lcm+1)