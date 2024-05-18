while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    
    key_list = {}
    answer_count = 0

    for i in range(h):
        r = list(input())
        for j, key in enumerate(r):
            key_list[key] = [i,j]
    
    s = list(input())
  
    x = 0
    y = 0

    for i in range(len(s)):
        answer_count += abs(x - key_list[s[i]][1]) + abs(y - key_list[s[i]][0]) + 1
        x = key_list[s[i]][1]
        y = key_list[s[i]][0]
    print(answer_count)
