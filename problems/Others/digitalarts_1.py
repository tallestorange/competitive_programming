s = input().split()
N = int(input())
t = [input() for _ in range(N)]

ans = []
for i in s:
    for j in t:
        if len(i)!=len(j):
            continue
        res = [a==b or b=="*" for a,b in zip(i,j)]
        if all(res):
            ans.append("*"*len(i))
            break
    else:
        ans.append(i)

print(*ans)