H, W, K = map(int, input().split())
ans = []
c = 1
v = 0

for _ in range(H):
    s = input()
    m = [-1]*W

    for i, j in enumerate(s):
        if j=="#":
            v += 1
            for k in range(i+1):
                if m[k]==-1:
                    m[k] = v
    if m[0]==-1:
        if ans:
            ans.append(ans[-1])
        else:
            c += 1
    else:
        for i in range(W):
            if m[i]==-1:
                m[i] = m[i-1]
        
        for _ in range(c):
            ans.append(m)
        c = 1

for i in ans:
    print(*i)
