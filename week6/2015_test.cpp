#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    while (true) {
        ll N, M, ans = 0;
        cin >> N >> M;
        if (N == 0 && M == 0) {
            break;
        }
        vector<ll> h(N + 1, 0), w(M + 1, 0);
        vector<ll> hz(N + 1, 0), wz(M + 1, 0);

        for (ll i = 1; i <= N; i++) cin >> h[i];
        for (ll i = 1; i <= M; i++) cin >> w[i];

        for (ll i = 1; i <= N; i++) {
            hz[i] = hz[i - 1] + h[i];
        }

        for (ll i = 1; i <= M; i++) {
            wz[i] = wz[i - 1] + w[i];
        }

        unordered_map<ll, ll> sum_count_h;
        for (ll i = 1; i <= N; i++) {
            for (ll j = 0; j < i; j++) {
                sum_count_h[hz[i] - hz[j]]++;
            }
        }

        for (ll i = 1; i <= M; i++) {
            for (ll j = 0; j < i; j++) {
                ans += sum_count_h[wz[i] - wz[j]];
            }
        }

        cout << ans << endl;
    }
    return 0;
}
