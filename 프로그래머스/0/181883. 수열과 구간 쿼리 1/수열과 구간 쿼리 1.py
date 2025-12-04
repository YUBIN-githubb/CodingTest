def solution(arr, queries):
    for i in range (0,len(queries)):
        for j in range (queries[i][0], queries[i][1]+1):
            arr[j] += 1
    return arr