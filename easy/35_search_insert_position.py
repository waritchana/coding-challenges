from math import ceil
from typing import List

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
    # Return where to add the number AFTER xth index
    return first_index

print(searchInsert([1,3], 1)) # expect 0
print(searchInsert([1,3,5,6], 5)) # expect 2
print(searchInsert([1,3,5,6], 2)) # expect 1
print(searchInsert([1,3,5,6], 7)) # expect 4
