H, W = map(int, input().split())

dw = [[0]*W for _ in range(H)]
dh = [[0]*W for _ in range(H)]
maze = [[0]*W for _ in range(H)]

for h in range(H):
    s = input()
    c = 0
    for w, ss in enumerate(s):
        maze[h][w] = ss
        if ss == ".":
            c += 1
            dw[h][w] = c
        else:
            c = 0

for w in range(W):
    c = 0
    for h in range(H):
        ss = maze[h][w]
        if ss == ".":
            c += 1
            dh[h][w] = c
        else:
            c = 0

for h in range(H):
    m = 0
    for w in range(W)[::-1]:
        if dw[h][w] == 0:
            m = 0
        else:
            m = max(m, dw[h][w])
            dw[h][w] = m

for w in range(W):
    m = 0
    for h in range(H)[::-1]:
        if dh[h][w] == 0:
            m = 0
        else:
            m = max(m, dh[h][w])
            dh[h][w] = m

ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, dh[h][w]+dw[h][w]-1)

print(ans)