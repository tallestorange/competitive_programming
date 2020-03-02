k = int(input())
l = [(k//50)+49]*50
v = k%50

for i in range(v):
    l[i] += 51-v
for j in range(v, 50):
    l[j] -= v

print(50)
print(*l)