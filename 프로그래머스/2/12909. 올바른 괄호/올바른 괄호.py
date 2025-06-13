def solution(s):
    stack = 0
    s = list(s)
    while s != []:
        if stack < 0:
            return False
        p = s.pop()
        if p ==  ")":
            stack += 1
        elif p == "(":
            stack -= 1
    if stack == 0:
        return True
    else:
        return False