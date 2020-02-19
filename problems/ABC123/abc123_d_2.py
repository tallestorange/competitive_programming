X, Y, Z, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
A.sort(reverse=True)

l = []
for i in B:
    for j in C:
        l.append(i+j)
l.sort(reverse=True)