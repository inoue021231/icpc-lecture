while True:
    words = list(input())
    if words[0] == '.':
        break
    
    miss_flag = False
    reset_flag = False

    i = 0

    while i < len(words):
        reset_flag = False
        if words[i] == '(':
            j = i + 1
            while j < len(words):
                if words[j] == ')':
                    del words[j]
                    del words[i]
                    i = 0
                    reset_flag = True
                    break
                elif words[j] == '[' or words[j] == '(':
                    reset_flag = True
                    i = j
                    break
                elif words[j] == ']':
                    miss_flag = True
                    break
                j += 1
        elif words[i] == '[':
            j = i + 1
            while j < len(words):
                if words[j] == ']':
                    del words[j]
                    del words[i]
                    i = 0
                    reset_flag = True
                    break
                elif words[j] == '[' or words[j] == '(':
                    i = j
                    reset_flag = True
                    break
                elif words[j] == ')':
                    miss_flag = True
                    break
                j += 1
        if reset_flag == False:
            i += 1

    if miss_flag or '(' in words or '[' in words or ')' in words or ']' in words:
        print('no')
    else:
        print('yes')
    