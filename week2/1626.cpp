#include<bits/stdc++.h>
using namespace std;

int main() {
    while (true) {
        int b;
        cin >> b;
        if (b == 0) {
            break;
        }

        int ans_count = 1;
        int ans_floor = b;

        for(int k = 2; 2*b > k*(k-1); k++) {
          if((-k*k+k+2*b) % (2*k) == 0 && (-k*k+k+2*b) / (2*k) > 0) {
            ans_count = k;
            ans_floor = (-k*k+k+2*b) / (2*k);
          }
        }

        cout << ans_floor << " " << ans_count << endl;
    }
    return 0;
}