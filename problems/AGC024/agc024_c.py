from itertools import accumulate

N = int(input())
A = [int(input()) for _ in range(N)]+[10**15]
bef = 0
l = [0]*(N+2)

for i,j in enumerate(A):
    if j!=bef:
        l[i] += 1
        if bef>=2:
            l[i-1] -= 1
            if j==0:
                l[i] -= 1
    bef = j

*p, = accumulate(l)
print(sum(p[:N]))