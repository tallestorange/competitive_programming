from itertools import product

N = int(input())
c = product(range(2), repeat=N)
d = [[] for _ in range(N)]

for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        d[i].append((x, y))


ans = 0
for l in c:
    is_conflict = False
    for i, j in enumerate(l):
        if j==0:continue
        for x, y in d[i]:
            if l[x-1]!=y:
                is_conflict = True
                break
        if is_conflict == True:
            break
    else:
        ans = max(ans, sum(l))

print(ans)