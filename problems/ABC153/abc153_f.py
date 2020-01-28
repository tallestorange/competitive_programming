import bisect

N, D, A = map(int, input().split())
X, H = zip(*sorted(list(map(int, input().split())) for _ in range(N)))
ans = 0
p = 0
t = 0

while t < N and p <= N:
    p = bisect.bisect_left(X, X[t]+2*D+1)
    print(H[t:p])
    m = max(H[t:p])

    ans += (m+A-1)//A
    t = p