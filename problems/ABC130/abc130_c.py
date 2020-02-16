W, H, x, y = map(int, input().split())
print(W*H/2, 1 if W==x*2 and H==y*2 else 0)