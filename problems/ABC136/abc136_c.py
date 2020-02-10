N = int(input())
*H, = map(int, input().split())

m = H[0]
for i in H:
    if m-i>1:
        print("No")
        break
    m = max(m, i)
else:
    print("Yes")
