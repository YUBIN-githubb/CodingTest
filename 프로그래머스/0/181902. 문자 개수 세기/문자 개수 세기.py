def solution(my_string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = []
    my_string_list = list(my_string)
    for str in alphabet:
        answer.append(my_string_list.count(str))
    return answer