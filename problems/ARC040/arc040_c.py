N = int(input())
l = [[0 if i=="." else 1 for i in input()] for _ in range(N)]

def ur():
    for i in range(N):
        for j in range(N)[::-1]:
            if l[i][j]==0:
                return (i, j)
    return (-1, -1)

ans = 0
while 1:
    y, x = ur()
    if x+y<0: break
    l[y] = [1]*(x+1)+l[y][x+1:]
    if y+1<N:
        l[y+1] = l[y+1][:x]+[1]*(N-x)
    ans += 1

print(ans)