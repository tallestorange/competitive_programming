N = int(input())
l = [(i,j) for i,j in enumerate(map(int, input().split()), start=1)]
print(*[i for i, j in sorted(l, key=lambda x:x[1])])