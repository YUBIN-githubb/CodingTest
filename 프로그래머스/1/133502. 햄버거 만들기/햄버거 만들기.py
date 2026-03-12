def solution(ingredient):
    answer = 0
    hamburger = []
    for i in range (0,len(ingredient)):
        hamburger.append(ingredient[i])
        if len(hamburger) >= 4:
            if hamburger[-1] == 1 and hamburger[-2] == 3 and hamburger[-3] == 2 and hamburger[-4] == 1:
                answer += 1
                hamburger.pop()
                hamburger.pop()
                hamburger.pop()
                hamburger.pop()
    return answer
    
    