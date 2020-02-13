from collections import defaultdict
from bisect import bisect_left

N = int(input())
d = defaultdict(list)

for i in range(N):
    v = int(input())
    d[v].append(i)

keys = sorted(d.keys())
s = d[keys[0]]

for k in keys[1:]:
    used = set()
    for i in d[k]:
        j = bisect_left(s, i)
        if 0<j<=len(s):
            if not s[j-1] in used:
                s[j-1] = i
            else:
                s = s[:j] + [i] + s[j:]
        elif j==0:
            s = [i]+s
        used |= {i}

print(len(s))