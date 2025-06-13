def solution(seoul):
    for string in seoul:
        if string == "Kim":
            return f"김서방은 {seoul.index(string)}에 있다"