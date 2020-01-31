N = int(input())
S, T = input().split()

s = ""
for a, b in zip(S, T):
    s += (a+b)
print(s)