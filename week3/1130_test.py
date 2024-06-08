
def search_tile(tile, x, y, W, H):
  count = 1
  tile[y][x] = '#'
  if x >= 1 and tile[y][x-1] == '.':
    count += search_tile(tile, x-1, y, W, H)
  if x < W-1 and tile[y][x+1] == '.':
    count += search_tile(tile, x+1, y, W, H)
  if y >= 1 and tile[y-1][x] == '.':
    count += search_tile(tile, x, y-1, W, H)
  if y < H-1 and tile[y+1][x] == '.':
    count += search_tile(tile, x, y+1, W, H)
  return count

while True:
  W, H = map(int, input().split())
  if (W, H) == (0, 0):
    break

  x = 0
  y = 0

  tile = []
  for i in range(H):
    t = list(input())
    for j in range(W):
      if t[j] == '@':
        x = j
        y = i
    tile.append(t)
  
  ans = search_tile(tile, x, y, W, H)

  print(ans)