#include<bits/stdc++.h>
using namespace std;

int solve(int count, vector<vector<char>>& field, int H, int W) {
  if(count == 0) {
    return 1;
  }
  int cnt = 0;

  int x = -1;
  int y = -1;

  for(int i = 0; i < H; i++) {
    int break_flag = 0;
    for(int j = 0; j < W; j++) {
      if(field[i][j] == '.') {
        x = j;
        y = i;
        break_flag = 1;
        break;
      }
    }
    if(break_flag) {
      break;
    }
  }
  if(x == -1 && y == -1) {
    return 0;
  }

  if(x < W - 1 && y < H - 1) {
    if(field[y+1][x] == '.' && field[y+1][x+1] == '.') {
      field[y][x] = '#';
      field[y+1][x] = '#';
      field[y+1][x+1] = '#';
      cnt += solve(count - 3, field, H, W);
      field[y][x] = '.';
      field[y+1][x] = '.';
      field[y+1][x+1] = '.';
    }
  }

  if(x < W - 1 && y < H - 1) {
    if(field[y][x+1] == '.' && field[y+1][x+1] == '.') {
      field[y][x] = '#';
      field[y][x+1] = '#';
      field[y+1][x+1] = '#';
      cnt += solve(count - 3, field, H, W);
      field[y][x] = '.';
      field[y][x+1] = '.';
      field[y+1][x+1] = '.';
    }
  }

  if(x < W - 1 && y < H - 1) {
    if(field[y+1][x] == '.' && field[y][x+1] == '.') {
      field[y][x] = '#';
      field[y+1][x] = '#';
      field[y][x+1] = '#';
      cnt += solve(count - 3, field, H, W);
      field[y][x] = '.';
      field[y+1][x] = '.';
      field[y][x+1] = '.';
    }
  }

  if(x > 0 && y < H - 1) {
    if(field[y+1][x-1] == '.' && field[y+1][x] == '.') {
      field[y][x] = '#';
      field[y+1][x-1] = '#';
      field[y+1][x] = '#';
      cnt += solve(count - 3, field, H, W);
      field[y][x] = '.';
      field[y+1][x-1] = '.';
      field[y+1][x] = '.';
    }
  }

  return cnt;
}

int main() {
  while(true) {
    int H, W;
    cin >> H >> W;
    if(H == 0 && W == 0) {
      break;
    }
    vector<vector<char>> field(H, vector<char>(W));
    int count = 0;
    for(int i = 0; i < H; i++) {
      for(int j = 0; j < W; j++) {
        cin >> field[i][j];
        if(field[i][j] == '.') {
          count++;
        }
      }
    }

    cout << solve(count, field, H, W) << endl;
  }

  return 0;
}