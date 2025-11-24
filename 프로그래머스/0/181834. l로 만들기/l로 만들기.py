def solution(myString):
    myString_list = [string for string in myString]
    for i in range (0,len(myString_list)):
        if myString_list[i] < "l":
            myString_list[i] = "l"
    return "".join(myString_list)