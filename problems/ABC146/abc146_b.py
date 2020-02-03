N = int(input())
S = input()
f=lambda x:chr(ord("A")+(ord(x)-ord("A")+N)%26)
print("".join(map(f, S)))