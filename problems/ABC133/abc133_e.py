from collections import defaultdict
v = defaultdict(list)
mod = 10**9+7

N, K = map(int, input().split())
for _ in range(N-1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

visited = [False]*(N+1)
ans = 1

q = [(1, 0, 0)]
while q:
    pos, parent, score = q.pop()
    visited[pos] = True
    ans *= (K-score)
    ans %= mod 
   
    a = 1 if pos==1 else 2
    b = 0

    for i in v[pos]:
        if visited[i]:continue
        q.append((i, pos, a+b))
        b += 1

print(ans)
