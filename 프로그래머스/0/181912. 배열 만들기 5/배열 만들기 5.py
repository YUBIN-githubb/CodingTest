def solution(intStrs, k, s, l):
    answer = []
    for i in range (0,len(intStrs)):
        sliced = intStrs[i][s:s+l]
        if int(sliced) > k:
            answer.append(int(sliced))
    return answer