def solution(my_string, is_suffix):
    for i in range (0,len(my_string)):
        sliced_string = my_string[i:]
        if (sliced_string == is_suffix):
            return 1
    return 0