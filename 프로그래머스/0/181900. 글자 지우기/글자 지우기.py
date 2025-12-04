def solution(my_string, indices):
    my_string_list = [str for str in my_string]
    for num in indices:
        my_string_list[num] = ""
    return "".join(my_string_list)