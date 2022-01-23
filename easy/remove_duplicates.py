from typing import List


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

print(removeDuplicates([1,1,2]))
