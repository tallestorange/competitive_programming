N, X = map(int, input().split())
q = [1]*(N+1)
p = [1]*(N+1)
for i in range(1, N+1):
    q[i] = 2*q[i-1]+3
    p[i] = 2*p[i-1]+1

ans = 0
s = [(X, N)]
while s:
    x, n = s.pop()
    if n==0:
        ans += x!=0
    if x:
        a = q[n-1] + 2
        b = p[n-1] + 1

        if x >= a:
            ans += b
            s += [(x-a, n-1)]
        else:
            s += [(x-1, n-1)]

print(ans)