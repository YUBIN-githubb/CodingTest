def solution(s):
    s = s.split(" ")
    result = []
    for j in range (len(s)):
        answer = ""
        for i in range (0,len(s[j])):
            if i%2 == 0:
                answer += s[j][i].upper()
            else:
                answer += s[j][i].lower()
        result.append(answer)
    return " ".join(result)
