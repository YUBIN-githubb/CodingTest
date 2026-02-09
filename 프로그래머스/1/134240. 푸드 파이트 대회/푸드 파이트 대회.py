def solution(food):
    answer = ''
    for i in range (1,len(food)):
        m = food[i] // 2
        for _ in range (0,m):
            answer += f"{i}"
    rev = reversed(list(answer))
    return answer + "0" + "".join(rev)