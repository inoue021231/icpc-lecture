while True:
    N = int(input())
    if N == 0:
        break
    A, B, C, D = map(int, input().split())
    x, y = map(int, input().split())
    goals = []
    for i in range(N):
        x1, y1 = map(int, input().split())
        goals.append([x1, y1])

    ans = 0

    for i in range(len(goals)):
        x1 = goals[i][0]
        y1 = goals[i][1]
        if (A <= x and x <= C and B <= y and y <= D) == False and (
            A <= x1 and x1 <= C and B <= y1 and y1 <= D
        ) == False:
            dis1 = abs(x1 - x) + abs(y1 - y)
            dis2 = -1
            if A > x:
                dis2 += A - x
            elif C < x:
                dis2 += x - C
            if B > y:
                dis2 += B - y
            elif D < y:
                dis2 += y - D
            if A > x1:
                dis2 += A - x1
            elif C < x1:
                dis2 += x1 - C
            if B > y1:
                dis2 += B - y1
            elif D < y1:
                dis2 += y1 - D
            ans += min(dis1, dis2)

        elif (A <= x and x <= C and B <= y and y <= D) == False:
            dis = -1
            if A > x:
                dis += A - x
            elif C < x:
                dis += x - C
            if B > y:
                dis += B - y
            elif D < y:
                dis += y - D
            ans += dis
        elif (A <= x1 and x1 <= C and B <= y1 and y1 <= D) == False:
            dis = 0
            if A > x1:
                dis += A - x1
            elif C < x1:
                dis += x1 - C
            if B > y1:
                dis += B - y1
            elif D < y1:
                dis += y1 - D
            ans += dis

        x = goals[i][0]
        y = goals[i][1]

    print(ans)
