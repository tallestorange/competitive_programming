from collections import Counter as c

S1 = input()
S2 = input()
S3 = input()
N = len(S1)//2

c1, c2, c3 = c(S1), c(S2), c(S3)
a, b = 0, 0

for i in range(26):
    s = chr(65+i)
    a += max(0, c3[s]-c2[s])
    b += min(c1[s], c3[s])

print("YES" if a<=N<=b else "NO")