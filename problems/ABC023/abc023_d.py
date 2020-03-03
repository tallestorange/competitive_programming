N = int(input())
t = [tuple(map(int, input().split())) for _ in range(N)]

def can(x):
    m = sorted((x-h)//s for h, s in t)
    for i, j in enumerate(m):
        if j<0 or i>j:
            return False
    return True

l, r = 0, 10**15

while r-l>1:
    m = (l+r)//2
    if can(m):
        r = m
    else:
        l = m

print(r)