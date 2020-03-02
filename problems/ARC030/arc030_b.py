from collections import defaultdict

n, x = map(int, input().split())
*h, = map(int, input().split())
V = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)


def search(root, pos):
    q = [(root, pos)]
    while q:
        root, pos = q.pop()
        if h[pos-1]:
            return True
        for p in V[pos]:
            if p==root:continue
            q.append((pos, p))
    return False

def solve(root, pos):
    ans = 0
    q = [(root, pos)]
    while q:
        root, pos = q.pop()
        for p in V[pos]:
            if p==root:continue
            if search(pos, p):
                ans += 2
                q.append((pos, p))
    return ans

print(solve(0, x))
