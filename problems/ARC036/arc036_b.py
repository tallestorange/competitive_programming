N = int(input())
l = [int(input()) for _ in range(N)]
d1 = {i:0 for i in range(N)}
d2 = {i:0 for i in range(N)}

v = 0
bef = 0
for i,j in enumerate(l):
    if i and bef>j:
        d1[i-1] = v
        v = 1
    else:
        v += 1
    bef = j
if v>=1:
    d1[i] = v

l.reverse()
v = 0
bef = 0
for i,j in enumerate(l):
    if i and bef>j:
        d2[N-(i)] = v
        v = 1
    else:
        v += 1
    bef = j
if v>=1:
    d2[0] = v

print(max(d1[i]+d2[i]-1 for i in range(N)))