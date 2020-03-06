T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

d1 = A1*T1+A2*T2
d2 = B1*T1+B2*T2

if d1==d2:
    print("infinity")
elif A1==B1:
    print(1)
else:
    v1 = A1*T1
    v2 = B1*T1
    if (v1-v2<0 and d1-d2<0) or (v1-v2>0 and d1-d2>0):
        print(0)
    else:
        print(1+2*(abs(v1-v2)//abs(d1-d2)))
