from collections import deque

N = int(input())
l = [deque([])]+[deque(map(int, input().split())) for _ in range(N)]

v = 0
ans = 0
t = N*(N-1)//2

last_used = set(range(1, N+1))
while v<t and ans<t:
    used = set()
    for n in last_used:
        if n in used:continue
        if not l[n]:continue
        pair = l[n][0]
        b = l[pair][0]
        if pair in used:continue

        if b==n:
            l[n].popleft()
            l[pair].popleft()
            used|={n,pair}
            v += 1
    last_used = used
    ans += 1

if ans==t and ans!=v:
    print(-1)
else:
    print(ans)