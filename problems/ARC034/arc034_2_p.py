N = int(input())

l = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            if 2*i+11*j+101*k==N:
                l.append(100*k+10*j+i)

print(len(l))
l.sort()
for i in l:
    print(i)