from operator import add
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline


class SegTree():
    def __init__(self, N, e, operator_func=add):
        self.e = e # 単位元
        self.size = N
        self.node = [self.e] * (2*N)
        self.operator_func = operator_func # 処理(add or xor max minなど)

    def set_list(self, l):
        for i in range(self.size):
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = self.operator_func(self.node[2*i+1], self.node[2*i+2])
    
    def update(self, k, x):
        k += self.size-1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self.operator_func(self.node[2*k+1], self.node[2*k+2])

    def get(self, l, r):
        # [l, r) についてqueryを求める
        x = self.e
        l += self.size
        r += self.size
        a, b = [], []

        while l<r:
            if l&1:
                a.append(l-1)
                l += 1
            if r&1:
                r -= 1
                b.append(r-1)
            l >>= 1
            r >>= 1

        # 交換則をみたさないときのために
        for i in a+(b[::-1]):
            x = self.operator_func(x, self.node[i])

        return x

def op(s, t):
    a, b = s
    c, d = t
    return (a*c, b*c+d)

if __name__ == "__main__":
    N, M = map(int, input().split())

    e = (1, 0)
    max_value = 1.0
    min_value = 1.0
    d = defaultdict(int)

    q = []
    for _ in range(M):
        p, a, b = input().split()
        p = int(p)
        a = float(a)
        b = float(b)
        d[p] += 1
        q.append((p, a, b))
    
    size = len(d.keys())
    tree = SegTree(size, e, op)
    kp = {j:i for i,j in enumerate(sorted(d.keys()))}

    for p, a, b in q:
        tree.update(kp[p], (a, b))
        s, t = tree.get(0, size)
        max_value = max(max_value, s+t)
        min_value = min(min_value, s+t)

    print(min_value)
    print(max_value)