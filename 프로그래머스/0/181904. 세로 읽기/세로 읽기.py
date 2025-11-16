def solution(my_string, m, c):
    answer = ''
    word_list = []
    for i in range(0,len(my_string),m):
        word = my_string[i:i+m]
        word_list.append(word)
    for word in word_list:
        answer += word[c-1]
    return answer