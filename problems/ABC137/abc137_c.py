from collections import defaultdict

N = int(input())
d = defaultdict(int)

for _ in range(N):
    d[tuple(sorted(input()))]+=1

ans = 0
for i in d.values():
    if i==1:continue
    ans += i*(i-1)//2

print(ans)