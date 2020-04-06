def get_lcs_table(s1, s2):
    l1, l2 = len(s1)+1, len(s2)+1
    dp = [[0]*l2 for _ in range(l1)]
    for i in range(l1):
        for j in range(l2):
            dp[i][j] = 0 if i==0 or j==0 else dp[i-1][j-1]+1 if s1[i-1]==s2[j-1] else max(dp[i][j-1], dp[i-1][j])
    return dp


def restore_lcs(s1, s2, dp):
    x, y = len(s1), len(s2)
    l = []
    while x and y:
        if dp[x][y] == dp[x-1][y]:
            x -= 1
        elif dp[x][y] == dp[x][y-1]:
            y -= 1
        else:
            x -= 1
            y -= 1
            l.append(s1[x])
    return "".join(l[::-1])


if __name__ == "__main__":
    s = input()
    t = input()
    dp = get_lcs_table(s, t)
    print(restore_lcs(s, t, dp))
