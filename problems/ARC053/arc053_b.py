from collections import Counter
from itertools import zip_longest

s = input()
total = len(s)

kind = 0
for i in Counter(s).values():
    if i%2:
        kind += 1
print(1+(((total-kind)//2)//kind)*2 if kind else total)