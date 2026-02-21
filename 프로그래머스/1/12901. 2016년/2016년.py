def solution(a, b):
    month = [
        (1,31),
        (2,29),
        (3,31),
        (4,30),
        (5,31),
        (6,30),
        (7,31),
        (8,31),
        (9,30),
        (10,31),
        (11,30),
        (12,31)
    ]
    answer = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    days = 0
    for i in range (1, a):
        days += month[i-1][1]
    days += b
    
    if days%7 == 0:
        return "THU"
    else:
        return answer[(days%7)-1]