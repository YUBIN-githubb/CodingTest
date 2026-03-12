def solution(n, lost, reserve):
    dic = {}
    reserve.sort()
    
    for i in range (1,n+1):
        if i in lost and i in reserve:
            dic[str(i)] = 1
            continue
            
        if i not in lost and i not in reserve:
            dic[str(i)] = 1
            continue
        
        if i in lost:
            dic[str(i)] = 0
            continue
            
        if i in reserve:
            dic[str(i)] = 2
            continue
                        
    for i in range(0,len(reserve)):
        if dic[str(reserve[i])] == 1:
            continue
            
        if dic.get(str(reserve[i]-1),"none") == 0:
            dic[str(reserve[i])] -= 1
            dic[str(reserve[i]-1)] += 1
            continue
        
        if dic.get(str(reserve[i]+1),"none") == 0:
            dic[str(reserve[i])] -= 1
            dic[str(reserve[i]+1)] += 1
            continue

            
    answer = list(filter(lambda x : dic[x] >= 1, dic))
    return len(answer)
        
    
                
                
                
            