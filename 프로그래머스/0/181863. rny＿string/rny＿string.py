def solution(rny_string):
    rny_string_list = list(rny_string)
    for i in range (0,len(rny_string_list)):
        if rny_string_list[i] == "m":
            rny_string_list[i] = "rn"
    return "".join(rny_string_list)
            