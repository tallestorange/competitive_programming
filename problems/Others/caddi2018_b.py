N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()

for i in range(N-1):
    a = l[i+1] - l[i]
    if a%2==0:
        l[i+1] -= a
        l[i] = 0
    elif l[i]%2:
        l[i] -= 1
    elif l[i+1]%2:
        l[i+1] -= 1

    
# if l[N-1]%2==0:
#     (N-2)%2
# else:
#     if l[N-2]%2:
