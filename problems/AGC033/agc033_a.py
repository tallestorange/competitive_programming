from collections import deque


def solve():
    H, W = map(int, input().split())
    m = [[-1]*W for _ in range(H)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([])

    for i in range(H):
        s = input()
        for j in range(W):
            if s[j]=="#":
                q.append((i, j))
                m[i][j] = 0
    
    while q:
        y, x = q.popleft()
        for px, py in zip(dx, dy):
            x1, y1 = x + px, y + py
            if not (0<=x1<W and 0<=y1<H):
                continue
            if m[y1][x1] == -1:
                q.append((y1, x1))
                m[y1][x1] = m[y][x] + 1

    print(max(map(max, m)))


if __name__ == "__main__":
    solve()
