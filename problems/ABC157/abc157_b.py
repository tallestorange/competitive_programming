l = [tuple(map(int, input().split())) for _ in range(3)]
used = [[False]*3 for _ in range(3)]

N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if l[i][j]==b:
                used[i][j]=True

def check():
    if used[0][0] and used[1][1] and used[2][2]:
        return True
    if used[0][2] and used[1][1] and used[2][0]:
        return True
    for i in range(3):
        if used[i][0] and used[i][1] and used[i][2]:
            return True
        if used[0][i] and used[1][i] and used[2][i]:
            return True

print("Yes" if check() else "No")