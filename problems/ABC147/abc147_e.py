H, W = map(int, input().split())

d = [[0]*(W+1) for _ in range(H+1)]
vmax = (H+W)*80
dp = [[[False]*(vmax+1) for _ in range(W+1)] for _ in range(H+1)]
dp[1][1][0] = True

for i in range(H):
    for j, n in enumerate(map(int, input().split())):
        d[i+1][j+1] = n
for i in range(H):
    for j, n in enumerate(map(int, input().split())):
        d[i+1][j+1] -= n
        d[i+1][j+1] = abs(d[i+1][j+1])

for i in range(1, H+1):
    for j in range(1, W+1):
        v1 = d[i-1][j]
        v2 = d[i][j-1]
        d1 = dp[i-1][j]
        d2 = dp[i][j-1]

        for k in range(v1, vmax+1):
            dp[i][j][k] |= d1[k-v1] 
        for k in range(0, vmax-v1+1):
            dp[i][j][k] |= d1[k+v1]
        for k in range(v2, vmax+1):
            dp[i][j][k] |= d2[k-v2]
        for k in range(0, vmax-v2+1):
            dp[i][j][k] |= d2[k+v2]

v = d[H][W]
ans = vmax
for i,j in enumerate(dp[H][W]):
    if not j:continue
    ans = min(ans, abs(i+v), abs(i-v))

print(ans)