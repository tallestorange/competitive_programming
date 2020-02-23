N, M = map(int, input().split())

am = [list(map(int, input())) for _ in range(N)]
before = [[0]*M for _ in range(N)]

for i in range(1, N-1):
    for j in range(1, M-1):
        v = min(am[i-1][j], am[i+1][j], am[i][j+1], am[i][j-1])
        if v:
            am[i-1][j] -= v
            am[i+1][j] -= v
            am[i][j+1] -= v
            am[i][j-1] -= v
            before[i][j] = v

for i in before:
    print(*i, sep="")