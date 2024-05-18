while True:
  n, r = map(int, input().split())
  if n == 0 and r == 0:
    break
  cards = sorted([i + 1 for i in range(n)], reverse=True)
  for i in range(r):
    p, c = map(int, input().split())
    buff = cards[p-1:p-1+c]
    del cards[p-1:p-1+c]
    cards = buff + cards
  print(cards[0])
