from collections import defaultdict

V = defaultdict(list)
N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)
*c, = map(int, input().split())
c.sort(reverse=True)

root, _ = max(V.items(), key=lambda x:len(x[1]))
visited = [False] * (N+1)
identifier = [0] * (N+1)

p = 0
q = [root]
while q:
    a = q.pop()
    visited[a] = True
    identifier[a] = p

    p+=1

    for i in V[a]:
        if visited[i]:continue
        q.append(i)

cost = 0
visited = [False] * (N+1)
q = [root]
while q:
    a = q.pop()
    visited[a] = True
    p+=1

    for b in V[a]:
        if visited[b]:continue
        cost += min(c[identifier[a]], c[identifier[b]])
        q.append(b)

print(cost)
print(*[c[i] for i in identifier[1:]])