from heapq import heappush, heappop, heapify

N, M = map(int ,input().split())
q = []
for i in map(int ,input().split()):
    heappush(q, -i)

for _ in range(M):
    a = heappop(q)
    heappush(q, ((-a)//2)*-1)

print(-sum(q))