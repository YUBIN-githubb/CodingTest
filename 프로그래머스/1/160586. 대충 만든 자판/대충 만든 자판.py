def solution(keymap, targets):
    answer = []
    dict = {}
    for i in range (0,len(keymap)):
        for j in range (0,len(keymap[i])):
            if keymap[i][j] not in dict:
                dict[keymap[i][j]] = j+1
            else:
                if dict[keymap[i][j]] > j+1:
                    dict[keymap[i][j]] = j+1
    
    for i in range (0,len(targets)):
        answer.append(0)
        for j in range (0,len(targets[i])):
            num = dict.get(targets[i][j],"none")
            if num == "none":
                answer[i] = -1
                break
            else:
                answer[i] += num
    return answer