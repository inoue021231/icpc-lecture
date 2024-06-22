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
        ll N, P;
        vector<ll> S, Z;
        cin >> N >> P;
        if(N == -1 && P == -1) {
            break;
        }
        ll count = P + 1;
        ll i = N+1;
        while(count > 0) {
            if(IsPrime(i)) {
                S.push_back(i);
                count--;
            }
            i++;
        }
        for(ll i = 0; i < S.size(); i++) {
            for(ll j = i; j < S.size(); j++) {
                Z.push_back(S[i] + S[j]);
            }
        }

        sort(Z.begin(), Z.end());

        cout << Z[P-1] << endl;
    }
    return 0;
}