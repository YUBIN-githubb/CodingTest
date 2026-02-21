def solution(number, limit, power):
    result = []
    
    for i in range (1,number+1):
        count = 0
        for j in range (1,int(i**0.5)+1):
            if i%j == 0:
                if j**2 == i:
                    count += 1
                else:
                    count += 2
        result.append(count)
    
    for i in range (0,len(result)):
        if result[i] > limit:
            result[i] = power
    
    return sum(result)
                