from heapq import heappush, heappop

X, Y, Z, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

# x以上のものがK個あるならOK
def f(x):
    cnt = 0
    for i in A:
        for j in B:
            for k in C:
                if i+j+k<x:break
                cnt += 1
                if cnt>=K:
                    return True
    return False

def get_boarder():
    l, r = 0, A[0]+B[0]+C[0]
    while r-l>1:
        m = (l+r)//2
        if f(m):
            l = m
        else:
            r = m
    return l

boarder = get_boarder()
q = []
for i in A:
    for j in B:
        for k in C:
            if i+j+k<boarder:break
            heappush(q, -(i+j+k))

for _ in range(K):
    print(-heappop(q))