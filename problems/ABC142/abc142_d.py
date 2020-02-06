from fractions import gcd
from collections import defaultdict

A, B = map(int, input().split())
x = gcd(A, B)
d = defaultdict(int)

d[1]=1
for i in range(2, int(x**0.5)+1):
    while x%i==0:
        x//=i
        d[i]+=1
if x!=1:
    d[x]+=1

ans = len(d.keys())
print(ans)