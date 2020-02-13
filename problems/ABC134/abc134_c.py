N = int(input())
l = [int(input()) for _ in range(N)]

dp1 = [0]*(N+1)
dp2 = [0]*(N+2)

for i in range(1, N+1):
    dp1[i] = max(dp1[i-1], l[i-1])

for i in range(1, N+1)[::-1]:
    dp2[i] = max(dp2[i+1], l[i-1])

for i in range(1, N+1):
    print(max(dp1[i-1], dp2[i+1]))