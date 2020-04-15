from collections import deque

N = int(input())
d = {i:[] for i in range(1, N+1)}
q = deque([(1, "a")])

while q:
    pos, s = q.popleft()
    if pos == N+1:
        break
    d[pos].append(s)
    size = len(set(s))
    for i in range(size+1):
        q.append((pos+1, s+chr(97+i)))

for i in d[N]:
    print(i)