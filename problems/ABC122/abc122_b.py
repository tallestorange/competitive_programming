s = input()
N = len(s)
ans = 0
for i in range(N):
    v = 0
    for j in range(i, N):
        if not s[j] in {"A", "G", "C", "T"}:
            break
        v += 1
    ans = max(ans, v)
print(ans)