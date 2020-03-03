class SegTree():
    def __init__(self, l, INF):
        self.inf = INF

        N = len(l)
        self.size = N
        self.node = [self.inf] * (2*self.size-1)
        for i in range(N): # 最下段を埋める
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = min(self.node[2*i+1], self.node[2*i+2]) # 上段の更新をする
    
    def update(self, k, x):
        k += self.size-1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = min(self.node[2*k+1], self.node[2*k+2])

    def get(self, l, r):
        x = self.inf
        l += self.size
        r += self.size

        while l<r:
            if l&1:
                x = min(x, self.node[l-1])
                l += 1
            if r&1:
                r -= 1
                x = min(x, self.node[r-1])
            l >>= 1
            r >>= 1
        return x

if __name__ == "__main__":
    l = [3, 4, 7, 4, 1, 9, 0, 1]
    tree = SegTree(l, 10**18)