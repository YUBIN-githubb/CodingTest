def solution(str_list, ex):
    return "".join([num for num in str_list if ex not in num])