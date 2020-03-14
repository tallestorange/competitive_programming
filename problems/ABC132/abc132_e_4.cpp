#include <bits/stdc++.h>
using namespace std;

int main() {
    queue<pair<int, int>> que;
    int N, M, u, v, S, T, dist;
    scanf("%d %d", &N, &M);
    vector<vector<int>> G(N+1);

    for(int i=0;i<M;i++) {
        scanf("%d %d", &u, &v);
        G[u].push_back(v);
    }
    scanf("%d %d", &S, &T);

    int used[N+1][3] = {0};
    pair<int, int> p = make_pair(S, 0);
    que.push(p);

    while (!que.empty()) {
        pair<int, int> p = que.front();
        que.pop();

        v = p.first;
        dist = p.second;
        used[v][dist%3] = 1;

        if(v==T && dist%3==0) {
            break;
        }

        for (int nv:G[v]) {
            if (used[nv][(dist+1)%3] != 0) {
                continue;
            }
            p = make_pair(nv, dist+1);
            que.push(p);
        }
    }

    if(v==T && dist%3==0) {
        printf("%d\n", dist/3);
    }
    else {
        printf("%d\n", -1);
    }
}