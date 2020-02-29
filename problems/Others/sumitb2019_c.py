X = int(input())
d = [0]*(X+1)
d[0] = 1

for i in range(100, X+1):
    d[i] = any(d[i-j] for j in (100, 101, 102, 103, 104, 105)) 

print(int(d[X]))
