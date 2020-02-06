from collections import defaultdict, deque

d = defaultdict(list)
N = int(input())
l = []

for _ in range(N-1):
    a, b = map(int, input().split())
    a-=1
    b-=1
    d[a].append(b)
    d[b].append(a)
    l.append((a,b))

parent = [0]*(N)
used = [False]*(N)
used[0]=True

q = deque()
q.append(0)
res = {}

max_n = 0
while q:
    p = q.popleft()
    color_num = 0
    for i in d[p]:
        if used[i]:continue

        used[i] = True
        
        color_num += 1
        # 根の値とかぶらない限り、1から小さい順に埋めるとよい
        if color_num == parent[p]:
            color_num+=1 # 根の値とかぶらないようにする
        parent[i] = color_num
        res[(p,i)] = color_num
        res[(i,p)] = color_num
        q.append(i)
    max_n = max(max_n, color_num)

print(max_n)
for i in l:
    print(res[i])