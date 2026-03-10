import re
def solution(dartResult):
    answer = []
    dartResult = re.split(r'([SDT#*])',dartResult)
    for i in range (0,len(dartResult)):
        if dartResult[i].isdigit():
            answer.append(int(dartResult[i]))
        if dartResult[i] == "S":
            answer[-1] = answer[-1] ** 1
        if dartResult[i] == "D":
            answer[-1] = answer[-1] ** 2
        if dartResult[i] == "T":    
            answer[-1] = answer[-1] ** 3
        if dartResult[i] == "*":
            answer[-1] = answer[-1] * 2
            if len(answer) >= 2:
                answer[-2] = answer[-2] * 2
        if dartResult[i] == "#":
            answer[-1] = answer[-1] * (-1)
    
    return sum(answer)
                