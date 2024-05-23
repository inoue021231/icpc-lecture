import math

while True:
  D, E = map(int, input().split())

  if (D, E) == (0, 0):
    break
  
  answer = abs(D - E)

  for i in range(1, D):
    x = i
    y = D - i

    answer = min(answer, abs(math.sqrt(x ** 2 + y ** 2) - E))
  
  print(answer)