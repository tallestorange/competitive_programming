from bisect import bisect_left

N = int(input())
*A, = map(int, input().split())
A.sort()

if A[0]<=0 and A[-1]<=0:
    ans = sum(map(abs, A[:-1]))+A[-1]
    A.reverse()

    r = 1
    a, b = A[0], A[1]
    t = []
    
    while 1:
        x, y = (a, b) if a>b else (b, a)
        t.append((x, y))
        r += 1
        if not r<N:
            break
        a, b = x-y, A[r]

elif A[0]>=0 and A[-1]>=0:
    ans = sum(A[1:])-A[0]

    r = 1
    a, b = A[0], A[1]
    t = []
    
    while 1:
        x, y = (a, b) if a<b else (b, a)
        t.append((x, y))
        
        r += 1
        if not r<N:
            break
        a, b = x-y, A[r]
    a, b = t[-1]
    t[-1] = (b, a)


else:
    ans = sum(map(abs, A))
    p = bisect_left(A, 0)
    t = []
    s = []

    a = A[p-1]
    for i in range(p, N-1):
        b = A[i]
        t.append((a, b))
        a = a - b
        
    c = A[N-1]
    for i in ([a]+A[:p-1]):
        t.append((c, i))
        c = c-i

print(ans)
for i in t:
    print(*i)