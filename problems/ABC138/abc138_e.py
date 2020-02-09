from collections import defaultdict
from bisect import bisect_left

s = input()
t = input()
d = defaultdict(list)
e = defaultdict(int)

a, b = set(s), set(t)
if a&b!=b:
    print(-1)
else:
    for i,j in enumerate(s):
        d[j].append(i)
        e[j]+=1
    
    p = -1
    orig_size = len(s)
    ans = 0

    for i in t:
        a = bisect_left(d[i], p)
        if 0<= a < e[i]:
            p = d[i][a] + 1
        else:
            p = d[i][0] + 1
            ans += orig_size
    
    print(ans+p)