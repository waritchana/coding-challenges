from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        # Time complexity: O(n)
        count_numbers = {}
        for num in nums:
            if num in count_numbers:
                count_numbers[num] += 1
            else:
                count_numbers[num] = 1

        for key, value in count_numbers.items():
            if value == 1:
                return key
        """
        number_to_xor = 0
        for num in nums:
            # Only unique bits will be the result
            # Bits get cancelled out (0) if appear twice
            number_to_xor ^= num
        return number_to_xor


#nums = [2,2,1] # 1
nums = [4,1,2,1,2] # 4
#nums = [1] # 1
print(Solution().singleNumber(nums))
