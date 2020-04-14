N, M = map(int, input().split())
d = {1:-1, 2:-1, 3:-1}

for _ in range(M):
    s, c = map(int, input().split())
    if d[s]!=-1 and d[s]!=c:
        print(-1)
        break
    d[s] = c
else:
    for i in list(range(10**(N-1)-(N==1), 10**N)):
        n = i
        for j in range(1, N+1)[::-1]:
            if not (d[j] == -1 or d[j] == i%10):
                break
            i//=10
        else:
            print(n)
            break
    else:
        print(-1)
