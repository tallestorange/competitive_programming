from math import atan, degrees
a, b, x = map(int, input().split())

rad = atan(2*(b/a-x/(a**3))) if x>=(a**2)*b/2 else atan(a*(b**2)/2/x)
print(degrees(rad))