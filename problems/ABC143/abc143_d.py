from bisect import bisect_left

N = int(input())
*L, = map(int, input().split())
L.sort()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        a, b = L[i], L[j]
        ans += (bisect_left(L, a+b)-(j+1))

print(ans)