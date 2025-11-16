def solution(my_string):
    answer = []
    for i in range (0,len(my_string)):
        word = my_string[i:]
        answer.append(word)
    return sorted(answer)
        