def solution(lottos, win_nums):
    dict = {
        "6" : 1,
        "5" : 2,
        "4" : 3,
        "3" : 4,
        "2" : 5,
        "1" : 6,
        "0" : 6
    }
    answer = []
    correct = 0
    zero_count = 0
    for i in range(0,len(lottos)):
        if lottos[i] in win_nums:
            correct += 1
        if lottos[i] == 0:
            zero_count += 1
    top = zero_count + correct
    answer.append(dict[str(top)])
    bottom = correct
    answer.append(dict[str(bottom)])
    
    return answer