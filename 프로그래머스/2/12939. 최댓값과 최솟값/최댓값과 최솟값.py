def solution(s):
    num = list(s.split(" "))
    num_list = []
    for i in num:
        num_list.append(int(i))
    return f"{min(num_list)} {max(num_list)}"