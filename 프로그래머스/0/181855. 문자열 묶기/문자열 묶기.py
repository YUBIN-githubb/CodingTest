from collections import Counter
def solution(strArr):
    answer = 0
    for i in range (0, len(strArr)):
        strArr[i] = len(strArr[i])
    count = Counter(strArr)
    for k, v in count.items():
        if v > answer:
            answer = v
    return answer
    
    