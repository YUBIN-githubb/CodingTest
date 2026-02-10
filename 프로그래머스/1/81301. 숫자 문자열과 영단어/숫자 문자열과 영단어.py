def solution(s):
    numbers = [("zero","0"), ("one","1"), ("two","2"), ("three","3"), ("four","4"), ("five","5"), ("six","6"), ("seven","7"), ("eight","8") , ("nine","9")]
    for i in range (0,len(numbers)):
        if numbers[i][0] in s:
            s = s.replace(numbers[i][0], numbers[i][1])              
    return int(s)