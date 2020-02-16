from itertools import accumulate
N, K = map(int, input().split())
*V, = map(int, input().split())

ans = 0
for a in range(N+1):
    for b in range(N+1):
        if a+b>N:continue
        t = []
        if a:
            t += V[:a]
        if b:
            t += V[-b:]
        t.sort()
        t = [0]+t
        
        v = sum(t)
        for c in range(a+b+1):
            v -= t[c]
            if a+b+c<=K:
                ans = max(ans, v)

print(ans)