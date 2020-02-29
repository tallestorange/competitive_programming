S = input()
n = len(S)
l1 = [0] * (n+1)
l2 = [0] * (n+1)

v = 0
for i in range(1, n+1):
    if S[i-1] == "<":
        v += 1
        l1[i] = v
    else:
        v = 0

v = 0
for i in range(n)[::-1]:
    if S[i] == ">":
        v += 1
        l2[i] = v
    else:
        v = 0

ans = 0
for i, j in zip(l1, l2):
    ans += max(i, j)

print(ans)