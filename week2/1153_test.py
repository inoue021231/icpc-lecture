while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    Sn = []
    Sm = []
    for _ in range(n):
        Sn.append(int(input()))
    for _ in range(m):
        Sm.append(int(input()))

    Sn.sort()
    Sm.sort()

    if abs(sum(Sn) - sum(Sm)) % 2 != 0:
        print(-1)
        continue

    diff = (sum(Sn) - sum(Sm)) / 2

    answer_total = 999999999999
    answer_n = -1
    answer_m = -1

    for i in range(n):
        for j in range(m):
            if Sn[i] - Sm[j] == diff:
                if answer_total > Sn[i] + Sm[j]:
                    answer_total = Sn[i] + Sm[j]
                    answer_n = Sn[i]
                    answer_m = Sm[j]

    if answer_total == 999999999999:
        print(-1)
    else:
        print(answer_n, answer_m)
