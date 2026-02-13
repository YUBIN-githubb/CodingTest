def solution(name, yearning, photo):
    answer = []
    for i in range (0,len(photo)):
        score = 0
        for j in range (0, len(photo[i])):           
            if photo[i][j] in name:
                score += yearning[name.index(photo[i][j])]
        answer.append(score)
    return answer