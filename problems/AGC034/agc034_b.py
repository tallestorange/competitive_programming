S = list(input())

size = len(S)
ans = 0

for _ in range(10):
    pos = 2
    print(S)
    while pos<size:
        s, t, u = S[pos-2], S[pos-1], S[pos]
        if s=="A" and t=="B" and u=="C":
            S[pos-2] = "B"
            S[pos-1] = "C"
            S[pos] = "A"
            ans += 1
            print(pos-2, pos-1, pos)
            pos += 2
        else:
            pos += 1