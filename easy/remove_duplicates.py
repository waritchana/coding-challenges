from typing import List


"""
def removeDuplicates(nums: List[int]) -> int:
    unique_indexes = {}
    # Add unique number (key) to dict
    for index in range(len(nums)):
        if not nums[index] in unique_indexes.keys():
            unique_indexes[nums[index]] = index
    # Add each number (key) to the beginning of the list
    # while ignore the rest of the list
    count = 0
    for key, value in unique_indexes.items():
        nums[count] = key
        count += 1
    # Return number of unique numbers in the first partial of the list
    return len(unique_indexes.keys())
"""
def removeDuplicates(nums: List[int]) -> int:
    # First index is unique, starting from the second index
    new_len = 1
    for index in range(1, len(nums)):
        # Add number when it is not duplicate
        if nums[index-1] != nums[index]:
            nums[new_len] = nums[index]
            new_len += 1
    return new_len


print(removeDuplicates([1,1,2]))
