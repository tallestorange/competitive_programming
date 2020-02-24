N = int(input())
ans = 1
*a, = map(int, input().split())
mod = 10**9+7

l = [[0,0,0] for _ in range(N+1)]
r, g, b = 0, 0, 0

for i, j in enumerate(a):
    if i:
        if j==0:
            if g==0:
                g += 1
            else:
                b += 1
        else:
            if r==j:
                r += 1
            elif g==j:
                g += 1
            elif b==j:
                b += 1
    else:
        r += 1
     
    l[i+1][0] = r
    l[i+1][1] = g
    l[i+1][2] = b

ans = 1
for i,j in zip(a, l):
    ans *= j.count(i)
    ans %= mod

print(ans)