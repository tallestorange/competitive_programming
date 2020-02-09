N = int(input())
print(sum(1 for i in range(1, N+1) if len(str(i))%2))