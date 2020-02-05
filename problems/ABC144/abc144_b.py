N = int(input())

for i in range(1, 10)[::-1]:
    if N%i==0:
        break

print("Yes" if 1<=i<=9 and 1<=N//i<=9 else "No")