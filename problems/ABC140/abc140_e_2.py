class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
    def lower_bound(self, x):
        sum_ = 0
        pos = 0
        for i in range(self.depth + 1)[::-1]:
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_


N = int(input())
l = [(j, i) for i, j in enumerate(map(int, input().split()))]
l.sort(key=lambda x:-x[0])
tree = BIT(N)
ans = 0

for value, idx in l:
    v = tree.sum(idx + 1)

    a = tree.lower_bound(v - 1)[0] if v>1 else 0
    b = tree.lower_bound(v - 0)[0] if v else 0
    c = tree.lower_bound(v + 1)[0] 
    d = tree.lower_bound(v + 2)[0]

    tree.add(idx + 1, 1)
    idx += 1
    ans += ((b-a)*(c-idx)+(d-c)*(idx-b)) * value

print(ans)