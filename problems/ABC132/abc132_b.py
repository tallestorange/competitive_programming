from itertools import permutations

n = int(input())
*p, = map(int, input().split())

ans = 0
for j, k in enumerate(p[:-2]):
    a, b, c = k, p[j+1], p[j+2]
    if a < b < c or c < b < a:
        ans += 1

print(ans)