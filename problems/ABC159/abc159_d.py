from collections import Counter

N = int(input())
*l, = map(int, input().split())
c = Counter(l)

v = 0
for i in c.values():
    v += i*(i-1)//2

for i in l:
    print(v-(c[i]*(c[i]-1)//2)+((c[i]-1)*(c[i]-2)//2))