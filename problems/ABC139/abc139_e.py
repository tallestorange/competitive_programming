N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

size = N*N
d = [set() for _ in range(size)]
e = [set() for _ in range(size)]

for i, j in enumerate(l, start=1):
    p = 0
    for k in j:
        while 1:
            s = (i, k) if i<k else (k, i)
            if not s in d[p] and not i in e[p] and not k in e[p]:
                d[p]|={s}
                e[p]|={i,k}
                break
            elif s in d[p]:
                p += 1
                break
            else:
                p += 1

ans = size-sum(not i for i in d)
total = N*(N-1)//2

print(ans if ans<=total else -1)