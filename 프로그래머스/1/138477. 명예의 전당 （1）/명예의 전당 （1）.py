def solution(k, score):
    answer = []
    k_array = []
    for i in range (0,len(score)):
        k_array.append(score[i])
        if len(k_array) > k:
            k_array.sort(reverse=True)
            k_array = k_array[:k]
            answer.append(min(k_array))
        else:
            answer.append(min(k_array))
        
        
            
    return answer