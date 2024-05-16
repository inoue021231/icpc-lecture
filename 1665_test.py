while True:
  n, m, p, q = map(int, input().split())
  if (n,m,p,q) == (0,0,0,0):
    break
  lines = list(map(int, input().split()))

  index = p

  for i,line in enumerate(lines):
    if index == line:
      index += 1
    elif index == line + 1:
      index -= 1

  if index == q:
    print("OK")
    continue

  x = 1
  y = 0
  
  end_flag = False

  for i in range(m+1):
    for j in range(n):
      index = p
      test_lines = lines.copy()
      test_lines.insert(i,j+1)
      for _,line in enumerate(test_lines):
        if index == line:
          index += 1
        elif index == line + 1:
          index -= 1
      
      if index == q:
        print(j+1,i)
        end_flag = True
        break
    if end_flag:
      break
  if end_flag:
    continue
  print("NG")
