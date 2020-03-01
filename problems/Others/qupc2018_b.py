N = int(input())
for _ in range(N):
  a, b, c = map(int, input().split())
  if (100*a+10*b+c)%2:
    print("No")
  else:
    v = (100*a+10*b+c)//2
    
    a1 = min(v//100, a)
    b1 = min((v-100*a1)//10, b)
    c1 = min(v-100*a1-10*b1, c)
    
    d1 = 100*a1+10*b1+c1
    d2 = 100*(a-a1)+10*(b-b1)+(c-c1)
    print("Yes" if d1==d2 else "No")
