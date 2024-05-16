while True:
  N = int(input())
  if N == 0:
    break

  block_list = {
    0: [0,0]
  }

  for i in range(N-1):
    n, d = map(int, input().split())
    if d == 0:
      block_list[i+1] = [block_list[n][0]-1,block_list[n][1]]
    elif d == 1:
      block_list[i+1] = [block_list[n][0],block_list[n][1]+1]
    elif d == 2:
      block_list[i+1] = [block_list[n][0]+1,block_list[n][1]]
    elif d == 3:
      block_list[i+1] = [block_list[n][0],block_list[n][1]-1]

  block_list = list(block_list.values())
  w_list = [block[0] for block in block_list]
  h_list = [block[1] for block in block_list]
  w_answer = max(w_list) - min(w_list) + 1
  h_answer = max(h_list) - min(h_list) + 1
  print(w_answer, h_answer)