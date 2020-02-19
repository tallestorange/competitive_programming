Q, H, S, D = map(int, input().split())
N = int(input())
m1 = min(Q*4, H*2, S)

if N%2:
    print(N//2*D+m1 if D < 2*m1 else N*m1)
else:
    print(N*min(Q*8, H*4, S*2, D)//2)