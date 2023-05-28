from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = True
            else:
                return True
        return False


nums = [1,2,3,1] # True
#nums = [1,2,3,4] # False
#nums = [1,1,1,3,3,4,3,2,4,2] # True
print(Solution().containsDuplicate(nums))
