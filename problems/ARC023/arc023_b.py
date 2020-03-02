R, C, D = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(R)]
c = [A[i][j] for i in range(R) for j in range(C) if i+j<=D and (D-(i+j))%2==0]
c.sort()
print(c[-1])