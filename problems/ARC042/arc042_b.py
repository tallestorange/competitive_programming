x, y = map(int, input().split())
N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]
ans = 10**12

for i in range(N):
    x1, y1 = l[i]
    x2, y2 = l[i-1]

    p1x, p1y = x1-x, y1-y
    p2x, p2y = x2-x, y2-y

    op1 = p1x**2 + p1y**2
    op2 = p2x**2 + p2y**2
    p1p2 = p1x*p2x + p1y*p2y
    
    a = (op1 * op2 - p1p2**2)

    ppx, ppy = x2-x1, y2-y1

    b = (ppx**2 + ppy**2)

    v = (a/b) ** 0.5
    ans = min(ans, v)

print(ans)