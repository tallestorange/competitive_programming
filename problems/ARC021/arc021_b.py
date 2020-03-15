L = int(input())
B = [int(input()) for _ in range(L)]
A = [0] * L

for i, j in enumerate(B):
    A[(i+1)%L] = A[i%L]^j

if A[0]:
    print(-1)
else:
    print(*A, sep="\n")