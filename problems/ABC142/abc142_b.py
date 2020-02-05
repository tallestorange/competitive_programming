N, K = map(int, input().split())
print(sum(map(lambda x:x>=K, map(int, input().split()))))