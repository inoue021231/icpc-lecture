while True:
    x, y, s = map(int, input().split())
    if (x, y, s) == (0, 0, 0):
        break
    answer = 0

    for i in range(1, s + 1):
        for j in range(i, s + 1):
            before_total = i + (i * x) // 100 + j + (j * x) // 100
            if before_total > s:
                break
            if before_total == s:
                after_total = i + (i * y) // 100 + j + (j * y) // 100
                if after_total > answer:
                    answer = after_total

    print(answer)
