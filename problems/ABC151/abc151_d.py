from collections import deque
import sys
import numpy as np

input = sys.stdin.readline
H, W = map(int, input().split())
maze = np.zeros((H, W), dtype='int')

for y in range(H):
    for x, s in enumerate(input()):
        if s=="#":
            maze[y][x] = 1


def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited = np.zeros_like(maze, dtype='int') 

    max_cost = 0
    while queue:
        px, py, cost = queue.popleft()
        max_cost = max(max_cost, cost)

        candidate = ((px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1))
        visited[py][px] = 1
        for cx, cy in candidate:
            if 0 <= cx < W and 0 <= cy < H and visited[cy][cx] == 0 and maze[cy][cx] == 0:
                queue.append((cx, cy, cost + 1))
    
    return max_cost


ans = 0
for y in range(H):
    for x in range(W):
        if maze[y][x] == 0:
            ans = max(ans, bfs(x, y))

print(ans)
