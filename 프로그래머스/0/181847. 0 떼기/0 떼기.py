def solution(n_str):
    answer = []
    str_list = [str for str in n_str]
    for s in str_list:
        if s != "0":
            answer.append(s)
        else:
            if len(answer) > 0:
                answer.append(s)
    return "".join(answer)
                
        