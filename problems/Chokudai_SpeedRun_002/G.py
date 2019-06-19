def gcd(a,b):
    if a<b:a,b=b,a
    if not b:return a
    return gcd(b,a%b)

N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    print(gcd(a,b))