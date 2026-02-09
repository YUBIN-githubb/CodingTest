def solution(s, n):
    answer = ''
    for i in range (0,len(s)):
        if s[i] != " ":
            if s[i].isupper():
                temp = ord(s[i]) + n
                if temp < 90:
                    answer += chr(temp % 90)
                elif temp == 90:
                    answer += "Z"
                elif temp > 90:
                    answer += chr((temp % 90) + 64)
            else:
                temp = ord(s[i]) + n
                if temp < 122:
                    answer += chr(temp % 122)
                elif temp == 122:
                    answer += "z"
                elif temp > 122:
                    answer += chr((temp % 122) + 96)      
        else:
            answer += " "
                
                
    return answer