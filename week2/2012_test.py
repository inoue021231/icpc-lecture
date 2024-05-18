# pypy3

while True:
    e = int(input())
    if e == 0:
        break

    z = 0

    answer = e

    while z**3 <= e:
        y = 0
        while z**3 + y**2 <= e:
            x = e - z**3 - y**2
            if x + y + z < answer:
                answer = x + y + z
            y += 1
        z += 1
    print(answer)
