from bisect import bisect_left

N, Q = map(int, input().split())
S = input()

ac_pos = []
p = 0
while p < N-1:
    if S[p]=="A" and S[p+1]=="C":
        ac_pos.append(p+1)
        p+=2
    else:
        p+=1

for _ in range(Q):
    l, r = map(int, input().split())
    p = bisect_left(ac_pos, l)
    q = bisect_left(ac_pos, r)
    print(q-p)