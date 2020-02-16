N = int(input())
*W, = map(int, input().split())
ans = 10000

s = sum(W)
v = 0
for i in W:
    v += i
    ans = min(ans, abs(v-(s-v)))

print(ans)