N = int(input())
*R, = map(int, input().split())
dp = [[0]*2 for _ in range(N)]

for i in range(N):
    a = [dp[j][0] for j in range(i) if R[i]>R[j]]
    b = [dp[j][1] for j in range(i) if R[i]<R[j]]

    v1 = max(a) if a else 0
    v2 = max(b) if b else 0

    dp[i][1] = max(dp[i][1], v1+1)
    dp[i][0] = max(dp[i][0], v2+1)

ans = max(dp[-1])
print(ans if ans>=3 else 0)

