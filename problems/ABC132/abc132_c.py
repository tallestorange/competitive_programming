N = int(input())
*d, = map(int, input().split())
d.sort()
print(d[N//2]-d[N//2-1])