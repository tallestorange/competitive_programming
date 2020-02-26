N = int(input())
A = [int(input()) for _ in range(N)][::-1]

if A[-1]:
    print(-1)
else:
    bef = A[0]
    c, ans = 0, 0
    for i in A:
        if bef!=i:
            if bef-i > 1:
                ans = -1
                break
            ans += bef*c
            c = 1 if bef<i else 0
        else:
            c += 1
        bef = i
    print(ans)
