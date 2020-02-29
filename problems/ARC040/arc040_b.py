N, R = map(int, input().split())
S = input()

for i, s in enumerate(S[::-1]):
    if s!="o":
        v = N-i
        break
else:
    v = 0

a, b = 0, (v//R-1)*R+(v%R) if v//R else 0
p = 0

while p<v:
    if S[p]==".":
        a += 1
        p += R
    else:
        p += 1

print(a+b)