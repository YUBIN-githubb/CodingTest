def solution(n):
    answer = []
    for i in range (0,n):
        stack = []
        for j in range (0,n):
            if i == j:
                stack.append(1)
            else:
                stack.append(0)
        answer.append(stack)
    return answer