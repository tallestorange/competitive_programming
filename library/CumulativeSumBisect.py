# Cumulative Sum Bisect


class SegTree():
    def __init__(self, N, e=0, operator_func=lambda x,y:x+y):
        self.e = e
        self.size = N
        self.node = [self.e] * (2*N)
        self.op = operator_func

    def set_list(self, l):
        for i in range(self.size):
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = self.op(self.node[2*i+1], self.node[2*i+2])
    
    def update(self, k, x):
        k += self.size - 1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self.op(self.node[2*k+1], self.node[2*k+2])

    def get(self, l, r):
        x = self.e
        l += self.size; r += self.size
        a, b = [], []

        while l<r:
            if l&1:
                a += [l-1]; l += 1
            if r&1:
                r -= 1; b += [r-1]
            l >>= 1; r >>= 1

        for i in a+(b[::-1]):
            x = self.op(x, self.node[i])
        return x

    def bisect_left(self, x):
        # O(log^2N)なので遅い
        left, right = 0, self.size
        while right-left>1:
            mid = (left+right)//2
            v = self.get(0, mid)
            if v >= x:
                right = mid
            else:
                left = mid
        return left+1


if __name__ == "__main__":
    # ABC140-E sample
    N = int(input())
    l = [(j, i) for i, j in enumerate(map(int, input().split()))]
    l.sort(key=lambda x:-x[0])
    tree = SegTree(N)

    ans = 0

    for n, (value, idx) in enumerate(l, start=1):
        v = tree.get(0, idx + 1)
        a = tree.bisect_left(v - 1) if v > 1 else 0
        b = tree.bisect_left(v - 0) if v else 0
        c = tree.bisect_left(v + 1) if n-v>1 else N+1
        d = tree.bisect_left(v + 2) if n-v>2 else N+1

        tree.update(idx, 1)
        idx += 1
        ans += ((b-a)*(c-idx)+(d-c)*(idx-b)) * value

    print(ans)