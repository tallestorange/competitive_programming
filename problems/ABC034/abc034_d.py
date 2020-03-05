N, K = map(int, input().split())
o = []

for _ in range(N):
    w, p = map(int, input().split())
    o.append((w, p))

def can(x):
    a = sorted([w*(p-x) for w,p in o])[::-1]
    if sum(a[:K])>=0:
        return True
    return False

l, r = -1, 200
for _ in range(30):
    m = (l+r)/2
    if can(m):
        l = m
    else:
        r = m

print(l)