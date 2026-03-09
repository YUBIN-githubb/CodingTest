def solution(s):
    answer = 0
    x = ""
    same = 0
    diff = 0
    for i in range (0,len(s)):
        if same == 0 and diff == 0:
            x = s[i]
        
        if s[i] == x:
            same += 1
        else:
            diff += 1
            
        if same == diff:
            answer += 1
            same = 0
            diff = 0
            x = ""
    
    if x != "":
        answer += 1
        
    return answer
        