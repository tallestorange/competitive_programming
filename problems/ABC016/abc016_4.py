Ax, Ay, Bx, By = map(int, input().split())
N = int(input())


def isCrossed(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    f = lambda x1, y1, x2, y2: lambda x, y: (x1-x2)*(y-y1)+(y1-y2)*(x1-x)
    g1 = f(x1, y1, x2, y2)
    g2 = f(x3, y3, x4, y4)

    return g1(x3, y3) * g1(x4, y4) < 0 and g2(x1, y1) * g2(x2, y2) < 0



l = [tuple(map(int, input().split())) for _ in range(N)]
c = sum(isCrossed((Ax, Ay), (Bx, By), l[i], l[i-1]) for i in range(N))
print((c//2)+1)