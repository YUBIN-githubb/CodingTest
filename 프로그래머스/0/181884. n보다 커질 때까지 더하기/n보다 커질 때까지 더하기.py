def solution(numbers, n):
    answer = 0
    for i in range(0,len(numbers)):
        if answer > n:
            return answer
        else:
            answer += numbers[i]
    if answer > n:
        return answer