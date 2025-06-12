def solution(x):
    s = 0
    for i in list(str(x)):
        s += int(i)
    if x%s == 0:
        return True
    else:
        return False