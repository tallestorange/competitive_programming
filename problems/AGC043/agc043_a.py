def solve():
    H, W = map(int, input().split())
    l = [list(input()) for _ in range(H)]
    q = [(0, 0)]
    sc = [[H*W]*W for _ in range(H)]
    sc[0][0] = 0 if l[0][0]=="." else 1

    while q:
        y, x = q.pop()
        for y1, x1 in [(y+1, x), (y, x+1)]:
            if not (0<=x1<W and 0<=y1<H):continue
            if l[y][x]=="#":
                if sc[y1][x1] > sc[y][x]:
                    sc[y1][x1] = sc[y][x]
                    q.append((y1, x1))
            else:
                v = sc[y][x]+1 if l[y1][x1]=="#" else sc[y][x]
                if sc[y1][x1] > v:
                    sc[y1][x1] = v
                    q.append((y1, x1))

    print(sc[-1][-1])


if __name__ == "__main__":
    solve()