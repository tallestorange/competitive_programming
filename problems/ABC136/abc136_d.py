r, l = 0, 0
pr, pl = 0, 0

d = []
S = input()
for i,s in enumerate(S):
    if r!=0 and l!=0 and s=="R":
        d.append((r,l,pr,pl))
        r, l = 1, 0
    elif s=="R":
        r+=1
    elif s=="L" and l==0:
        pl, pr = i, i-1
        l+=1
    else:
        l+=1
if r!=0 and l!=0:
    d.append((r,l,pr,pl))

ans = [0]*len(S)
for r,l,pr,pl in d:
    ans[pl] = r//2 + l - l//2
    ans[pr] = l//2 + r - r//2

print(*ans)