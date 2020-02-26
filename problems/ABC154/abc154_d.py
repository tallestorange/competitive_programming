N, K = map(int, input().split())
*p, = map(int, input().split())

s = 0
for i in range(K):
    s += p[i]
ans = (K+s)/2

for i in range(K, N):
    s += p[i]
    s -= p[i-K]
    ans = max(ans, (K+s)/2)

print(ans)