N = int(input())
*X, = map(int, input().split())

ans = 10**15
for i in range(1, 101):
    v = 0
    for j in X:
        v += (j-i)**2
    ans = min(ans, v)

print(ans)