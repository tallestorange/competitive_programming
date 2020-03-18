from collections import Counter

N = int(input())
S = input()
c = Counter(S)
print(c["R"]%2+c["G"]%2+c["B"]%2)