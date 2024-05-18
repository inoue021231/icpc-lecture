while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    a = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] <= m and answer < a[i] + a[j]:
                answer = a[i] + a[j]

    if answer == 0:
        print("NONE")
    else:
        print(answer)
