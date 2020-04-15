N, K = map(int, input().split())
S = list(input())

l = []
bef = ""
start = 0

for i, s in enumerate(S):
    if bef=="":
        start = i
    elif bef!=s:
        l.append(i-start)
        start = i
    bef = s
l.append(i-start+1)

size = len(l)
ans = 0
for i in range(min(2*K+1, size)):
    ans += l[i]
ans -= 1
for i in range(min(2*K+1, size), size):
    ans += l[i]-1
print(ans)
