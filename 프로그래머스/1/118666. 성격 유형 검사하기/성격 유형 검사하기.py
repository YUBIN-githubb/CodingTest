def solution(survey, choices):
    score = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
    }
    
    answer = {
        1 : 3,
        2 : 2,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 2,
        7 : 3
    }
    
    for i in range (0,len(choices)):
        if choices[i] < 4:
            score[survey[i][0]] += answer[choices[i]]
        else:
            score[survey[i][1]] += answer[choices[i]]
    
    answer = ""
    
    if score["R"] > score["T"]:
        answer += "R"
    elif score["R"] == score["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if score["C"] > score["F"]:
        answer += "C"
    elif score["C"] == score["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if score["J"] > score["M"]:
        answer += "J"
    elif score["J"] == score["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if score["A"] > score["N"]:
        answer += "A"
    elif score["A"] == score["N"]:
        answer += "A"
    else:
        answer += "N"
            
    
    return answer