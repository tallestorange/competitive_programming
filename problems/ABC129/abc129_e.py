S = input()
N = len(S)
mod = 10**9+7
ans = pow(2, S.count("1"), mod)

a = 0
for i, s in enumerate(S, start=1):
    if s=="1":
        a += 1
        ans += pow(2, a-1, mod)*pow(3, N-i, mod)
        ans %= mod

print(ans%mod)