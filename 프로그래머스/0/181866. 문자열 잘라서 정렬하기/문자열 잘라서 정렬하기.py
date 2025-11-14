def solution(myString):
    myString_split = myString.split("x")
    myString_split_removed = [string for string in myString_split if string != ""]
    return sorted(myString_split_removed)