from collections import defaultdict, deque


def grouping(n, N, d):
    group = [-1]*(N+1)
    group[n] = 1

    q = deque([n])
    while q:
        s = q.popleft()
        for t in d[s]:
            if group[t]!=-1:continue
            group[t] = group[s] + 1
            q.append(t)

    for k, v in d.items():
        for j in v:
            if not abs(group[j]-group[k])==1:
                return False
    
    return group


def solve():
    N = int(input())
    d = defaultdict(list)
    for i in range(1, N+1):
        for j, s in enumerate(input(), start=1):
            if s=="1":
                d[i].append(j)
    

    ans = -1
    for i in range(1, N+1):
        res = grouping(i, N, d)
        if res != False:
            ans = max(ans, max(res))
    
    print(ans)

if __name__ == "__main__":
    solve()
