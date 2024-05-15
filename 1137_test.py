n = int(input())
for i in range(n):
  num1, num2 = map(list,input().split())
  
  j = 0
  total = 0
  while j < len(num1):
    if num1[j] == 'm':
      if j == 0:
        total += 1000
      else:
        total += int(num1[j-1]) * 1000
      break
    j += 1 

  j = 0
  while j < len(num1):
    if num1[j] == 'c':
      if num1[j-1] == 'm' or num1[j-1] == 'c' or num1[j-1] == 'x' or num1[j-1] == 'i':
        total += 100
      else:
        total += int(num1[j-1]) * 100
      break
    j += 1 

  j = 0
  while j < len(num1):
    if num1[j] == 'x':
      if num1[j-1] == 'm' or num1[j-1] == 'c' or num1[j-1] == 'x' or num1[j-1] == 'i':
        total += 10
      else:
        total += int(num1[j-1]) * 10
      break
    j += 1 

  j = 0
  while j < len(num1):
    if num1[j] == 'i':
      if num1[j-1] == 'm' or num1[j-1] == 'c' or num1[j-1] == 'x' or num1[j-1] == 'i':
        total += 1
      else:
        total += int(num1[j-1])
      break
    j += 1 

  j = 0
  while j < len(num2):
    if num2[j] == 'm':
      if j == 0:
        total += 1000
      else:
        total += int(num2[j-1]) * 1000
      break
    j += 1 

  j = 0
  while j < len(num2):
    if num2[j] == 'c':
      if num2[j-1] == 'm' or num2[j-1] == 'c' or num2[j-1] == 'x' or num2[j-1] == 'i':
        total += 100
      else:
        total += int(num2[j-1]) * 100
      break
    j += 1 

  j = 0
  while j < len(num2):
    if num2[j] == 'x':
      if num2[j-1] == 'm' or num2[j-1] == 'c' or num2[j-1] == 'x' or num2[j-1] == 'i':
        total += 10
      else:
        total += int(num2[j-1]) * 10
      break
    j += 1 

  j = 0
  while j < len(num2):
    if num2[j] == 'i':
      if num2[j-1] == 'm' or num2[j-1] == 'c' or num2[j-1] == 'x' or num2[j-1] == 'i':
        total += 1
      else:
        total += int(num2[j-1])
      break
    j += 1

  i = total % 10
  total -= i
  x = total % 100
  total -= x
  c = total % 1000
  total -= c
  m = total
  x /= 10
  c /= 100
  m /= 1000
  
  m = int(m)
  c = int(c)
  x = int(x)
  i = int(i)

  answer = ""

  if m == 1:
    answer += 'm'
  elif m > 1:
    answer += str(m) + 'm'

  if c == 1:
    answer += 'c'
  elif c > 1:
    answer += str(c) + 'c'

  if x == 1:
    answer += 'x'
  elif x > 1:
    answer += str(x) + 'x'

  if i == 1:
    answer += 'i'
  elif i > 1:
    answer += str(i) + 'i'


  print(answer)