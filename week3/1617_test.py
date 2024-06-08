while True:
  s1 = list(input())

  if len(s1) == 1 and s1[0] == '.':
    break
  s2 = list(input())
  if s1 == s2:
    print("IDENTICAL")
    continue

  if s1.count('"') != s2.count('"'):
    print("DIFFERENT")
    continue

  i = 0
  j = 0
  miss_count = 0

  while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
      miss_count = 2
      print("DIFFERENT")
      break
    if s1[i] == '"':
      i0 = i+1
      j0 = j+1
      i += 1
      j += 1
      while s1[i] != '"':
        i += 1
      while s2[j] != '"':
        j += 1
      if s1[i0:i] != s2[j0:j]:
        miss_count += 1
        if miss_count >= 2:
          print("DIFFERENT")
          break
    i += 1
    j += 1

  if (i >= len(s1) or j >= len(s2)) and miss_count >= 2:
    print("DIFFERENT")
  elif miss_count < 2:
    print("CLOSE")