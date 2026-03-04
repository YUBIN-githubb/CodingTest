from itertools import combinations
def solution(nums):
    answer = 0
    
    for a,b,c in combinations(nums,3):
        num = a+b+c
        answer += 1
        for i in range (2,int(num**0.5)+1):
            if num%i == 0:
                answer -= 1
                break
    
    

    return answer