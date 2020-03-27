N = input()
size = len(N)
a, b = 0, 0

for i in range(1, size+1):
    v = int(N[-i])
    if i%2:
        a += v
    else:
        b += v

print(b, a)