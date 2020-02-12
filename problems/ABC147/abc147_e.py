H, W = map(int ,input().split())

d = [[0]*(W+1) for _ in range(H+1)]
inf = 10**12
dp = [[[0]*(W+1) for _ in range(H+1)] for _ in range(12801)]
dp[0][0][0] = 1

for i in range(H):
    for j, n in enumerate(map(int, input().split())):
        d[i+1][j+1] = n
    
for i in range(H):
    for j, n in enumerate(map(int, input().split())):
        d[i+1][j+1] -= n

for i in range(1, H+1):
    for j in range(1, W+1):
        for k in range(12801):
            if abs(k-d[i-1][j])<12801:
                dp[k][i][j] |= dp[abs(k-d[i-1][j])][i-1][j]
            if abs(k+d[i-1][j])<12801:
                dp[k][i][j] |= dp[abs(k+d[i-1][j])][i-1][j]
            if abs(k-d[i][j-1])<12801:
                dp[k][i][j] |= dp[abs(k-d[i][j-1])][i][j-1]
            if abs(k+d[i][j-1])<12801:
                dp[k][i][j] |= dp[abs(k+d[i][j-1])][i][j-1]
