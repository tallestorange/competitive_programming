from collections import Counter
from bisect import bisect_left

N = int(input())
s = [int(input()) for _ in range(N)]
zero = 0 in s

c = Counter(s)
n = N
l = []

bef = 0
for i,j in sorted(c.items()):
    if i:
        if bef and zero:
            l.append((bef+1, n))
        elif (not bef) and (not zero):
            l.append((bef, n))
        elif not zero:
            l.append((bef+1, n))
        bef = i
        n -= j
    else:
        n -= j
        l.append((0, n))
l.append((bef+1, 0))

size = len(l)

def check(l, x):
    left, right = -1, size
    while right-left>1:
        m = (left+right)//2
        if l[m][1] > x:
            left = m
        else:
            right = m
    
    return l[right][0]

Q = int(input())
for _ in range(Q):
    k = int(input())
    print(check(l, k))