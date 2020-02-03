A, B, X = map(int, input().split())
f = lambda N:A*N+B*len(str(N)) <= X
l,r = 0, 10**9+1
while r-l>1:
    m = l+(r-l)//2
    if f(m):
        l = m
    else:
        r = m
print(l)