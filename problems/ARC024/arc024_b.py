N = int(input())
cl = [int(input()) for _ in range(N)]
chk = [0] * N

for i in range(N):
    if cl[(i-1)%N]==cl[i]==cl[(i+1)%N]:
        chk[i] = 1

if all(chk):
    print(-1)

else:
    v = 0
    s = 0
    p = []
    for i in range(N):
        if chk[i]:
            if v==0:
                s = i
            v += 1
        else:
            if v:
                p.append((s, v))
            v = 0
    if v:
        p.append((s, v))

    lng = max(p, key=lambda x:x[1])[1]
    if p[0][0] == 0 and v:
        lng = max(lng, p[0][1]+v)

    a, b = divmod(lng, 2)
    if b:
        print(a+2)
    else:
        print(a+1)