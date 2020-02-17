N = int(input())
*A, = map(int, input().split())
A.sort()

a, b, c = 0, 0, 0
for i in A:
    if i<0:
        a+=1
    elif i>0:
        c+=1
    else:
        b+=1

if b:
    ans = sum(map(abs, A))
elif c:
    for i,j in enumerate(A):
        if j>=0:break

    if a%2==0:
        ans = sum(map(abs, A))
    else:
        for i,j in enumerate(A):
            if j>=0:break
        ans = sum(map(abs, A)) - 2 * max(abs(A[i-1]), abs(A[i]))
else:
    if a%2 == 0:
        ans = sum(map(abs, A))
    else:
        ans = sum(map(abs, A[:-1]))+A[-1]

print(ans)