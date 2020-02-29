N = int(input())

n1 = 8*N+1
a = int(n1**0.5)

if N==1:
    print("Yes")
    print(2)
    print(1, 1)
    print(1, 1)
elif n1==a**2:
    n = (-3+a)//2
    d = [[0]*(n+1) for _ in range(n+2)]
    d[0][0] = 1
    d[0][1] = 2
    d[1][0] = 2
    d[1][1] = 3
    d[2][0] = 3
    d[2][1] = 1
    for i in range(1, n):
        v = 4+((i-1)*(i+4)//2)
        c = 2+i

        for j in range(c):
            d[c][j] = v+j
            d[j][c-1] = v+j

    print("Yes")
    print(n+2)
    for i in range(n+2):
        print(n+1, *d[i], sep=" ")
else:
    print("No")