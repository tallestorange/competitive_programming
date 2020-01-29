from collections import deque
H, W = map(int, input().split())
maze = [input() for _ in range(H)]


def bfs(x, y):
    visited, queue = [], deque([(x, y, 0)])
    max_cost = 0
    while queue:
        px, py, cost = queue.popleft()
        max_cost = max(max_cost, cost)

        candidate = ((px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1))
        visited.append((px, py))
        for cx, cy in candidate:
            if 0 <= cx < W and 0 <= cy < H and not (cx, cy) in visited and maze[cy][cx] == ".":
                queue.append((cx, cy, cost + 1))
    return max_cost


ans = 0
for y in range(H):
    for x in range(W):
        if maze[y][x] == ".":
            ans = max(ans, bfs(x, y))

print(ans)
