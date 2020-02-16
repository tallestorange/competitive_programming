N, K = map(int, input().split())

amax = (N-1)*(N-2)//2
if amax-K>=0:
    print(amax-K+N-1)
    for i in range(N-1):
        print(1, i+2)
    cnt = 0

    def out(x):
        cnt = 0
        for i in range(2, N+1):
            for j in range(i+1, N+1):
                if cnt == amax-K:
                    return
                print(i, j)
                cnt += 1
    out(amax-K)
else:
    print(-1)