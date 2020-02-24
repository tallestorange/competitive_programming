N, M = map(int, input().split())
*A, = map(int, input().split())

d = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
c = [(i, d[i]) for i in A]
minpos = min(c, key=lambda x:x[1])[1]

dp = [0] * (N+1)
digit = [0] * (N+1)

for i in range(minpos, N+1):
    for n, cost in c:
        if i-cost<0 or 0<i-cost<minpos: continue
        a = dp[i]
        b = dp[i-cost] + n * (10**(digit[i-cost]))
        if a<b:
            dp[i] = b
            digit[i] = digit[i-cost] + 1

print(dp[N])