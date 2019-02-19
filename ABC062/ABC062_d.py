# ABC062
# https://atcoder.jp/contests/abc062/tasks/arc074_b

# 方針
# 数列のなかで左から1個目のものをx=1とする(1<=x<=3N)
# このとき点P(x=p,N<=p<=2N)をおき、pを動かして考える

# A = (a1,a2,a3..apの中から大きいものN個の和)
# B = (a(p+1),a(p+2)..a(3n)の中から小さいものN個の和) とすると
# 求めたいのは A-B
# pを動かしてA-Bの最大値を求めればそれが答えになる

# 愚直に実装するとO(N^2)であるためTLE

# プライオリティキューを用いることによりO(N)で実装できる
# pがインクリメントされる毎に
# A -> 一番小さい値をpop
# B -> 一番大きい値をpop すれば良い

from heapq import heappush,heappop

N=int(input())
*a,=map(int,input().split())
a=[0]+a

A,B=0,0
As,Bs=[None]*(3*N+1),[None]*(3*N+1)
l,r=[],[]

for p in range(1,N+1):
    heappush(l,a[p])
A=sum(l)
As[N]=A
for p in range(N+1,2*N+1):
    heappush(l,a[p])
    b=heappop(l)
    A=A+a[p]-b
    As[p]=A

for p in range(2*N+1,3*N+1)[::-1]:
    heappush(r,-a[p])
B=-sum(r)
Bs[2*N+1]=B
for p in range(N+1,2*N+1)[::-1]:
    heappush(r,-a[p])
    b=heappop(r)
    B=B+a[p]+b
    Bs[p]=B
    
ans=max(As[p]-Bs[p+1] for p in range(N,2*N+1))
print(ans)