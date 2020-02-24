N = int(input())

l = []
for x in range(max(1, N-153), N+1):
    v, a = x, x
    while x:
        v += x%10
        x //= 10
    if v==N:
        l.append(a)

print(len(l))
for i in l:
    print(i)