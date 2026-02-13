def solution(n, arr1, arr2):
    answer = []
    result = []
    
    for i in range (0,len(arr1)):
        arr1[i] = format(arr1[i],'b')
    for i in range (0,len(arr1)):
        if len(arr1[i]) < n:
            count = n - len(arr1[i])
            for j in range (0,count):
                arr1[i] = "0" + arr1[i] 
    
    for i in range (0,len(arr2)):
        arr2[i] = format(arr2[i],'b')
    for i in range (0,len(arr2)):
        if len(arr2[i]) < n:
            count = n - len(arr2[i])
            for j in range (0,count):
                arr2[i] = "0" + arr2[i]
    
    for i in range (0,n):
        s = ""
        for j in range (0,len(arr1)):
            if arr1[i][j] == "0" and arr2[i][j] == "0":
                s += "0"
            elif arr1[i][j] == "1" or arr2[i][j] == "1":
                s += "1"
        answer.append(s)
    
    for i in range (0,len(answer)):
        s = ""
        for j in range (0,len(answer[i])):
            if answer[i][j] == "1":
                s += "#"
            elif answer[i][j] == "0":
                s += " "
        result.append(s)
          
                
    return result