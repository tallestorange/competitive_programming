from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
penalty = 0
accepted = 0

for p, S in (input().split() for _ in range(M)):
    d[p].append(S)

for k, v in d.items():
    tmp = 0
    for i in v:
        if i=="AC":
            accepted += 1
            penalty += tmp
            break
        else:
            tmp += 1

print(accepted, penalty)