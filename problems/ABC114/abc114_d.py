from collections import defaultdict, Counter
from itertools import permutations as p

def factorize(n):
    d = defaultdict(int)
    for i in range(2, int(n**0.5)+1):
        while n%i==0:
            d[i] += 1
            n //= i
        if not n:
            break
    if n>1:
        d[n] += 1
    return d

N = int(input())
d = Counter()
for i in range(1, N+1):
    d += factorize(i)
vl = d.values()

ans = sum(1 for i, j, k in p(vl, 3) if i>=2 and j>=4 and k>=4)//2
ans += sum(1 for i, j in p(vl, 2) if i>=2 and j>=24)
ans += sum(1 for i, j in p(vl, 2) if i>=4 and j>=14)
ans += sum(1 for i in vl if i>=74)
print(ans)