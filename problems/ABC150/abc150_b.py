N = int(input())
S = input()
print(sum(1 for i in range(N) if S[i:i+3]=="ABC"))
