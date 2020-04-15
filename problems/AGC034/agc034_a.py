N, A, B, C, D = map(int, input().split())
S = input()


def dfs(start, end):
    q = [start-1]
    while q:
        s = q.pop()
        if s==end-1:
            return True
        if s+2<N and S[s+2]==".":
            q.append(s+2)
        if s+1<N and S[s+1]==".":
            q.append(s+1)
    return False


res = dfs(A, C) and dfs(B, D)

if C<D:
    print("Yes" if res else "No")
else:
    #A<B<D<C
    for i in range(B-1, D):
        if S[i-1]=="." and S[i]=="." and S[i+1]==".":
            print("Yes" if res else "No")
            break
    else:
        print("No")
