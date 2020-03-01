N = int(input())
l = [0]*N

for _ in range(N):
    w = int(input())
    for i,j in enumerate(l):
        if l[i]==0 or j>=w:
            l[i] = w
            break

print(N-l.count(0))