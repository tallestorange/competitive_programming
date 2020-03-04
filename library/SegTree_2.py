from operator import add


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

if __name__ == "__main__":
    n, q = map(int, input().split())
    tree = SegTree(n, 0, add)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com:
            print(tree.get(x, y+1))
        else:
            tree.update(x, y)