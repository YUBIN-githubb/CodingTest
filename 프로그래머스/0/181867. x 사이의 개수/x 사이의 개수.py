def solution(myString):
    split_myString = myString.split("x")
    return [len(string) for string in split_myString]