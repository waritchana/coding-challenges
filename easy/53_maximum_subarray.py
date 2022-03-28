from typing import List


def maxSubArray(nums: List[int]) -> int:
    sum_max_subarray = nums[0]
    sum_current_subarray = nums[0]
    # Start from second item
    for num in nums[1:]:
        # If sum of the previous item(s) and current value is higher,
        # extend the subarray
        # Otherwise, start over from the current item
        if sum_current_subarray+num >= num:
            sum_current_subarray += num
        else:
            sum_current_subarray = num
        # Compare the new subarray with saved max subarray
        # save the higer number
        if sum_current_subarray >= sum_max_subarray:
            sum_max_subarray = sum_current_subarray
    return sum_max_subarray


max_sum = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print("Max sum value is:", max_sum)

