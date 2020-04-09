N, K, M, R = map(int, input().split())
l = [int(input()) for _ in range(N-1)]
l.sort(reverse=True)

if sum(l[:K])>=R*K:
    print(0)
else:
    v = R*K-sum(l[:K-1])
    print(v if v<=M else -1)
