n = int(input())
s = input()
ans = 0

for i in range(1000):
    t = str(i).zfill(3)
    isExists = [False]*3
    pos = 0
    for (p,j) in enumerate(t):
        while pos<n:
            if s[pos]==j:
                pos += 1
                isExists[p] = True
                break
            pos += 1
    if all(isExists):
        ans += 1

print(ans)