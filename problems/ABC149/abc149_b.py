A, B, K = map(int, input().split())

if A-K>=0:
    print(A-K, B)
elif A+B>=K:
    print(0, A+B-K)
else:
    print(0, 0)