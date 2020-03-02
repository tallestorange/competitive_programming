#include <bits/stdc++.h>
using namespace std;
int A[1000][1000] = {0};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    vector<pair<int, int>> v;
    
    int R, C, D;
    cin >> R >> C >> D;

    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            cin >> A[i][j];

            if(i+j<=D){
                pair<int, int> p;
                p.first = A[i][j];
                p.second = i+j;
                v.push_back(p);
            }
        }
    }
    sort(v.begin(), v.end(), greater<pair<int, int>>());

    for(pair<int, int> p: v) {
        int d = D-p.second;
        if(d%2==0){
            cout << p.first << endl;
            break;
        }
    }

    return 0;
}