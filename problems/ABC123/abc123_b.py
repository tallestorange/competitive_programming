from itertools import permutations as p
l = [int(input()) for _ in range(5)]

ans = 1000
for i in p(range(5)):
    v = 0
    for j,k in enumerate(i):
        if j!=4:
            if l[k]%10:
                v += (l[k] - l[k]%10 + 10)
            else:
                v += l[k]
        else:
            v += l[k]
    ans = min(ans, v)

print(ans)