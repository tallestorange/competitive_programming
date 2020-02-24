N = int(input())

a, b, c, d = 0, 0, 0, 0
for _ in range(N):
    s = input()
    if s[0]=="B" and s[-1]=="A":
        a += 1
    elif s[0]=="B":
        b += 1
    elif s[-1]=="A":
        c += 1
    d += s.count("AB")

ans = d
if b==c==0:
    ans += max(0, a-1)
else:
    ans += a + min(b, c)
print(ans)