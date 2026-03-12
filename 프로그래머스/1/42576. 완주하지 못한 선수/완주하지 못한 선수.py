def solution(participant, completion):
    dict = {}
    for i in range (0,len(completion)):
        if completion[i] not in dict:
            dict[completion[i]] = 1
        else:
            dict[completion[i]] += 1
            
    for i in range (0,len(participant)):
        result = dict.get(participant[i],"none")
        if result == "none":
            return participant[i]
        else:
            if dict[participant[i]] >= 1:
                dict[participant[i]] -= 1
            else:
                return participant[i]
