def solution(a, b, c, d):
    dice_list = [a,b,c,d]
    dictionary = {}
    for num in dice_list:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] += 1
    if len(dictionary) == 4:
        sorted_dict = sorted(list(dictionary.keys()))
        return sorted_dict[0]
    elif len(dictionary) == 3:
        answer = 1
        for k,v in dictionary.items():
            if v == 1:
                answer *= k
        return answer
    elif len(dictionary) == 2:
        value_list = [v for k,v in dictionary.items()]
        if 2 in value_list:
            list_dict = [k for k,v in dictionary.items()]
            return (list_dict[0] + list_dict[1]) * abs(list_dict[0] - list_dict[1])
        else:
            p = 0
            q = 0
            for k,v in dictionary.items():
                if v == 3:
                    p = k
                else:
                    q = k
            return (10*p+q)**2
    elif len(dictionary) == 1:
        return 1111*a
        
        
            
                
            
    