def solution(names):
    all = []
    group = []
    answer = []
    for i in range (0,len(names)):
        if len(group) < 5:
            group.append(names[i])
        elif len(group) == 5:
            all.append(group)
            group = []
            group.append(names[i])
    all.append(group)
    for i in range (0,len(all)):
        answer.append(all[i][0])
    return answer