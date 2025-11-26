def solution(arr):
    while True:
        length = len(arr)
        if (length & (length-1)) != 0:
            arr.append(0)
        else:
            break
    return arr