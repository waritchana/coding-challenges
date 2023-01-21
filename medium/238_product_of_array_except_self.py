from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        # Create a prefix list, the multiplication result from the beginning
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])

        # Create a postfix list, the multiplication result from the end
        postfix = [nums[-1]]
        for i in range(1, len(nums)):
            postfix.insert(0, postfix[len(postfix)-i] * nums[len(nums)-i-1])

        result = []
        # Final result is the prefix * postfix
        for i in range(0, len(nums)):
            if i == 0:
                result.append(postfix[i+1])
            elif i == len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*postfix[i+1])
        return result
        """
        # Create a prefix list, the multiplication result from the beginning
        # to itself. Named this list as result to be used in all calculations
        # to save memory
        result = [1]
        for i in range(1, len(nums)):
            result.append(result[i-1] * nums[i-1])

        # Working from the end of the list, multiply prefix multiplication result
        # with the postfix multiplication result
        current_postfix = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            else:
                result[i] *= current_postfix
                current_postfix *= nums[i]
        return result


nums = [1,2,3,4]
#expected_output = [24,12,8,6]
#nums = [-1,1,0,-3,3]
#expected_output = [0,0,9,0,0]
result = Solution().productExceptSelf(nums)
