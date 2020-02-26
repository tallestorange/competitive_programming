from collections import defaultdict as dd
from heapq import heappop, heappush

N, K = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x:-x[1])
used = set()
q1 = dd(list)
q2, q3 = [], []

score, kind = 0, 0

for t, d in l[:K]:
    score += d
    if t in used:
        heappush(q3, d)
    else:
        used.add(t)
        kind += 1

for t, d in l[K:]:
    if not t in used:
        heappush(q1[t], -d)
for t in q1.keys():
    d = heappop(q1[t])
    heappush(q2, d)

ans = score + kind*kind
while q2 and q3:
    score -= heappop(q2)+heappop(q3)
    kind += 1
    ans = max(ans, score + kind*kind)

print(ans)
