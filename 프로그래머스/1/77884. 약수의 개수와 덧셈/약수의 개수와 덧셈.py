def solution(left, right):
    answer = 0
    for i in range (left,right+1):
        y = []
        for j in range (1,i+1):
            if i%j == 0:
                if j not in y:
                    y.append(j)
        if len(y)%2 == 0:
            answer += i
        else:
            answer -= i
    return answer