def lcs_length(s1, s2):
    l1, l2 = len(s1)+1, len(s2)+1
    dp = [[0]*l2 for _ in range(l1)]
    for i in range(l1):
        for j in range(l2):
            dp[i][j] = 0 if i==0 or j==0 else dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

N = int(input())
S = input()
ans = N
for i in range(N+1):
    lcs = lcs_length(S[:i], S[i:])
    ans = min(ans, N-2*lcs)
print(ans)
