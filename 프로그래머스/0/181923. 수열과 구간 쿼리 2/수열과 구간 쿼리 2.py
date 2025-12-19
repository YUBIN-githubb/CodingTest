def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        above_k = []
        for i in range (s,e+1):
            if arr[i] > k:
                above_k.append(arr[i])
        if len(above_k) > 0:
            answer.append(min(above_k))
        else:
            answer.append(-1)         
    return answer