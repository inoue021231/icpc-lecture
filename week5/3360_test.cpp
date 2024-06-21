#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  while(true) {
    ll N, D;
    cin >> N >> D;
    if(N == 0 && D == 0) {
      break;
    }

    vector<pair<ll,ll>> S(N);

    for(ll i = 0; i < N; i++) cin >> S[i].first >> S[i].second;

    sort(S.begin(), S.end());

    if(N == 1) {
      ll ans = 0;
      for(ll i = 0; i < D; i++) {
        ans += S[0].first - S[0].second * i;
      }
      cout << ans << endl;
    } else {
      ll ans = 0;

      ll a_max_1 = S.back().first;
      ll b_max = S.back().second;
      ll a_max_2 = S[N-2].first;

      ll a_pair = a_max_1 + a_max_2;
     
      for(ll i = 0; i * 2 <= D; i++) {
        ll buff = a_pair * i;
        ll d = D - i * 2;
        buff += a_max_1 * d - (d - 1) * d / 2 * b_max; 
        ans = max(buff, ans);
      }
      cout << ans << endl;
    }
  }
  return 0;
}