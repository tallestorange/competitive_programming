from heapq import heappop, heappush

X, Y, Z, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
A.sort(reverse=True)

# Bi+Cjの和を求め、降順にソートしておく(Dkとします)
D = [i+j for j in C for i in B]
D.sort(reverse=True)

# Ai+Bj+Ckの大きい順からK個を構成する要素としては、Aiの大きい順からK個とDkの大きい順からK個しか登場しないので
q = []
for i in A[:K]:
    for j in D[:K]:
        heappush(q, -(i+j))

for _ in range(K):
    print(-heappop(q))