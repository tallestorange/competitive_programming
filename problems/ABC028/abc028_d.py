N, K = map(int, input().split())
a = 6*(K-1)*(N-K) + 3*(N-1) + 1
b = N**3
print(a/b)