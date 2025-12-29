def solution(arr):
    col = len(arr[0])
    row = len(arr)
    if row > col:
        diff = row - col
        for i in range (0,len(arr)):
            for j in range (0,diff):
                arr[i].append(0)
    elif row < col:
        diff = col - row
        for i in range (0,diff):
            arr.append([0]*col)
    else:
        return arr
    return arr
            