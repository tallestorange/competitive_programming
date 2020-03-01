N, M = map(int, input().split())
d = {i:[] for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)

used = [False] * (N+1)

def check(r, p):
    q = [(r, p)]
    result = True
    while q:
        root, pos = q.pop()
        used[pos] = True

        for p in d[pos]:
            if p==root:
                continue
            if used[p] and used[pos]:
                result = False
                continue
            q.append((pos, p))
    return result

p = 1
ans = 0
while p<=N:
    if not used[p]:
        ans += check(0, p)
    p += 1

print(ans)