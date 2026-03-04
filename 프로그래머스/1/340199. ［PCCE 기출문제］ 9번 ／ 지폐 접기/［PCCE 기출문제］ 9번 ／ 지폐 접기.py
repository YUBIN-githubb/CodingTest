def solution(wallet, bill):
    answer = 0
    if bill[0] < wallet[0] and bill[1] < wallet[1]:
        return answer
    else:
        while bill[0] > wallet[0] or bill[1] > wallet[1]:
            if bill[0] > bill[1]:
                bill[0] = bill[0]//2
                answer += 1
            else:
                bill[1] = bill[1]//2
                answer += 1
                
            if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
                break
            else:
                if bill[1] <= wallet[0] and bill[0] <= wallet[1]:
                    break
        
    
    return answer