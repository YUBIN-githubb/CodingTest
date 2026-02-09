def solution(s):
    answer = []
    word = []
    for i in range (0,len(s)):
        if s[i] not in word:
            word.append(s[i])
            answer.append(-1)
        else:
            index = []
            for j in range (0,len(word)):
                if word[j] == s[i]:
                    index.append(j)
            m = max(index)
            answer.append(i-m)
            word.append(s[i])
    return answer