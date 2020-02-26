N, P = map(int, input().split())

def factorize(n):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(2, int(n**0.5)+1):
        while n%i==0:
            d[i] += 1
            n //= i
        if not n:
            break
    return d

d = factorize(P)
ans = 1
for i, j in d.items():
    ans *= (i ** (j//N))
print(ans if N!=1 else P)