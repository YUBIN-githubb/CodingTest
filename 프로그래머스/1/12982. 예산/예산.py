def solution(d, budget):
    answer = 0
    d = sorted(d)
    for num in d:
        if num > budget:
            break
        else:
            budget = budget - num
            answer += 1
    return answer