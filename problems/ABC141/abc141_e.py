N = int(input())
S = input()
ans = 0
l, r = 0, 1

while l<N:
    s1 = S[l]
    v = 0
    while r<N:
        s2 = S[r]
        if s1!=s2:
            r+=1
            continue
        v = 1
        for i in range(1, r-l):
            if r+i>=N or l+i>=r:break
            if S[l+i]!=S[r+i]:continue
            v+=1
        ans = max(ans, v)
        r+=1
    l+=1
    r=l+1
print(ans)