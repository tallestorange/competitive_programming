Q, L = map(int, input().split())
q = []
size = 0

for _ in range(Q):
    query = input().split()
    s = query[0]

    if s == "Push":
        n, m = map(int, query[1:])
        q.append((m, size+n))
        size += n

