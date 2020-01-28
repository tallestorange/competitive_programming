N = int(input())
d = [[0] * 10 for _ in range(10)]
ans = 0

for n in range(1, N+1):
    s = str(n)
    a, b = int(s[0]), int(s[-1])
    d[a][b] += 1

for i in range(10):
    for j in range(10):
        ans += d[i][j] * d[j][i]

print(ans)