#include <bits/stdc++.h>
using namespace std;

long long int a[3000] = {0};
int used[3000][3000] = {0};
long long int dp[3000][3000] = {0};

long long int f(int l, int r) {
    if (used[l][r]){
        return dp[l][r];
    }
    used[l][r] = 1;

    if (l==r){
        dp[l][r] = a[r];
    }
    else {
        dp[l][r] = max(a[l]-f(l+1,r), a[r]-f(l, r-1));
    }
    
    return dp[l][r];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int N;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> a[i];
    }
    cout << f(0, N-1) << endl;
    return 0;
}