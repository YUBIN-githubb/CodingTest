def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    i = 0
    while m <= len(score) - i:
        answer += score[i+m-1] * m
        i += m
    return answer