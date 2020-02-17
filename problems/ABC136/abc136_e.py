N, K = map(int, input().split())
*A, = map(int, input().split())
A.sort()

S = sum(A)
candidates = []
for i in range(1, int(S**0.5)+1):
    if S%i:continue
    a, b = i, S//i
    
    candidates.append(a)
    if a!=b:
        candidates.append(b)
candidates.sort()

ans = 0
for d in candidates:
    m = [i%d for i in A if i%d]
    m.sort()
    modsum = sum(m)
    
    a = 0
    for i, j in enumerate(m[:-1], start=1):
        a += j
        b = d*(N-i)-(modsum-a)
        print(a, b, d)
        if a==b and a<=K:
            ans = max(ans, d)

print(ans)