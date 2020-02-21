from bisect import bisect_left
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]+[10**15]
t = [int(input()) for _ in range(B)]+[10**15]

for _ in range(Q):
    x = int(input())

    # x -> s -> t
    dist1, dist2 = 0, 0
    p1 = bisect_left(s, x)
    x1, x2 = s[p1-1], s[p1]
    dist1 += abs(x-x1)
    dist2 += abs(x-x2)

    p3 = bisect_left(t, x1)
    x3, x4 = t[p3-1], t[p3]
    dist1 += min(abs(x1-x3),abs(x1-x4))

    p3 = bisect_left(t, x2)
    x3, x4 = t[p3-1], t[p3]
    dist2 += min(abs(x2-x3),abs(x2-x4))

    dist_st = min(dist1, dist2)

    # x -> t -> s

    dist1, dist2 = 0, 0
    p1 = bisect_left(t, x)
    x1, x2 = t[p1-1], t[p1]
    dist1 += abs(x-x1)
    dist2 += abs(x-x2)

    p3 = bisect_left(s, x1)
    x3, x4 = s[p3-1], s[p3]
    dist1 += min(abs(x1-x3),abs(x1-x4))

    p3 = bisect_left(s, x2)
    x3, x4 = s[p3-1], s[p3]
    dist2 += min(abs(x2-x3),abs(x2-x4))

    dist_ts = min(dist1, dist2)

    print(min(dist_st, dist_ts))