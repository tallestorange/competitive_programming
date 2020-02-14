from fractions import gcd

A, B, C, D = map(int, input().split())
E = (C*D)//gcd(C, D)

a = B//C-(A-1)//C
b = B//D-(A-1)//D
c = B//E-(A-1)//E
print(B-A+1-a-b+c)