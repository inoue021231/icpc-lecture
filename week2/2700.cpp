#include<bits/stdc++.h>
using namespace std;

int main() {
  while(true) {
    int n;
    cin >> n;
    if(n == 0) {
      break;
    }

    vector<string> S(n);
    for(int i = 0; i < n; i++) cin >> S[i];

    int max_len = 0;
    vector<string> codes(n);
    for(int i = 0; i < n; i++) {
      codes[i] += S[i][0];
      for(int j = 1; j < S[i].length(); j++) {
        if(S[i][j-1] == 'a' || S[i][j-1] == 'i' || S[i][j-1] == 'u' || S[i][j-1] == 'e' || S[i][j-1] == 'o') {
          codes[i] += S[i][j];
        }
      }
      max_len = max(max_len, int(codes[i].length()));
    }
    int ans = 0;
    while(ans <= max_len) {
      ans++;
      vector<string> test_codes;
      int break_flag = 1;
      for(int i = 0; i < codes.size(); i++) {
        test_codes.push_back(codes[i].substr(0,ans));
      }
      int i = 0;
      for(int i = 0; i < test_codes.size(); i++) {
        for(int j = i + 1; j < test_codes.size(); j++) {
          if(test_codes[i] == test_codes[j]) {
            break_flag = 0;
            break;
          }
        }
      }
      if(break_flag == 1) {
        break;
      }
    }
    if(ans == max_len+1) {
      cout << -1 << endl;
    } else {
      cout << ans << endl;
    }
  }
  return 0;
}