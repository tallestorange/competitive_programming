N = int(input())
A, B = map(int, input().split())

if N<=A:
    print("Takahashi")
else:
    if A==B:
        # N-(A+1)に先に到達したほうが勝ち
        # 7 3 3 

        # ok
        # 5,6,7

        # ng 
        # 8,