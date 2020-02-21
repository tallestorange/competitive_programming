from collections import defaultdict

N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()
d = defaultdict(int)

mod = 10**9+7
v = 0
for i, j in enumerate(l):
    v += (N-i)*j
    d[j] += 1

c = 1
for i in d.values():
    for j in range(1, i+1):
        c *= j
        c %= mod

print(v)
print(c)