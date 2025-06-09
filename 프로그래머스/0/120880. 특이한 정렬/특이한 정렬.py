def solution(numlist, n):
    numlist.sort(reverse=True)
    result = []
    while len(numlist) > 0:
        diff = []
        for num in numlist:
            diff.append(abs(n - num))
        result.append(numlist[diff.index(min(diff))])
        numlist.remove(numlist[diff.index(min(diff))])
    return result
    