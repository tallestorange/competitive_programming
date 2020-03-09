T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
v1, v2 = A1 - B1, A2 - B2
d1, d2 = v1 * T1, v2 * T2
if d1 > 0:
    d1 *= -1
    d2 *= -1

if d1 + d2 < 0:
    print(0)
elif d1 + d2 ==  0:
    print("infinity")
elif d1 + d2 > 0:
    s, t = divmod(-d1, d1+d2)
    print(2*s+(t!=0))