S = input().replace("25", "X")
c = 0
ans = 0

for s in S:
    if s=="X":
        c += 1
    else:
        if c:
            ans += c*(c+1)//2
        c = 0
if c:
    ans += c*(c+1)//2
print(ans)