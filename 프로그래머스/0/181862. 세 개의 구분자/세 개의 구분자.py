def solution(myStr):
    answer = []
    queue = []
    for str in myStr:
        if str != "a" and str != "b" and str != "c":
            queue.append(str)
        else:
            if len(queue) > 0:
                answer.append("".join(queue))
                queue = []
    if len(queue) > 0:
        answer.append("".join(queue))
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer
    
            
    
            