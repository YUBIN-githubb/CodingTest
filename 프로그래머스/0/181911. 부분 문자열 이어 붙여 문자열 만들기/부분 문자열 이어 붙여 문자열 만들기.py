def solution(my_strings, parts):
    answer = ""
    for i in range (0,len(parts)):
        words = my_strings[i]
        answer += words[parts[i][0]:parts[i][1]+1]
    return answer
        