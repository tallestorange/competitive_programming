from math import pi

N, Q = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
d = [0]*(20001)

for x in range(20001):
    v = 0
    for x1, r1, h1 in l:
        V1 = (pi*(r1**2)*h1)/3
        if x1 <= x <= x1+h1:
            H1 = h1-(x-x1)
            R1 = H1*r1/h1
            V2 = (pi*(R1**2)*H1)/3

            v += (V1-V2)
        elif x > x1+h1:
            v += V1
    d[x] = v

for _ in range(Q):
    A, B = map(int, input().split())
    print(d[B]-d[A])