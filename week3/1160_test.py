import sys

sys.setrecursionlimit(100000)


def visit(x, y, visited):
    global field, w, h
    visited.append([x, y])
    if x + 1 < w and field[y][x + 1] == 1 and [x + 1, y] not in visited:
        visit(x + 1, y, visited)
    if (
        x + 1 < w
        and y + 1 < h
        and field[y + 1][x + 1] == 1
        and [x + 1, y + 1] not in visited
    ):
        visit(x + 1, y + 1, visited)
    if y + 1 < h and field[y + 1][x] == 1 and [x, y + 1] not in visited:
        visit(x, y + 1, visited)
    if (
        x - 1 >= 0
        and y + 1 < h
        and field[y + 1][x - 1] == 1
        and [x - 1, y + 1] not in visited
    ):
        visit(x - 1, y + 1, visited)
    if x - 1 >= 0 and field[y][x - 1] == 1 and [x - 1, y] not in visited:
        visit(x - 1, y, visited)
    if (
        x - 1 >= 0
        and y - 1 >= 0
        and field[y - 1][x - 1] == 1
        and [x - 1, y - 1] not in visited
    ):
        visit(x - 1, y - 1, visited)
    if y - 1 >= 0 and field[y - 1][x] == 1 and [x, y - 1] not in visited:
        visit(x, y - 1, visited)
    if (
        y - 1 >= 0
        and x + 1 < w
        and field[y - 1][x + 1] == 1
        and [x + 1, y - 1] not in visited
    ):
        visit(x + 1, y - 1, visited)


while True:
    w, h = map(int, input().split())

    if (w, h) == (0, 0):
        break

    field = []

    for i in range(h):
        s = list(map(int, input().split()))
        field.append(s)
    count = 0
    while True:
        flag = 0
        break_flag = 0
        visited = []
        for i in range(h):
            for j in range(w):
                if field[i][j] == 1:
                    visit(j, i, visited)
                    for v in visited:
                        field[v[1]][v[0]] = 0
                    count += 1

        if flag == 0:
            break
    print(count)
