import sys
input=sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    d = {i:[] for i in range(1, N+1)}
    e = {i:[] for i in range(1, N+1)}
    h = [0] * (N+1)

    for _ in range(N+M-1):
        A, B = map(int, input().split())
        d[A].append(B)
        e[B].append(A)
        h[B] += 1

    st = set()
    for i in range(1, N+1):
        if h[i]==0:
            st.add(i)

    tp = {}
    c = 0
    while st:
        i = st.pop()
        c += 1
        tp[i] = c
        for j in d[i]:
            h[j] -= 1
            if h[j] == 0:
                st.add(j)

    ans = [0] * (N+1)
    for i in range(1, N+1):
        s, t = 0, 0
        for j in e[i]:
            if s < tp[j]:
                s = tp[j]
                t = j
        print(t)


if __name__ == "__main__":
    solve()
