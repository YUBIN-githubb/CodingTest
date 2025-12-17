def solution(arr):
    answer_list = []
    answer_list.append(arr[0:])
    while True:
        for i in range(0,len(arr)):
            if (arr[i] >= 50) and ((arr[i]%2) == 0):
                arr[i] = arr[i]//2
            elif (arr[i] < 50) and ((arr[i]%2) != 0):
                arr[i] = arr[i]*2 + 1
        answer_list.append(arr[0:])
        if answer_list[-1] == answer_list[-2]:
            return len(answer_list) - 2