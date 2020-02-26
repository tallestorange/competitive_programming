from collections import Counter

N = int(input())
*a, = map(int, input().split())
c = Counter(a)
b = len(c.keys())

def check():
    if 0 in c.keys():
        if b==1 or (b==2 and c[0]==N//3):
            return True
    elif b==3:
        s, t, u = c.keys()
        if s^t^u==0 and c[s]==c[t]==c[u]:
            return True
    return False

print("Yes" if check() else "No")