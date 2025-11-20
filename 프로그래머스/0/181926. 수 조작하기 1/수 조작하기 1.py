def solution(n, control):
    for string in control:
        if string == "w":
            n += 1
        elif string == "s":
            n -= 1
        elif string == "d":
            n += 10
        elif string == "a":
            n -= 10
    return n