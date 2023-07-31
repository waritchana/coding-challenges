from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The biggest value as for loop does not go to the last value
        # other numbers get add in the loop
        result = len(nums)
        for i in range(len(nums)):
            result += i
            result -= nums[i]
        return result


nums = [3,0,1] # 2
#nums = [0,1] # 2
#nums = [9,6,4,2,3,5,7,0,1] # 8
print(Solution().singleNumber(nums))
