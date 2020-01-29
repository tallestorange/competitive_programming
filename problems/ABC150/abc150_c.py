from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
a, b = 0, 0

for i, l in enumerate(permutations(range(1, N+1))):
    if l==P: 
        a = i
    if l==Q:
        b = i

print(abs(a-b))