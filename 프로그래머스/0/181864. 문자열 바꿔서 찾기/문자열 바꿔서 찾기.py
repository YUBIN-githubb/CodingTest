def solution(myString, pat):
    myStringList = []
    for string in myString:
        if(string == "A"):
            myStringList.append("B")
        else:
            myStringList.append("A")
    for i in range (0,len(myStringList)-len(pat)+1):
        result = "".join(myStringList[i:i+len(pat)])
        if(result == pat):
            return 1
    return 0