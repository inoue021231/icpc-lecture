#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int solve(vector<string> s) {
  int ans = 0;
  if(s.size() == 0) {
    return 0;
  }
  if(s[0][0] == '+') {
    vector<string> ss, sss;
    for(int i = 1; i < s.size(); i++) {
      if(s[i][1] == '.') {
        for(int j = 1; j < s[i].length();j++) {

        }
        ss.push_back(s[i]);
      } else if(s[i][1] == '+') {
        ans += solve(ss);
      } else if(s[i][1] == '*') {

      } else {
        ans += int(s[i][1]);
      }
    }
    ans += solve(ss);
  } else if(s[0][0] == '*') {
    
  }
  return 0;
}

int main() {
  while(true) {
    int n;
    cin >> n;
    if(n == 0) {
      break;
    }
    vector<string> S(n);
    for(int i = 0; i < n; i++) cin >> S[i];

    if(n == 1) {
      cout << S[0] << endl;
      continue;
    }

    for(int i = 0; i < n; i++) {
      cout << S[i] << endl;
    }
  }
  return 0;
}