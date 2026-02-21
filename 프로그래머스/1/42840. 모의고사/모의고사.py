def solution(answers):
    result = [[1,0],[2,0],[3,0]]
    number1 = [1,2,3,4,5]
    number2 = [2, 1, 2, 3, 2, 4, 2, 5]
    number3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range (0,len(answers)):
        if answers[i] == number1[i%5]:
            result[0][1] += 1
        if answers[i] == number2[i%8]:
            result[1][1] += 1
        if answers[i] == number3[i%10]:
            result[2][1] += 1
            
    result.sort(key=lambda x : x[1])

    if result[2][1] == result[1][1] and result[1][1] == result[0][1]:
        return [result[0][0], result[1][0], result[2][0]]
    elif result[2][1] == result[1][1]:
        return [result[1][0], result[2][0]]
    else:
        return [result[2][0]]
        
    
