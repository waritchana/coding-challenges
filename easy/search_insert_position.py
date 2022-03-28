from math import ceil
from typing import List


def findMiddle(first_index, last_index, nums):
    if len(nums[first_index:last_index+1]) % 2:
        return (first_index+(int((last_index-first_index)/2)))
    else:
        return (first_index+ceil((last_index-first_index)/2))


def searchInsert(nums: List[int], target: int) -> int:
    first_index = 0
    last_index = len(nums)-1
    while (last_index-first_index > 1):
        pointer = findMiddle(first_index, last_index, nums)
        if target == nums[pointer]:
            return pointer
        elif target < nums[pointer]:
            last_index = pointer
        elif target > nums[pointer]:
            first_index = pointer
    if target == nums[last_index]:
        return last_index
    elif target == nums[first_index]:
        return first_index
    elif target > nums[last_index]:
        return last_index+1
    elif target < nums[last_index] and target > nums[first_index]:
        return last_index
    elif target < nums[first_index]:
        if first_index == 0:
            return 0
        return first_index-1

"""
def searchInsert(nums: List[int], target: int) -> int:
    first_index = 0
    last_index = len(nums)-1
    while first_index <= last_index:
        pointer = int((first_index+last_index)/2)
        if target == nums[pointer]:
            return pointer
        elif target > nums[pointer]:
            first_index = pointer+1
        elif target < nums[pointer]:
            last_index = pointer-1
    return first_index
"""

print(searchInsert([1,3], 1)) # expect 0
print(searchInsert([1,3,5,6], 5)) # expect 2
print(searchInsert([1,3,5,6], 2)) # expect 3
print(searchInsert([1,3,5,6], 7)) # expect 4
