def solution(arr):
    stk = []
    for i in range (0,len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif len(stk) > 0:
            if stk[-1] == arr[i]:
                stk.pop(-1)
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
    if len(stk) == 0:
        return [-1]
    return stk