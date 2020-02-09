from heapq import heappush, heappop

N = int(input())
q = []

for i in map(int, input().split()):
    heappush(q, i)

for _ in range(N-1):
    a = heappop(q)
    b = heappop(q)
    c = (a+b)/2
    heappush(q, c)

ans = heappop(q)
print(ans)