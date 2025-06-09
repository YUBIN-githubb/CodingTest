def solution(common):
    if len(common) == 2:
        if common[1] % common[0] == 0:
            return common[-1] * (common[1] // common[0])
        else:
            return common[-1] + (common[1] - common[0])
    else:
        if (common[2]-common[1]) == (common[1]-common[0]):
            return common[-1] + (common[1] - common[0])
        else:
            return common[-1] * (common[1] // common[0])
            
            
            
            
