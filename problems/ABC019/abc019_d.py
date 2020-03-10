import sys
from itertools import combinations

N = int(input())
v = 0
p = 0

for i in range(2, N+1):
    print("?", 1, i)
    sys.stdout.flush()
    dist = int(input())
    if v < dist:
        v = dist
        p = i

ans = 0
for i in range(1, N+1):
    if i==p:continue
    print("?", p, i)
    sys.stdout.flush()
    dist = int(input())
    ans = max(ans, dist)

sys.stdout.flush()
print("!", ans)