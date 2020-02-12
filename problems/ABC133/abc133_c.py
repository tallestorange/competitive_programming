L, R = map(int, input().split())

ans = 2018
for i in range(L, L+2019):
    for j in range(R-2019, R+1):
        if not i<j:
            continue
        ans = min(ans, (i*j)%2019)

print(ans)