A, B = map(int, input().split())

def f(x):
    d = {}
    for i in range(45):
        k = 2**i
        if x-k<0:
            d[i] = 0
        else:
            A = (x-k)//k
            v = k*(A-A//2)
            if A%2==0:
                v += x-(A+1)*k+1
            d[i] = v
    return d

b = f(B)
for i,j in f(A-1).items():
    b[i] -= j

ans = 0
for i,j in b.items():
    if j%2:
        ans += 2**i
print(ans)
