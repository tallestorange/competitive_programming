from collections import deque

N = int(input())
S = input()
dp = [[[[0]*(N+1) for _ in range(N+1)] for _ in range(4)] fpr _ in range(4)]

for i in range(1, N+1):
    for j in range(i+1):
        # for l in range(4):
        #     for r in range(4):
        s = S[i-1]
        if s == "R":
            dp[i-1][j-2] = dp[i-1][j-1][1]
            pass
        elif s == "G":
            pass
        elif s == "B":
            pass