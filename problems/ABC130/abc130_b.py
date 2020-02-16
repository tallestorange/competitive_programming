N, X = map(int, input().split())
*L, = map(int, input().split())

v = 0
ans = 1
for i in L:
    v += i
    if v<=X:
        ans += 1

print(ans)
