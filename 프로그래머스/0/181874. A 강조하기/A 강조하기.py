def solution(myString):
    myString_list = [string for string in myString]
    for i in range (0,len(myString_list)):
        if myString_list[i] == "a":
            myString_list[i] = "A"
        else:
            if myString_list[i] != "A":
                if myString_list[i].isupper():
                    myString_list[i] = myString_list[i].lower()
    return "".join(myString_list)