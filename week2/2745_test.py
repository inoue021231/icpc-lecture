import math

while True:
    R0, W0, C, R = map(int, input().split())
    if (R0, W0, C, R) == (0, 0, 0, 0):
        break
    print(max(math.ceil((C * W0 - R0) / R), 0))
