def solution(n):
    answer = 0
    num = [True]*(n+1)
    num[0] = False
    num[1] = False
    for i in range (2,int(n**0.5)+1):
        if num[i] == True:
            for j in range (i*2,n+1,i):
                num[j] = False
    return num.count(True)