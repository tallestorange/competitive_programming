N, M = map(int, input().split())

l = []
for i in range(1, int(M**0.5)+1):
    if M%i==0:
        l += [M//i]
        if M//i != i:
            l += [i]
l.sort()

for i in l:
    if i >= N:
        print(M//i)
        break