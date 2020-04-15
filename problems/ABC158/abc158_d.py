from collections import deque
S = list(input())
Q = int(input())

dq1 = deque(S)
dq2 = deque(S[::-1])
isReversed = False

for _ in range(Q):
    l = input().split()
    if l[0] == "1":
        isReversed = not isReversed
    else:
        s = l[2]
        if l[1]=="1":
            if isReversed:
                dq1.append(s)
                dq2.appendleft(s)
            else:
                dq1.appendleft(s)
                dq2.append(s)
        else:
            if isReversed:
                dq1.appendleft(s)
                dq2.append(s)
            else:
                dq1.append(s)
                dq2.appendleft(s)

print("".join(dq2 if isReversed else dq1))
