from collections import deque
from bisect import bisect_left

N = int(input())
d = deque([])
l = [int(input()) for _ in range(N)]

d.append(l[0])

for i in l[1:]:
    v = bisect_left(d, i)
    if v == 0:
        d.appendleft(i)
    else:
        d[v-1] = i

print(len(d))