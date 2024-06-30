#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll solve(vector<string> s) {
  ll ans = 0;

  if(s.size() == 0) {
    return 0;
  }

  ll base_len = 1;
  
  if(s[0][0] == '+') {
    vector<string> ss, sss;
    ll i = 1;
    while(i < s.size()) {
      if(s[i][1] == '+' || s[i][1] == '*') {
        ll end_index = i+1;
        while(end_index < s.size()) {
          if(s[end_index].length() == 2) {
            break;
          }
          end_index++;
        }

        if(end_index >= s.size()) end_index--;

        for(ll j = i; j <= end_index; j++) {
          string ssss = "";
          for(ll k = 1; k < s[j].length(); k++) {
            ssss += s[j][k];
          }
          sss.push_back(ssss);
        }

        /* for(ll j = 0; j < sss.size(); j++) {
          cout << sss[j] << endl;
        } */
        i = end_index;
      } else {
        ans += int(s[i][1]);
        cout << s[i][1] << endl;
        i++;
      }
    }
    ans += solve(ss);
  } else if(s[0][0] == '*') {
    vector<string> ss, sss;
    ll i = 1;
    while(i < s.size()) {
      if(s[i][1] == '+' || s[i][1] == '*') {
        ll end_index = i+1;
        while(end_index < s.size()) {
          if(s[end_index].length() == 2) {
            break;
          }
          end_index++;
        }

        if(end_index >= s.size()) end_index--;

        for(ll j = i; j <= end_index; j++) {
          string ssss = "";
          for(ll k = 1; k < s[j].length(); k++) {
            ssss += s[j][k];
          }
          sss.push_back(ssss);
        }

        /* for(ll j = 0; j < sss.size(); j++) {
          cout << sss[j] << endl;
        } */
        i = end_index;
      } else {
        cout << s[i][1] << endl;
        ans *= int(s[i][1]);
        i++;
      }
    }
    ans *= solve(ss);
  }
  return ans;
}

int main() {
  while(true) {
    ll n;
    cin >> n;
    if(n == 0) {
      break;
    }
    vector<string> S(n);
    for(ll i = 0; i < n; i++) cin >> S[i];

    if(n == 1) {
      cout << S[0] << endl;
      continue;
    }

   /*  for(ll i = 0; i < n; i++) {
      cout << S[i] << endl;
    } */
    cout << solve(S) << endl;
  }
  return 0;
}