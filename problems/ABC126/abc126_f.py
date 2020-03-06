M, K = map(int, input().split())

if K==0:
    l = []
    for i in range(2**M):
        l += [i, i]
    print(*l)
elif M==0 or M==1:
    print(-1)
elif 1<=K<2**M:
    l = []    
    for i in range(2**M):
        if i!=K:
            l += [i]
    l += [K]
    for i in range(2**M)[::-1]:
        if i!=K:
            l += [i]
    l += [K]
    print(*l)
else:
    print(-1)