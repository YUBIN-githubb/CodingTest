def solution(num_list):
    _prod = 1
    for num in num_list:
        _prod *= num
    _sum = sum(num_list) ** 2
    if _prod < _sum:
        return 1
    else:
        return 0