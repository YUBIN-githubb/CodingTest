def solution(arr, flag):
    X = []
    for i in range (0,len(flag)):
        if flag[i] == True:
            for j in range (0,arr[i]*2):
                X.append(arr[i])
        else:
            for j in range (0,arr[i]):
                X.pop()
    return X
            