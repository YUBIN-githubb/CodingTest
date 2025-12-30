def solution(l, r):
    answer = []
    for i in range (l,r+1):
        str_num = str(i)
        str_num = str_num.replace("5","")
        str_num = str_num.replace("0","")
        if str_num == "":
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer