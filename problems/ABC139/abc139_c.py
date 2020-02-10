N = int(input())
*H, = map(int, input().split())
ans = 0

l, r = 0, 1
while l < N:
    v = H[l]
    a = 0
    while r < N:
        if H[r]<=v:
            a += 1
            v = H[r]
            r += 1
        else:
            l = r-1
            r = l+2
            break
    ans = max(ans, a)
    l+=1
print(ans)