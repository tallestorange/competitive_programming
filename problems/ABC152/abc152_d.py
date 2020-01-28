# 125 521
# 1234 4531
# AxxxB ByyyyyyyA

# 1, 1
# x, x

N = int(input().split())
ans = 0

for n in range(1, N+1):
    a, b = str(n)[0], str(n)[-1]
    #10*b+a
