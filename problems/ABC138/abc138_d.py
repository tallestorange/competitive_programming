from collections import defaultdict
N,  Q = map(int ,input().split())

d = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

dp = [0]*N
used = [False]*N

for _ in range(Q):
    p, x = map(int, input().split())
    dp[p-1] += x

q = [1]
used[0] = True

while q:
    x = q.pop()
    
    for i in d[x]:
        if used[i-1]==True:
            continue
        dp[i-1] += dp[x-1]
        used[i-1] = True
        q.append(i)

print(*dp)