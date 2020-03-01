H, W = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(H)]
l = []

for h in range(H):
    for w in range(W-1):
        if d[h][w]%2:
            d[h][w+1] += 1
            d[h][w] -= 1
            l.append((h+1, w+1, h+1, w+2))

for h in range(H-1):
    if d[h][W-1]%2:
        d[h][W-1] -= 1
        d[h+1][W-1] += 1
        l.append((h+1, W, h+2, W))

print(len(l))
for i in l:
    print(*i)