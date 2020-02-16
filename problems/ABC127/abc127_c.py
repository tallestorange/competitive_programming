from itertools import accumulate as ac
N, M = map(int, input().split())
o = [0]*(N+2)

for _ in range(M):
    l, r = map(int, input().split())
    o[l] += 1
    o[r+1] -= 1

print(list(ac(o)).count(M))