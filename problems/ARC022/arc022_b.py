N = int(input())
*A, = map(int, input().split())
u = set()
l, r, ans = 0, 0, 0

while l<N:
    while r<N:
        if A[r] in u:
            break
        else:
            u.add(A[r])
            r += 1
    ans = max(ans, r-l)
    u.remove(A[l])
    l += 1

print(ans)