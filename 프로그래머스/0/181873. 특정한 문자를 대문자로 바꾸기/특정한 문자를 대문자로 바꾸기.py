def solution(my_string, alp):
    my_string_list = []
    for str in my_string:
        if str == alp:
            my_string_list.append(str.upper())
        else:
            my_string_list.append(str)
    return "".join(my_string_list)