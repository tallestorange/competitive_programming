from collections import defaultdict as dd
from heapq import heappop, heappush

N, K = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x:-x[1])
q1 = dd(list)
used = set()

score = 0
for t, d in l[:K]:
    score += d
    used.add(t)
    heappush(q1[t], d)

kind = len(used)
ans = score + kind*kind
q2, q3 = [], []

for t, d in l[K:]:
    heappush(q2, (-d, t))

for t in q1.keys():
    c = len(q1[t])-1
    for _ in range(c):
        d = heappop(q1[t])
        heappush(q3, (d, t))

while q2 and q3:
    while q2:
        d1, t1 = heappop(q2)
        d1 = -d1
        if not t1 in used:
            break
    if not t1 is used:
        used.add(t1)
        d2, t2 = heappop(q3)
        score -= d2
        score += d1
        kind += 1
        ans = max(ans, score + kind*kind)

print(ans)