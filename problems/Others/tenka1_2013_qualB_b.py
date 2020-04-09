from bisect import bisect_right
import sys
input=sys.stdin.readline

Q, L = map(int, input().split())
pos = 0
l = [input().split() for _ in range(Q)]

for s in l:
    com = s[0]
    if com=="Top":
        if pos-1<0:
            print("EMPTY")
            break
        print(tree.query(pos-1, pos))
    elif com=="Size":
        print(pos)
    elif com=="Push":
        n, m = int(s[1]), int(s[2])
        if pos+n>L:
            print("FULL")
            break
        tree.update(pos, pos+n, m)
        pos += n
    elif com=="Pop":
        n = int(s[1])
        if pos-n<0:
            print("EMPTY")
            break
        tree.update(pos-n, pos, 0)
        pos -= n
else:
    print("SAFE")