N = int(input())
*H, = map(int, input().split())

ans = 0
for i in range(N):
    canSee = True
    for j in range(0, i):
        if not H[j]<=H[i]:
            canSee = False
            break
    ans += canSee
print(ans)