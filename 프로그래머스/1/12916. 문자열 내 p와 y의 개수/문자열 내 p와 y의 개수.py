def solution(s):
    answer = True
    p = 0
    y = 0
    for string in s:
        if string == "P" or string == "p":
            p += 1
        elif string == "Y" or string == "y":
            y += 1
    if p == y:
        return answer
    else:
        answer = False
        return answer
            