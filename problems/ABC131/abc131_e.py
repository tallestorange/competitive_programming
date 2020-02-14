N, K = map(int, input().split())

def f(N, K):
    for k in range(1, N+1):
        a = k*(k-1)//2
        for l in range(k):
            b = l*(l-1)//2
            if a-b==K and 1+k==N:
                return (k, l)

    return (-1, -1)

a, b = f(N, K)
if a==-1 and b==-1:
    print(-1)
else:
    l = []
    v = []

    for i in range(a):
        l.append((1, i+2))
        v.append(i+2)

    for i in range(b-1):
        l.append((v[i], v[i+1]))

    print(len(l))
    for i,j in l:
        print(i, j)