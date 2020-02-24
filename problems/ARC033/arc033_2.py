from collections import defaultdict

Na, Nb = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
d = defaultdict(int)

for i in A:
    d[i] += 1
for i in B:
    d[i] += 1

a, b = 0, 0
for i in d.values():
    a += 1
    if i==2:
        b += 1
print(b/a)