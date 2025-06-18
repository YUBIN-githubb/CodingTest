def solution(a, b):
    s = 0
    for i in range (0,len(a)):
        s += a[i]*b[i]
    return s