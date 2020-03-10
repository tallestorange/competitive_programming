#include <bits/stdc++.h>
using namespace std;

int dp[80][80][12801] = {0};
int C[80][80] = {0};

int main(){
    int H, W;
    scanf("%d %d", &H, &W);
    int b;

    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            scanf("%d", &b);
            C[i][j] += b;
        }
    }

    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            scanf("%d", &b);
            C[i][j] -= b;
            C[i][j] = abs(C[i][j]);
        }
    }

    int vmax = (H+W)*(80);
    dp[0][0][C[0][0]] = 1;

    int k1, k2;
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            for (int k=0;k<vmax+1;k++) {
                if (i+1<H) {
                    k1 = k+C[i+1][j];
                    k2 = abs(k-C[i+1][j]);
                    if (k1<=vmax) {
                        dp[i+1][j][k1] |= dp[i][j][k];
                    }
                    if (k2<=vmax) {
                        dp[i+1][j][k2] |= dp[i][j][k];
                    }
                }
                if (j+1<W) {
                    k1 = k+C[i][j+1];
                    k2 = abs(k-C[i][j+1]);
                    if (k1<=vmax) {
                        dp[i][j+1][k1] |= dp[i][j][k];
                    }
                    if (k2<=vmax) {
                        dp[i][j+1][k2] |= dp[i][j][k];
                    }
                }
            }
        }
    }

    int ans = 0;

    for (int i=0;i<vmax;i++) {
        if(dp[H-1][W-1][i]){
            printf("%d\n", i);
            break;
        }
    }
}