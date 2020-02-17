from functools import reduce
from fractions import gcd

N = int(input())
*A, = map(int, input().split())

l_gcd = [0]*(N+2)
r_gcd = [0]*(N+2)

l_gcd[0] = A[0]
for i in range(1, N+1):
    l_gcd[i] = gcd(l_gcd[i-1], A[i-1])

r_gcd[N+1] = A[N-1]
for i in range(1, N+1)[::-1]:
    r_gcd[i] = gcd(r_gcd[i+1], A[i-1])

ans = 0
for i in range(1, N+1):
    if i==1:
        ans = max(ans, r_gcd[i+1])
    elif i==N:
        ans = max(ans, l_gcd[i-1])
    else:
        ans = max(ans, gcd(l_gcd[i-1], r_gcd[i+1]))

print(ans)