def solution(absolutes, signs):
    num = []
    for i in range (0,len(absolutes)):
        if signs[i] == False:
            num.append(absolutes[i]*(-1))
        else:
            num.append(absolutes[i])
    return sum(num)