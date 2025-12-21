def solution(arr, k):
    answer = []
    answer.append(arr[0])
    for i in range (1,len(arr)):
        if answer.count(arr[i]) == 0:
            answer.append(arr[i])
    if len(answer) == k:
        return answer
    elif len(answer) > k:
        return answer[:k]
    else:
        add = k - len(answer)
        for i in range (0,add):
            answer.append(-1)
        return answer