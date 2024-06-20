#include<bits/stdc++.h>
using namespace std;

int solve(string s) {
  vector<int> split_s;

  if(isdigit(s[1])) {
    string num_str = "";
    for(int i = 1; i < s.length()-1; i++) num_str += s[i];
    int num = stoi(num_str) / 2 + 1;
    return num;
  }

  int pare_count = 0;

  int i = 1;
  while(i < s.length() - 1) {
    if(pare_count == 0 && s[i] == '[') {
      pare_count++;
      string new_s = "[";
      i++;
      while(true) {
        new_s += s[i];
        if(pare_count == 1 && s[i] == ']') {
          pare_count--;
          split_s.push_back(solve(new_s));
          break;
        } else if(s[i] == '[') {
          pare_count++;
        } else if(s[i] == ']') {
          pare_count--;
        }
        i++;
      }
    }

    i++;
  }

  int ans = 0;
  sort(split_s.begin(), split_s.end());

  for(int i = 0; i <= split_s.size() / 2; i++) {
    ans += split_s[i];
  }

  return ans;
}

int main() {
  int n;
  cin >> n;
  vector<string> S(n);
  for(int i = 0; i < n; i++) cin >> S[i];

  for(int i = 0; i < n; i++) cout << solve(S[i]) << endl;

  return 0;
}