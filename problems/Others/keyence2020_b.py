N = int(input())
l = []

for _ in range(N):
    X, L = map(int, input().split())
    l.append((X-L, X+L))

l.sort(key=lambda x:x[1])
before = -10**9
ans = 0

for i, j in l:
    if i>=before:
        ans += 1
        before = j
print(ans)