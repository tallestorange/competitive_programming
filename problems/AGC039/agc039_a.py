S = input()
K = int(input())
N = len(S)

bef = ""
start = 0
l = []
for i, s in enumerate(S):
    if bef=="":
        start = i
    elif bef!=s:
        l.append(i-start)
        start = i
    bef = s
l.append(i-start+1)

if len(set(S))==1:
    print((N*K)//2)
else:
    if S[0]==S[-1]:
        ans = (l[0]//2)+(l[-1]//2)+((l[0]+l[-1])//2)*(K-1)
    else:
        ans = (l[0]//2)*K+(l[-1]//2)*K
    for i in l[1:-1]:
        ans += (i//2)*K
    print(ans)
