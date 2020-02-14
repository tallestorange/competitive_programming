N, L = map(int, input().split())
*a, = map(lambda x:L+x-1, range(1, N+1))
a.sort(key=abs)
print(sum(a)-a[0])