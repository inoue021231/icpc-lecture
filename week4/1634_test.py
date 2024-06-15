import itertools


def find_min_common_element(matrix):
    if not matrix:
        return -1

    common_elements = set(matrix[0])

    for row in matrix[1:]:
        common_elements.intersection_update(row)

    if not common_elements:
        return -1

    return min(common_elements)


while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    total_w = []
    cannot_weigh_list = []

    for i in range(2, len(w) + 1):
        for c in itertools.combinations(w, i):
            total_w.append(sum(c))

    for i in range(n):
        can_weigh_flag = False
        for j in range(m):
            if a[i] == w[j]:
                can_weigh_flag = True
        if can_weigh_flag:
            continue

        for j in range(len(total_w)):
            if a[i] == total_w[j]:
                can_weigh_flag = True

        if can_weigh_flag:
            continue
        for j in range(1, len(w)):
            for c1 in itertools.combinations(w, j):
                another_w = list(set(w) - set(list(c1)))
                for k in range(1, len(another_w) + 1):
                    for c2 in itertools.combinations(another_w, k):
                        if sum(c1) + a[i] == sum(c2):
                            can_weigh_flag = True
        if can_weigh_flag:
            continue
        cannot_weigh_list.append(a[i])
    if len(cannot_weigh_list) == 0:
        print(0)
    else:
        answer_list = []
        for i in range(len(cannot_weigh_list)):
            weigh_list = set()
            weigh_list.add(cannot_weigh_list[i])
            for j in range(1, len(w) + 1):
                for c in itertools.combinations(w, j):
                    weigh_list.add(abs(cannot_weigh_list[i] - sum(c)))
            for j in range(0, len(w) + 1):
                for c1 in itertools.combinations(w, j):
                    another_w = list(set(w) - set(list(c1)))
                    for k in range(0, len(another_w) + 1):
                        for c2 in itertools.combinations(another_w, k):
                            weight = abs(sum(c1) + cannot_weigh_list[i] - sum(c2))
                            if weight > 0:
                                weigh_list.add(weight)
            sorted_list = list(weigh_list)
            answer_list.append(sorted_list)
        answer = find_min_common_element(answer_list)
        print(answer)
