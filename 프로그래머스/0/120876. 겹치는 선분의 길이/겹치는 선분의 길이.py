def solution(lines):
    counts= [0] * 201
    result = 0
    for l in lines:
        for i in range (l[0],l[1]):            
            counts[i + 100] += 1
            
    for i in range(len(counts)):
        if counts[i] >= 2:
            result += 1
    
    return result
    