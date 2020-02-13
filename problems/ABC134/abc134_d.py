N = int(input())
a = [0] + list(map(int, input().split()))
ans = [False]*(N+1)

if N==1:
    if a[1]:
        print(1)
        print(1)
    else:
        print(0)
else:
    for i in range(2, N+1)[::-1]:
        for j in range(N):
            if j==0:
                ans[i] = a[i]
            else:
                if a[i] == a[i*2]:
                    ans[i] = 0
                else:
                    ans[i] = 1

            if i%2 or i==2:break
            else: i //= 2

    c = sum([1][2:])%2
    v = a[1]
    if c==v:
        ans[1] = 0
    else:
        ans[1] = 1

    M = sum(ans[1:])
    print(M)
    if M!=0:
        print(*(i for i,j in enumerate(ans[1:],start=1) if j))