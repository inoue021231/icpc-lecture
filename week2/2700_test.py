while True:
  n = int(input())
  if n == 0:
    break
  s = []
  for _ in range(n):
    ss = []
    words = list(input())
    ss.append(words[0])
    for index, word in enumerate(words):
      if index == len(words) - 1:
        break
      if word in 'aiueo':
        ss.append(words[index + 1])

    s.append(ss)
  
  k = 0
  while k < max([len(word) for word in s]):
    for i in range(len(s)):
      pass
    k += 1

  if k == max([len(word) for word in s]):
    print(-1)
  else:
    print(k)