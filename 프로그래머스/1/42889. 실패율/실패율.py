def solution(N, stages):
    answer = []
    for i in range (1,N+1):
        result = list(filter(lambda x : x>=i, stages))
        user = result.count(i)
        if len(result) > 0:
            ratio = user / len(result)
        else:
            ratio = 0
        answer.append((i,ratio))
    answer.sort(key=lambda x : x[1],reverse=True)
    return list(map(lambda x : x[0],answer))