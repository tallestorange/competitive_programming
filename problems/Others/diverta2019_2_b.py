N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort()
m = []

for i in range(N-1):
    x1, y1 = l[i]
    x2, y2 = l[i+1]
    m.append((x1-x2, y1-y2))

ans = 10**10

for p, q in m:
    v = 1
    for i in range(N-1):
        x, y = l[i]
        a, b = l[i+1]
        if not (x==a-p and y==b-q):
            v += 1
    ans = min(ans, v)

print(ans)