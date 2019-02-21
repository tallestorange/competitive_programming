x=0
N=int(input())
S=[input() for _ in range(2)]
mod=10**9+7

l=[]
while x<N:
    if S[0][x]==S[1][x]:
        l.append(1)
        # たて
        x+=1
    else:
        l.append(0)
        # 横
        x+=2

v=1
for i,j in enumerate(l):
    if not i:
        v=3 if j else 6
    else:
        if l[i-1]:
            v*=2
        elif not j:
            v*=3
    v%=mod

print(v)