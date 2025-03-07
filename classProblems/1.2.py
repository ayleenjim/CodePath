# take in a list nums
# 

def goldilocks_approved(nums):
    maxNum = max(nums)
    minNum = min(nums)
    #ans = -1
    for num in nums:
        if num == minNum or num == maxNum:
            continue
        else:
            return num
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))