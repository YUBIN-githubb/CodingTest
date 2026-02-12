def solution(cards1, cards2, goal):
    answer = ''
    for i in range (0,len(goal)):
        if goal[i] in cards1 and len(cards1) > 0:
            if goal[i] == cards1[0]:
                cards1.remove(goal[i])
                continue
        if goal[i] in cards2 and len(cards2) > 0:
            if goal[i] == cards2[0]:
                cards2.remove(goal[i])
                continue
        return "No"
    return "Yes"
                