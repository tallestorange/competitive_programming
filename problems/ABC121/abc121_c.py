N, M = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort()

v = 0
ans = 0

for a, b in l:
    if b+v >= M:
        ans += a*(M-v)
        break
    else:
        ans += a*b
        v+=b

print(ans)