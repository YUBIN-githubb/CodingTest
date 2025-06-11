def solution(x, n):
    answer = []
    diff = x
    for i in range (0,n):
        answer.append(x)
        x += diff
    return answer