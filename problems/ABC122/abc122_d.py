N = int(input())
d = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
d[0][0][0][0] = 1
mod = 10**9+7

# T -> 0
# A -> 1
# G -> 2
# C -> 3 とする

# 先頭の文字をi、先頭から2番めの文字をj、先頭から3番目の文字をkとなるような
# 場合の数をDPテーブルで管理する
# dp[n][i][j][k] += dp[n-1][j][k][l]

# 新しく文字を追加したとき、
# 先頭4文字が以下のようにならないようにしたい
# AGC*, ACG*, GAC*, AG*C, A*GC 

# j,k,lがこれらのときアウト
# AGC -> 123 -> 321
# ACG -> 132 -> 231
# GAC -> 213 -> 312

# j,k,l,mがこれらのときアウト
# AG*C -> 12*3 -> 3*21
# A*GC -> 1*23 -> 32*1

for i in range(1, N+1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):

                    if j==3 and k==2 and l==1:continue
                    elif j==2 and k==3 and l==1:continue
                    elif j==3 and k==1 and l==2:continue
                    elif j==3 and k==2 and m==1:continue
                    elif j==3 and l==2 and m==1:continue

                    d[i][j][k][l] += d[i-1][k][l][m]
                    d[i][j][k][l] %= mod

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += d[N][i][j][k]
            ans %= mod

print(ans)