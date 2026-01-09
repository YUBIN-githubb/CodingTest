def solution(n):
    result_3 = ""
    
    while n > 0:
        n,remain = divmod(n,3)
        result_3 = str(remain) + result_3
    
    result = list(result_3)
    result.reverse()
    result = "".join(result)
    result = int(result,3)
    print(result)
        
    return result