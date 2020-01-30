H, W = map(int, input().split())
m = [list(input()) for _ in range(H)]
inf = 10**3

V = H*W
maze = [[inf]*V for _ in range(V)]

for i in range(V):
    maze[i][i] = 0

for py in range(H):
    for px in range(W):
        if m[py][px] == "#":
            continue
        candidate = [(px+1, py), (px-1, py), (px, py+1), (px, py-1)]
        for x, y in candidate:
            if not (0<=x<W and 0<=y<H):continue
            if m[y][x] == "#":
                continue
            maze[W*py+px][W*y+x] = 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            maze[i][j] = min(maze[i][j], maze[i][k]+maze[k][j])

print(max([j for i in maze for j in i if j!=inf]))