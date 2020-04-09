from collections import Counter as c
from itertools import combinations, product

A = input()
B = input()
ca, cb = c(A), c(B)
isdupe = any(filter(lambda x:x>=2, ca.values()))
N = len(A)
l = [i for i in range(N) if A[i]!=B[i]]
sa, sb = "".join(A[i] for i in l), "".join(B[i] for i in l)
size = len(l)

def f(sa, sb, n):
    for i in product(combinations(range(size), 2), repeat=n):
        l = list(sa)
        for s, t in i:
            l[s], l[t] = l[t], l[s]
        if "".join(l)==sb:
            return True
    return False

if size>6 or size==1 or ca!=cb:
    print("NO")
elif size==0:
    print("YES" if isdupe else "NO")
else:
    r1, r2, r3 = f(sa, sb, 1), f(sa, sb, 2), f(sa, sb, 3)
    if isdupe:
        print("YES" if r1 or r2 or r3 else "NO")
    else:
        print("YES" if r3 else "NO")
