N = int(input())
ans = 0

l, m = [], []

for _ in range(N):
    s, t = input().split()
    t = int(t)
    l.append(s)
    m.append(t)

X = input()

idx = l.index(X)
for i in range(idx+1, N):
    ans += m[i]

print(ans)
