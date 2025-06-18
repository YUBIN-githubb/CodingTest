def solution(n):
    answer = ""
    while True:
        if n == 0:
            break
        n -= 1
        if answer == "":
            answer += "수"
        elif answer[-1] == "박":
            answer += "수"
        elif answer[-1] == "수":
            answer += "박"
    return answer