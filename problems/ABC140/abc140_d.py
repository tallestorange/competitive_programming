N, K = map(int ,input().split())
S = input()

ans = 0
for i in range(N-1):
    if S[i]==S[i-1]:
        ans += 1

#

l = 0
while l<N:
    a = S[l]
    r = l+1
    while r<N:
        b = S[r]
