T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

def check(k):
    v1 = A1 - B1
    v2 = A2 - B2

    a, b = k//2, k%2
    d1 = (a+b)*(v1*T1) + (a)*(v2*T2)

    k += 1

    a, b = k//2, k%2
    d2 = (a+b)*(v1*T1) + (a)*(v2*T2)

    if d1==0:
        return True
    elif d2==0:
        return True
    elif (d1<0 and d2>0) or (d1>0 and d2<0):
        return True
    else:
        return False

if A1*T1+A2*T2 == B1*T1+B2*T2:
    print("infinity")
else:
    l = -1
    r = 10**20

    while r-l>1:
        m = (l+r)//2
        if check(m):
            l = m
        else:
            r = m
    
    print(l)