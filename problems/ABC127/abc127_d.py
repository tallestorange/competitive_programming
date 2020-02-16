N, M = map(int, input().split())
*A, = map(int, input().split())
A.sort()

l = []
for _ in range(M):
    B, C = map(int, input().split())
    l.append((B, C))
l.sort(key=lambda x:-x[1])

def solve():
    p = 0
    ans = 0
    for i, j in l:
        for _ in range(i):
            ans += max(A[p], j)
            p += 1
            if N==p:
                return ans
    
    for i in range(p, N):
        ans += A[i]
    return ans
    
print(solve())