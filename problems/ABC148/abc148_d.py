N = int(input())
*a, = map(int, input().split())

if not 1 in a:
    print(-1)
else:
    p = a.index(1)
    target = 2

    for i in range(p, N):
        if a[i]==target:
            target += 1
    
    print(N-target+1)