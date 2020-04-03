from bisect import bisect_right
import sys
input=sys.stdin.readline


class LazySegTree():
    def __init__(self, N):
        self.INF = 2**31-1
        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.data = [0]*(2*self.N0)
        self.lazy = [0]*(2*self.N0)

    def gindex(self, l, r):
        L = (l + self.N0) >> 1; R = (r + self.N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()

        m = []
        for i in range(self.LV):
            if rc <= i:
                m.append(R)
            if L < R and lc <= i:
                m.append(L)
            L >>= 1; R >>= 1
        
        return m
    
    # 遅延伝搬処理
    def propagates(self, ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0

    # 区間[l, r)にxを加算
    def update(self, l, r, x):
        ids = self.gindex(l, r)
        self.propagates(ids)

        L = self.N0 + l; R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] += x; self.data[R-1] += x
            if L & 1:
                self.lazy[L-1] += x; self.data[L-1] += x
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.data[i-1] = max(self.data[2*i-1], self.data[2*i])
    
    # 区間[l, r)内の最小値を求める
    def query(self, l, r):
        self.propagates(self.gindex(l, r))
        L = self.N0 + l; R = self.N0 + r

        s = -self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = max(s, self.data[R-1])
            if L & 1:
                s = max(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    def set_list(self, l, N):
        for i in range(N):
            self.data[i+self.N0-1] = l[i]
        for i in range(self.N0-1)[::-1]:
            self.data[i] = max(self.data[2*i+1], self.data[2*i+2])


def solve():
    N, D, A = map(int, input().split())
    tree = LazySegTree(N)

    m, l = zip(*sorted(tuple(map(int, input().split())) for _ in range(N)))
    tree.set_list(l, N)

    ans = 0
    for i, j in enumerate(m):
        v = tree.query(i, i+1)
        if v>0:
            c = (v+A-1)//A
            ans += c
            pos = bisect_right(m, j+2*D)
            tree.update(i, pos, -c*A)

    print(ans)


if __name__ == "__main__":
    solve()
