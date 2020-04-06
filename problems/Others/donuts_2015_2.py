from itertools import combinations as comb

N, M = map(int, input().split())
*A, = map(int, input().split())

bonus = []
d = {i:[] for i in range(1, N+1)}

for i in range(M):
    B, _, *I = map(int, input().split())
    bonus.append(B)
    for j in I:
        d[j].append(i)

ans = 0
for i in comb(range(1, N+1), 9):
    score = 0
    e = [0]*M
    for j in i:
        score += A[j-1]
        for k in d[j]:
            e[k] += 1
    for j, k in enumerate(e):
        if k>=3:
            score += bonus[j]
    ans = max(ans, score)

print(ans)