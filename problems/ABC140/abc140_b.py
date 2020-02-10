N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())

d = {}
for i in A:
    d[i] = B[i-1]

before = -1
ans = 0
for i in A:
    ans+=d[i]
    if i-before==1:
        ans += C[i-2]
    before = i

print(ans)