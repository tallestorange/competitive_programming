H, W = map(int, input().split())

A = [tuple(map(int, input().split())) for _ in range(H)]
B = [tuple(map(int, input().split())) for _ in range(H)]
C = [[abs(i-j) for i, j in zip(a, b)] for a, b in zip(A, B)]

dmax = max([j for i in C for j in i])
vmax = (H+W) * dmax

dp = [[[0]*(vmax+1) for _ in range(W)] for _ in range(H)]
dp[0][0][C[0][0]] = 1

for i in range(H):
    for j in range(W):
        for k in range(vmax+1):
            if i+1<H:
                k1, k2 = k+C[i+1][j], abs(k-C[i+1][j])
                if k1<=vmax:
                    dp[i+1][j][k1] |= dp[i][j][k]
                if k2<=vmax:
                    dp[i+1][j][k2] |= dp[i][j][k]

            if j+1<W:
                k1, k2 = k+C[i][j+1], abs(k-C[i][j+1])
                if k1<=vmax:
                    dp[i][j+1][k1] |= dp[i][j][k]
                if k2<=vmax:
                    dp[i][j+1][k2] |= dp[i][j][k]

print(dp[H-1][W-1].index(1))