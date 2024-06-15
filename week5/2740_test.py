def solve(a, b):
    if (
        len(a) == 0
        or len(b) == 0
        or (len(a) == 2 and a[0] == "(" and a[1] == ")")
        or (len(b) == 2 and b[0] == "(" and b[1] == ")")
    ):
        return ""
    root_a_value = -1
    root_a_left = []
    root_a_right = []

    i = 1
    pare_count = 1
    while i < len(a):
        if pare_count == 0 and a[i] == "[":
            j = 1
            v = a[i + j]
            while True:
                if a[i + j + 1].isdigit():
                    j += 1
                    v += a[i + j]
                else:
                    break
            root_a_value = int(v)
            root_a_left = a[1 : i - 1]
            root_a_right = a[i + j + 3 : len(a) - 1]
            break
        elif a[i] == "(":
            pare_count += 1
        elif a[i] == ")":
            pare_count -= 1
        i += 1

    root_b_value = -1
    root_b_left = []
    root_b_right = []

    i = 1
    pare_count = 1

    while i < len(b):
        if pare_count == 0 and b[i] == "[":
            j = 1
            v = b[i + j]
            while True:
                if b[i + j + 1].isdigit():
                    j += 1
                    v += b[i + j]
                else:
                    break
            root_b_value = int(v)
            root_b_left = b[1 : i - 1]
            root_b_right = b[i + j + 3 : len(b) - 1]
            break
        elif b[i] == "(":
            pare_count += 1
        elif b[i] == ")":
            pare_count -= 1
        i += 1

    return (
        "("
        + solve(root_a_left, root_b_left)
        + ")["
        + str(root_a_value + root_b_value)
        + "]("
        + solve(root_a_right, root_b_right)
        + ")"
    )


A = list(input())
B = list(input())

value = solve(A, B)

print(value)
