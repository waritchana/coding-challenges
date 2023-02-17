from typing import List


def removeElement(nums: List[int], val: int) -> int:
    replacing_index = 0
    for i in range(0, len(nums)):
        # Add numbers that are not val, use index to track
        # added index
        if nums[i] != val:
            nums[replacing_index] = nums[i]
            replacing_index += 1
    return replacing_index


nums = [0,1,2,2,3,0,4,2]
length = removeElement(nums, 2)
# Expect [0, 1, 3, 0, 4]
print(nums[0:length])
