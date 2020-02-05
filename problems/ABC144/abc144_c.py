N = int(input())

ans = 10**20
for i in range(1, int(N**0.5)+1):
    if N%i==0:
        a, b = i, N//i
        ans = min(ans, a+b-2)

print(ans)