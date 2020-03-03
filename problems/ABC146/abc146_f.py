N, M = map(int, input().split())
S = input()[::-1]
l = []
p = 0

chk = True
while p<N:
    for i in range(1, min(M, N-p)+1)[::-1]:
        if S[p+i]=="0":
            break
    else:
        print(-1)
        chk = False
        break
    l.append(i)
    p += i

if chk:
    l.reverse()
    print(*l)