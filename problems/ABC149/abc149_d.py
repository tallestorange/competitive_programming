N, K = map(int, input().split())
R, S, P = map(int, input().split())
d = [[] for _ in range(K)]

for i, s in enumerate(input()):
    d[i%K].append(s)

ans = 0
score = {}
score["s"] = R
score["p"] = S
score["r"] = P

for l in d:
    prev_hand = "a"
    for s in l:
        if s!=prev_hand:
            ans += score[s]
            prev_hand = s
        else:
            prev_hand = "a"
print(ans)