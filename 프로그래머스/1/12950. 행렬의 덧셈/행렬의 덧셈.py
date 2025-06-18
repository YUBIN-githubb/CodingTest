def solution(arr1, arr2):
    answer = []
    for i in range (0,len(arr1)):
        row = []
        for j in range (0,len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer