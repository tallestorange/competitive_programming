S = input()
hs = sum(map(lambda x:ord(x)-96, S))

if hs == 1 or hs == 520:
    print("NO")

elif 495 <= hs < 520:
    t = chr(96+hs-494)
    u = "z"*19
    for i in range(20):
        s = u[:i]+t+u[i:]
        if s!=S:
            print(s)
            break
else:
    for i in range(1, min(hs, 26)+1):
        a, b = divmod(hs, i)
        s = chr(96+i)*a
        if b:
            s += chr(96+b)
        if len(s)<=20 and s!=S:
            print(s)
            break

