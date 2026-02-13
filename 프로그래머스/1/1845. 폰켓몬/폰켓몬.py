def solution(nums):
    num = []
    for i in range (0,len(nums)):
        if nums[i] not in num:
            num.append(nums[i])
    if len(nums) // 2 < len(num):
        return len(nums) // 2
    elif len(nums) // 2 > len(num):
        return len(num)
    else:
        return len(num)
