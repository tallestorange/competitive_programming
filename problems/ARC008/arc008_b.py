from collections import Counter as c

N, M = map(int, input().split())
name = input()
kit = input()

s1 = set(name)
s2 = set(kit)
c1 = c(name)
c2 = c(kit)

if s1&s2==s1:
    l = []
    for i,j in c1.items():
        v = c2[i]
        l.append((j+v-1)//v)
    print(max(l))
else:
    print(-1)