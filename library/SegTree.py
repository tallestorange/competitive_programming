class SegTree():
    def __init__(self, l, INF):
        self.inf = INF

        N = len(l)
        v = 1
        while v<N:
            v *= 2

        self.size = v
        self.node = [self.inf] * (2*self.size-1)
        for i in range(N): # 最下段を埋める
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = self.node[2*i+1] + self.node[2*i+2] # 上段の更新をする

    def get(self, left, right, k=0, l=0, r=-1):
        if r < 0:
            r = self.size

        if (r <= left or right <= l):
            return self.inf
        if (left <= l and r <= right):
            return self.node[k]

        vl = self.get(left, right, 2*k+1, l, (l+r)//2)
        vr = self.get(left, right, 2*k+2, (l+r)//2, r)
        return vl + vr

    def update(self, x, v):
        x += self.size-1
        self.node[x] = v

        while x>0:
            x = (x-1)//2
            self.node[x] = self.node[2*x+1] + self.node[2*x+2]


if __name__ == "__main__":
    l = [3, 4, 7, 4, 1, 9, 0]
    tree = SegTree(l, 0)