from collections import Counter

S = input()
c = Counter(S)
print("Yes" if tuple(c.values()) == (2,2) else "No")