while True:
  n = int(input())
  if n == 0:
    break
  k = list(map(int, input().split()))
  s = list(map(ord, list(input())))
  index = 0
  for i in range(len(s)):
    for j in range(k[index]):
      if s[i] == 65:
        s[i] = 122
      elif s[i] == 97:
        s[i] = 90
      else:
        s[i] -= 1
    
    if index == n - 1:
      index = 0
    else:
      index += 1
  answer = ''.join(map(chr, s))
  print(answer)