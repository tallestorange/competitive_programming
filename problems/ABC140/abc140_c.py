N = int(input())
inf = 10**10
*a, = map(int ,input().split())
b = [inf]+a+[inf]
print(sum(min(b[i], b[i+1]) for i in range(N)))