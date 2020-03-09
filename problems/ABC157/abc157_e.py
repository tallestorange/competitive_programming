import sys
from operator import or_
input=sys.stdin.readline


class SegTree():
    def __init__(self, N, e=float("inf"), operator_func=min):
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


def main():
    N = int(input())
    S = list(input())[:-1]
    trees = {chr(97+i):SegTree(N, e=0, operator_func=or_) for i in range(26)}

    for i, s in enumerate(S):
        trees[s].update(i, 1)

    Q = int(input())
    for _ in range(Q):
        mode, i, v = input().split()
        if mode=="1":
            i = int(i)-1
            trees[S[i]].update(i, 0)
            trees[v].update(i, 1)
            S[i] = v
        else:
            i = int(i)-1
            v = int(v)
            ans = sum(trees[chr(97+j)].get(i, v) for j in range(26))
            print(ans)


if __name__ == "__main__":
    main()
