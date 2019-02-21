N = int(input())
S = input()
l = []

for s in S:
    if not l:
        l.append(s)
    else:
        t=l[-1]
        if t=="(" and s==")":
            l.pop()
        else:
            l.append(s)

print("("*(l.count(")")) + S + ")"*(l.count("(")))