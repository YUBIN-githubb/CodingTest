def solution(arr):
    while True:
        if len(arr) == 0:
            return [-1]
        else:
            if arr[-1] == 2:
                break
            else:
                arr.pop()
    while True:
        if len(arr) == 0:
            return [-1]
        else: 
            if arr[0] == 2:
                break
            else:
                arr.pop(0)
    return arr