from collections import Counter

N = int(input())
S = input()
ans = 0

for j in range(1, N-1):
    cl, cr = Counter(S[:j]), Counter(S[j+1:])
    
    for i in set(cl.keys())-set(S[j]):
        ans += cl[i]*(N-1-j-cr[S[j]]-cr[i])
            
    for i in range(1, min(j, N-1-j)+1):
        if S[j] != S[j-i] and S[j] != S[j+i] and S[j-i]!=S[j+i]:
            ans -= 1
    
print(ans)
