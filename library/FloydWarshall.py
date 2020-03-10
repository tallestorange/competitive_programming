import sys
input = sys.stdin.readline


def check(W):
    # false -> exist negative cycle
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if W[i][k]+W[k][j]+W[j][i]<0:
                    return False
                W[i][j] = min(W[i][j], W[i][k]+W[k][j])
    return True


if __name__ == "__main__":
    V, E = map(int, input().split())
    inf = float("inf")
    W = [[inf]*V for _ in range(V)]
    for i in range(V):
        W[i][i] = 0

    for _ in range(E):
        s, t, d = map(int, input().split())
        W[s][t] = d

    if check(W):
        for i in W:
            print(*(j if j!=inf else "INF" for j in i))
    else:
        print("NEGATIVE CYCLE")
