while True:
    N = int(input())

    if N == 0:
        break

    words_list = []
    for _ in range(N):
        words_list.append(input())

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
                j = 1
                max_length = 0
                while j < len(same_length_list[i]):
                    flag = 0
                    k = j
                    while k < len(same_length_list[i]):
                        for l in range(len(same_length_list)):
                          if l != i and same_length_list[i][:j+1] == same_length_list[l][:j+1] and same_length_list[i][-(k+1):] == same_length_list[l][-(k+1):]:
                            flag = 1
                          print(i,j,k,l)
                        k += 1
                    if flag == 0:
                        max_length = max(max_length, k - j + 1)
                        break
                    j += 1
                answer += max_length
        index += 1
    print(answer)

'''
16
39
2
6
80
7237
7201
27223
26220
21411
9
'''
