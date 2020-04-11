X, Y, A, B, C = map(int, input().split())
*p, = map(int, input().split())
*q, = map(int, input().split())
*r, = map(int, input().split())

p.sort(reverse=True)
q.sort(reverse=True)

l = p[:X]+q[:Y]+r
l.sort(reverse=True)
print(sum(l[:X+Y]))