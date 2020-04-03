N = int(input())
S = input()
MOD = 1000000007

T = []
for _ in range(N):
    s = input()
    size = len(s)
    T.append((s, size))

lenS = len(S)
dp = [0] * (lenS+1)
dp[0] = 1

for i in range(lenS):
    for s, size in T:
        size = len(s)
        for j in range(i, i+size):
            if not 0 <= j < lenS or S[j] != s[j-i]:
                break
        else:
            dp[i+size] += dp[i]
            dp[i+size] %= MOD

print(dp[-1])
