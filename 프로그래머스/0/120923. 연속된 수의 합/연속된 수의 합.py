def solution(num, total):
    for i in range (-(total+num),(total+num)+1):
        result = []
        for j in range (0,num):
            result.append(i+j)
        if sum(result) == total:
            return result