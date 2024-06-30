#include<bits/stdc++.h>
using namespace std;

int main() {
  while(true) {
    int N;
    cin >> N;
    if(N == 0) break;
    vector<string> s(N);
    vector<vector<pair<string, int>>> i18n_list(N);

    for(int i = 0; i < s.size(); i++) {
      cin >> s[i];
    }

    for(int i = 0; i < N; i++) {      
      for(int j = (int)s[i].size()-2; j >= 1; j--) {
        for(int k = 1; k <= (int)s[i].size()-1-j;k++) {
          string substr = s[i];
          substr.erase(k,j);
          substr.insert(k,to_string(j));
          i18n_list[i].push_back(make_pair(substr,j));
        }
      }
      i18n_list[i].push_back(make_pair(s[i],0));
    }

    int ans = 0;

    for(int i = 0; i < N; i++) {
      for(int ii = 0; ii < (int)i18n_list[i].size(); ii++) {
        int break_flag = 0;
        for(int j = 0; j < N; j++) {
          if(i == j) {
            continue;
          }
          for(int jj = 0; jj < (int)i18n_list[j].size(); jj++) {
            if(i18n_list[i][ii].first == i18n_list[j][jj].first) {
              break_flag = 1;
              break;
            }
          }
        }
        if(break_flag == 0) {
          ans += i18n_list[i][ii].second;
          break;
        }
      }
    }
   cout << ans << endl;
  }
  return 0;
}