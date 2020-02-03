from itertools import permutations
from math import sqrt

N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
n = 0

for i in permutations(l):
    for j in range(N-1):
        x1, y1 = i[j]
        x2, y2 = i[j+1]
        ans += sqrt((x1-x2)**2+(y1-y2)**2)
    n += 1

print(ans/n)