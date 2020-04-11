from itertools import combinations

N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]
t = {i for i in l}

if N==1 or N==2:
    print(1)
else:
    ans = N
    for i in range(N):
        for j, k in combinations([l[j] for j in range(N) if j!=i], 2):
            x1, y1 = j
            x2, y2 = k
            x, y = x1-x2, y1-y2

            b = 1
            for m in range(N):
                if i==m:continue
                x3, y3 = l[m]
                if not (x3-x, y3-y) in t:
                    b += 1
            ans = min(ans, b)
    print(ans)
