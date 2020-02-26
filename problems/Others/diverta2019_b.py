R, G, B, N = map(int, input().split())
d = {i:0 for i in range(N+1)}

for i in range((N//G)+1):
    for j in range((N//B)+1):
        if i*G+j*B<=N:
            d[i*G+j*B] += 1

ans = 0
for i in range((N//R)+1):
    ans += d[N-(R*i)]
print(ans)