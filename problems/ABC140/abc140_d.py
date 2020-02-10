N, K = map(int ,input().split())
S = input()

ans = 0
for i in range(N-1):
    if S[i]==S[i-1]:
        ans += 1

l = 0
while l<N:
    a = S[l]
    r = l+2
    while r<N:
        b = S[r]
        if a!=b and S[r-1]!=b:
            if r+1<N:
                if S!=S[r+1]:
                    l = r - 1
                    ans += 1
                    break
                else:
                    r += 1
            else:
                l = r - 1
                ans += 1
                break
        else:
            r += 1
    l += 1