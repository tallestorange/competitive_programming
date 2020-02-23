C = int(input())
N, M, L = zip(*[sorted(map(int, input().split())) for _ in range(C)])
print(max(N)*max(M)*max(L))