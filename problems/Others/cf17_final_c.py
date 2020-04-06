from itertools import product, combinations
from collections import Counter


def solve():
    N = int(input())
    *D, = map(int, input().split())

    l, m = [], []
    for i, j in Counter(D).items():
        if j>=3 or (i==12 and j>=2) or i==0:
            print(0)
            return
        elif j==2:
            l += [i]
        elif j==1:
            m += [i]

    size = len(m)
    ans = 0

    g = lambda x: min(x, 24-x)

    for i in product(range(2), repeat=size):
        c = [m[j] if k else 24-m[j] for j, k in enumerate(i)]
        f = lambda x, y: g(abs(c[x]-c[y]))
        for j in l:
            c.append(j)
            c.append(24-j)

        a = min(map(g, c))
        b = min(f(j, k) for j, k in combinations(range(N), 2))
        ans = max(ans, min(a, b))

    print(ans)

if __name__ == "__main__":
    solve()

