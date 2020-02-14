N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]

l.sort(key=lambda x:(x[1],-x[0]))
c = 0

for i,j in l:
    if c+i <= j:
        c += i
    else:
        print("No")
        break
else:
    print("Yes")