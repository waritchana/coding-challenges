from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Get rid of duplicates to not be counted twice
        nums_set = set(nums)
        longest_len = 0
        for num in nums:
            # New sequence found when the number does not follow another number
            if (num - 1) not in nums_set:
                current_length = 0
                # Adding length until it's not continuously
                while num + current_length in nums_set:
                    current_length += 1
                longest_len = max(longest_len, current_length)
        return longest_len


nums = [100,4,200,1,3,2] # output = 4
result = Solution().longestConsecutive(nums)
print("Longest consecutive sequence is", result)

nums = [0,3,7,2,5,8,4,6,0,1] # output = 9
