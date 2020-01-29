N, K, M = map(int, input().split())
*A, = map(int, input().split())
score = N*M-sum(A)

if 0<score<=K:
    print(score)
elif score<=0:
    print(0)
else:
    print(-1)