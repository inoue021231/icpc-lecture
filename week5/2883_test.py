def solve(s):

    if len(s) == 1:
        return s[0]

    i = 0

    while i < len(s):
        if s[i] == "]":
            v = 0
            if s[i - 3] == "+":
                v = s[i - 2] | s[i - 1]
            elif s[i - 3] == "*":
                v = s[i - 2] & s[i - 1]
            elif s[i - 3] == "^":
                v = s[i - 2] ^ s[i - 1]
            s.insert(i + 1, v)
            del s[i - 4 : i + 1]
            i = 0
            continue
        i += 1
    return s[0]


while True:
    s = list(input())
    if s[0] == ".":
        break
    num = input()

    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])

    num_list = {"a": a, "b": b, "c": c, "d": d}

    ss = s.copy()

    for i in range(len(ss)):
        if ss[i] == "a":
            ss[i] = a
        elif ss[i] == "b":
            ss[i] = b
        elif ss[i] == "c":
            ss[i] = c
        elif ss[i] == "d":
            ss[i] = d

    value = solve(ss)

    count = 0

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    ss = s.copy()
                    for m in range(len(s)):
                        if ss[m] == "a":
                            ss[m] = i
                        elif ss[m] == "b":
                            ss[m] = j
                        elif ss[m] == "c":
                            ss[m] = k
                        elif ss[m] == "d":
                            ss[m] = l
                    if value == solve(ss):
                        count += 1
    print(value, count)
