s = input()
n = len(s)
l = 0
r = n-1
ans = 0

while l<r:
    if s[l]!=s[r]:ans+=1
    l+=1
    r-=1

print(ans)