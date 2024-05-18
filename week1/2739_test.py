N, M, T = map(int, input().split())
n = list(map(int, input().split()))

time = [0] * T

i = 0
while i < N:
  first = max(0,n[i] - M)
  end = min(T,n[i] + M)
  j = first
  while j < end:
    time[j] += 1
    j += 1
  i += 1

i = 0
answer = 0
while i < T:
  if time[i] == 0:
    answer += 1 
  i += 1

print(answer)
