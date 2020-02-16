from itertools import accumulate
N, K = map(int, input().split())
*V, = map(int, input().split())

ans = 0
for a in range(N+1):
    for b in range(N+1):
        if a+b>N:continue
        
        if a and b:
            qa, qb = list(accumulate([0]+sorted(V[:a]))), list(accumulate([0]+sorted(V[-b:])))
            sa, sb = sum(V[:a]), sum(V[-b:])
            for c in range(a+1):
                for d in range(b+1):
                    if a+b+c+d<=K:
                        ans = max(ans, sa+sb-qa[c]-qb[d])
        elif a:
            qa = list(accumulate([0]+sorted(V[:a])))
            sa = sum(V[:a])
            for c in range(a+1):
                if a+c<=K:
                    ans = max(ans, sa-qa[c])
        elif b:
            qb = list(accumulate([0]+sorted(V[-b:])))
            sb = sum(V[-b:])
            for d in range(b+1):
                if b+d<=K:
                    ans = max(ans, sb-qb[d])

print(ans)