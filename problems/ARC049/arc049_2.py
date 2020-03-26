def canmove(l, sec):
    left, right = -10**6, 10**6
    down, up = -10**6, 10**6
    
    for x, y, c in l:
        r = sec/c
        if left <= x-r < right <= x+r:
            left = x-r
        elif x-r <= left < x+r <= right:
            right = x+r
        elif x-r <= left < right <= x+r:
            pass
        elif left <= x-r < x+r <= right:
            left = x-r
            right = x+r
        else:
            return False

        if down <= y-r < up <= y+r:
            down = y-r
        elif y-r <= down < y+r <= up:
            up = y+r
        elif y-r <= down < up <= y+r:
            pass
        elif down <= y-r < y+r <= up:
            down = y-r
            up = y+r
        else:
            return False
        
    return True


if __name__ == "__main__":
    N = int(input())
    l = []

    for _ in range(N):
        x, y, c = map(int, input().split())
        l.append((x, y, c))

    s, t = 0, 10**9+1
    for i in range(50):
        m = (s+t)/2
        if canmove(l, m):
            t = m
        else:
            s = m

    print(t)