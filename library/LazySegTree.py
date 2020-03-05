class SegTree():
    def __init__(self, N, e=float("inf"), operator_func=min):
        self.e = e
        self.size = N
        self.node = [self.e] * (2 * N)
        self.lazy = [None] * (2 * N)
        self.op = operator_func

    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        for i in self.get_target_indexes(l, r):
            self.lazy[i] = self.node[i] = x

        for i in ids:
            self.node[i-1] = self.op(self.node[2*i-1], self.node[2*i])

    def gindex(self, l, r):
        L = l + self.size; R = r + self.size
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1
    
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue
            self.lazy[2*i-1] = self.node[2*i-1] = self.lazy[2*i] = self.node[2*i] = v
            self.lazy[i-1] = None

    def get_target_indexes(self, l, r):
        l += self.size; r += self.size
        a, b = [], []
        while l < r:
            if r & 1:
                r -= 1
                b += [r - 1]
            if l & 1:
                a += [l - 1]
                l += 1
            l >>= 1; r >>= 1
        
        return a + b[::-1]

    def query(self, l, r):
        self.propagates(*self.gindex(l, r))
        x = self.e
        
        for i in self.get_target_indexes(l, r):
            x = self.op(x, self.node[i])
        return x

if __name__ == "__main__":
    n = 10
    tree = SegTree(n)
