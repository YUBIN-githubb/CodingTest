def solution(n, m, section):
    answer = 1
    mask = section[0] + (m-1)
    for i in range (1,len(section)):
        if section[i] > mask:
            answer += 1
            mask = section[i] + (m-1)
            
        
    
    return answer