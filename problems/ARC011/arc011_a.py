m, n, N = map(int, input().split())
ans = N

a = 0
while N:
    a += N%m
    print(a, N)
    if N//m:
        N = (N//m)*n 
    else:
        ans += (N+a)//m*n
        break
    ans += N

print(ans)