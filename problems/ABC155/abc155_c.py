from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
    d[input()] += 1

v = max(d.values())
for s in sorted([i[0] for i in d.items() if i[1]==v]):
    print(s)