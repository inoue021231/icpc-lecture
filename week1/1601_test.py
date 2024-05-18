while True:
    N = int(input())
    if N == 0:
        break

    words = []
    for i in range(N):
        words.append(input())
    
    first_index = 0
    
    while True:
      index = first_index
      continue_flag = True

      word_total_len = 0
      while True:
        word_total_len += len(words[index])
        if word_total_len == 5:
          index += 1
          break
        elif word_total_len > 5:
          first_index += 1
          continue_flag = False
          break
        index += 1

      if continue_flag == False:
         continue
      
      word_total_len = 0
      while True:
        word_total_len += len(words[index])
        if word_total_len == 7:
          index += 1
          break
        elif word_total_len > 7:
          first_index += 1
          continue_flag = False
          break
        index += 1

      if continue_flag == False:
         continue
      
      word_total_len = 0
      while True:
        word_total_len += len(words[index])
        if word_total_len == 5:
          index += 1
          break
        elif word_total_len > 5:
          first_index += 1
          continue_flag = False
          break
        index += 1

      if continue_flag == False:
         continue
      
      word_total_len = 0
      while True:
        word_total_len += len(words[index])
        if word_total_len == 7:
          index += 1
          break
        elif word_total_len > 7:
          first_index += 1
          continue_flag = False
          break
        index += 1

      if continue_flag == False:
        continue
      
      word_total_len = 0
      while True:
        word_total_len += len(words[index])
        if word_total_len == 7:
          index += 1
          break
        elif word_total_len > 7:
          first_index += 1
          continue_flag = False
          break
        index += 1

      if continue_flag == False:
        continue
      print(first_index+1)
      break
      
      
      

    

    # print(words)
