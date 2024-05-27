while True:
    N = int(input())

    if N == 0:
        break

    words_list = []
    for _ in range(N):
        words_list.append(list(input()))

    # ソート結果の確認
    words_list.sort(key=len)

    index = 0
    answer = 0
    while index < N:
        same_length_list = [words_list[index]]
        
        while True:
            if index + 1 == N:
                break
            if len(words_list[index]) == len(words_list[index + 1]):
                same_length_list.append(words_list[index + 1])
                index += 1
            else:
                break


        if len(same_length_list) == 1:
            answer += len(same_length_list[0]) - 2
        else:
            for i in range(len(same_length_list)):
                j = 0
                while j < (len(same_length_list[i]) // 2 + 1):
                    flag = 0

                    for k in range(len(same_length_list)):
                        if k == i:
                            continue
                        if same_length_list[i][:j+1] == same_length_list[k][:j+1] and same_length_list[i][-(j+1):] == same_length_list[k][-(j+1):]:
                            flag = 1
                            break
                    
                    if flag == 0:
                        answer += len(same_length_list[i]) - 2 - j
                        break
                    
                    j += 1

        index += 1
    print(answer)
