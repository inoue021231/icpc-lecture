#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool IsPrime(ll num) {
    if (num < 2) return false;
    else if (num == 2) return true;
    else if (num % 2 == 0) return false;

    double sqrtNum = sqrt(num);
    for (ll i = 3; i <= sqrtNum; i += 2) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    while(true) {
        ll n, n1, n2, ans = 0;
        cin >> n;
        if(n == 0) {
            break;
        }
        n1 = n + 1;
        n2 = 2 * n;
        for(ll i = n1; i <= n2; i++) {
            if(IsPrime(i)) {
                ans++;
            }
        }
        cout << ans << endl;
    }
    
    return 0;
}