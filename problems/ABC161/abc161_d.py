from collections import deque


def solve():
    N = int(input())
    q = deque([1,2,3,4,5,6,7,8,9])
    cnt = 0
    l = []

    while cnt<N:
        p = q.popleft()
        l.append(p)
        cnt += 1
        for i in range(max((p%10)-1,0), min((p%10)+1, 9)+1):
            q.append(10*p+i)

    print(l[N-1])


if __name__ == "__main__":
    solve()
