X, Y, Z, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
A.sort(reverse=True)

D = [i+j for j in C for i in B]
D.sort(reverse=True)
E = [i+j for j in D[:K] for i in A[:K]]
E.sort(reverse=True)

print(*E[:K], sep="\n")