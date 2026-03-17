def solution(X, Y):
    answer = []
    dic = {}
    for i in range (0,len(X)):
        if X[i] not in dic:
            dic[X[i]] = 1
        else:
            dic[X[i]] += 1
            
    for i in range (0,len(Y)):
        result = dic.get(Y[i],"none")
        if result != "none" and result > 0:
            answer.append(Y[i])
            dic[Y[i]] -= 1
    
    if len(answer) == 0:
        return "-1"
    else:
        if answer.count('0') == len(answer):
            return "0"
        else:
            answer.sort(reverse=True)
            return "".join(answer)
            