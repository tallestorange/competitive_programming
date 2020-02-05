N = int(input())
S = input()

l = [S[0]]
for s in S[1:]:
    if s!=l[-1]:
        l.append(s)

print(len(l))