N = int(input())

if N%2==1:
    print(0)
else:
    k2, k5 = 0, 0
    s = 1
    while 1:
        v = N//(2**s)
        if v==0:
            break
        else:
            k2 += v
        s+=1

    s = 1
    while 1:
        v = N//(5**s)
        if v==0:
            break
        else:
            k5 += (v//2)
        s+=1
    
    print(min(k2, k5))