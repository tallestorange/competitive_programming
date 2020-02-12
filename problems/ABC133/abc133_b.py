from itertools import combinations

N, D = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in combinations(d, 2):
    dist = sum(abs(i-j)**2 for i,j in zip(a, b))
    for i in range(1, int(dist**0.5)+1):
        if i**2==dist:
            ans += 1
            break
    
print(ans)