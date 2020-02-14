N, K = map(int, input().split())

def f(N, K):
    for i in range(1, N+1):
        a = i*(i-1)//2
        for j in range(1, N+1):
            b = j
            for k in range(0, N+1):
                c = k
                if i+j+k+1==N and a+b+c==K:
                    return (i, j, k)
    return (-1, -1, -1)

i, j, k = f(N, K)
if i==-1 and j==-1 and k==-1:
    print(-1)
else:
    l = []
    a = 1
    for a in range(2, 2+i):
        l.append((1,a))

    p = a
    for a in range(p, p+j):
        l.append((a, a+1))
    p = a

    for a in range(p+1, N+1):
        for b in range(a+1, N+1):
            l.append((a,b))
    
    print(len(l))
    for a, b in l:
        print(a, b)