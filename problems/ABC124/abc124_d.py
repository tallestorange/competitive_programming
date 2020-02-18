from itertools import accumulate as ac

N, K = map(int, input().split())
*S, = map(int, input())

l = []
c = 0

if N==1:
    l.append(S[0])
else:
    for i in range(N-1):
        c += 1
        if S[i]!=S[i+1]:
            l.append(c)
            c = 0
    if c:
        l.append(c+1)

if S[0]==0:
    l = [0]+l
if S[-1]==0:
    l.append(0)

size = len(l)
*a, = ac([0]+l)
group_size = min(2*K+1,size)

ans = 0
for i in range(group_size, size+1, 2):
    ans = max(ans, a[i]-a[i-group_size])
print(ans)