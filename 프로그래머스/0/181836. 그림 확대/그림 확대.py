def solution(picture, k):
    answer = []
    for i in range (0,len(picture)):
        str = ""
        for j in range (0,len(picture[i])):
            char = ""
            for p in range (0,k):
                char += picture[i][j]
            str += char
        for y in range (0,k):
            answer.append(str)
    return answer