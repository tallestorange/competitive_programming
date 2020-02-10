from functools import reduce
N = int(input())
*A, = map(int, input().split())

a = reduce(lambda x,y:x*y, A)
b = sum(map(lambda x:a//x,A))
print(a/b)