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
        ll m, n, count = 0;
        cin >> m >> n;
        if(m == 0 && n == 0) {
            break;
        }
        vector<ll> S;
        S.push_back(m);
        m++;
        while(count < n) {
            ll break_flag = 0;
            if(IsPrime(m)) {
                S.push_back(m);
                count++;
                m++;
                continue;
            }
            for(ll i = 0; i < S.size(); i++) {
                if(m % S[i] == 0) {
                    break_flag++;
                    break;
                }
            }
            if(break_flag == 0) {
                S.push_back(m);
                count++;
            }
            m++;
        }

        cout << S.back() << endl;
    }
    return 0;
}