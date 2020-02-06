from collections import Counter

N, K, Q = map(int ,input().split())
A = [int(input()) for _ in range(Q)]
c = Counter(A)

for i in range(1, N+1):
    print("Yes" if K-Q+c[i]>0 else "No")