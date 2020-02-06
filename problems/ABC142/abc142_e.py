N, M = map(int, input().split())

l = []
ans = 0
for _ in range(M):
    a, b = map(int ,input().split())
    c = set(map(int ,input().split()))
    l.append([a/b, a, c])
l.sort(reverse=True)

selected = set()
inf = 10**8
while l and len(selected)!=N:
    perf, cost, treasures = l.pop()
    selected|=treasures
    ans += cost
    l = [i for i in l if i[2]&treasures!=i[2]]
    l.sort(reverse=True)

print(ans if selected == set(range(1, N+1)) else -1)