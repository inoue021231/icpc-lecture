while True:
    W, H, N, D, B = map(int, input().split())
    if (W, H, N, D, B) == (0, 0, 0, 0, 0):
        break

    field = [[0] * W for _ in range(H)]
    xy = []

    for _ in range(N):
        x, y = map(int, input().split())
        field[y - 1][x - 1] = 1
        xy.append([x - 1, y - 1])
    count = 0

    def bomb_clush(x, y):
        global count
        count += 1
        field[y][x] = 0
        for i in range(1, D + 1):
            if x + i < W:
                if field[y][x + i] == 1:
                    bomb_clush(x + i, y)
            if x - i >= 0:
                if field[y][x - i] == 1:
                    bomb_clush(x - i, y)
            if y + i < H:
                if field[y + i][x] == 1:
                    bomb_clush(x, y + i)
            if y - i >= 0:
                if field[y - i][x] == 1:
                    bomb_clush(x, y - i)

    bomb_clush(xy[B - 1][0], xy[B - 1][1])

    print(count)
