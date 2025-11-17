def solution(my_string, s, e):
    toreverse = [string for string in my_string[s:e+1]]
    toreverse.reverse()
    return my_string[:s] + "".join(toreverse) + my_string[e+1:]