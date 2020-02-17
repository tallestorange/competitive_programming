from itertools import product as p

N = int(input())
*V, = map(int, input().split())
*C, = map(int, input().split())

ans = 0
for a in p(range(2), repeat=N):
    X, Y = 0, 0
    for i, j in enumerate(a):
        if j:
            X+=V[i]
            Y+=C[i]
    ans = max(ans, X-Y)
print(ans)