N, K = map(int, input().split())
*a, = map(int, input().split())

s, t = 0, 0
v = 0

ans = 0
while 1:
    while t<N and v<K:
        v += a[t]
        t += 1
    if v<K:break
    ans += N-t+1
    v -= a[s]
    s += 1

print(ans)