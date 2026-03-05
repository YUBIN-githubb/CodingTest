def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for i in range (0,len(babbling)):
        for w in word:
            if w*2 in babbling[i]:
                continue
            if w in babbling[i]:
                babbling[i] = babbling[i].replace(w," ")
        if babbling[i] == len(babbling[i])*" ":
            answer += 1
    return answer
                