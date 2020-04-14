#include <bits/stdc++.h>
using namespace std;

int dp[1000][1000] = {0};
char s[1000];

int main() {
    int H, W;
    scanf("%d %d", &H, &W);
    
    for(int i=0;i<H;i++) {
        scanf("%s", s);
        for(int j=0;j<W;j++) {
            if(s[j]=='#') {
                dp[i][j] = 1;
            }
        }
    }
    return 0;
}