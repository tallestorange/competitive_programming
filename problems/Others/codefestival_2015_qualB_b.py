from collections import Counter
N, M = map(int, input().split())
*A, = map(int, input().split())

m = Counter(A).most_common()[0]
print(m[0] if m[1]*2>N else "?")

