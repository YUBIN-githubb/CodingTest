from itertools import combinations

def solution(numbers):
    answer = []
    result = []
    for i in combinations (numbers,2):
        answer.append(i[0] + i[1])
    answer.sort()
    for i in range (0,len(answer)):
        if answer[i] not in result:
            result.append(answer[i])
    return result