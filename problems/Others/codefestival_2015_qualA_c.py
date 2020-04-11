N, T = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x:-(x[0]-x[1]))

a = [0]*(N+1)
b = [0]*(N+1)

for i in range(N):
    a[i+1] = a[i] + l[i][1]
    b[N-i-1] = b[N-i] + l[N-i-1][0]

for i in range(N+1):
    if a[i]+b[i]<=T:
        print(i)
        break
else:
    print(-1)
