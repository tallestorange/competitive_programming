N, M = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
A.sort(reverse=True)
B.sort(reverse=True)

if N<M:
    print("NO")
else:    
    print("YES" if all(i>=j for i, j in zip(A, B)) else "NO")

