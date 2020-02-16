N = int(input())
l = []

for i in range(N):
    s, p = input().split()
    l.append((s, int(p), i+1))

l.sort(key=lambda x:(x[0],-x[1]))
for _, _, i in l:
    print(i)