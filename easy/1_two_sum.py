from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Bruce force going through each position and what comes after
        Time complexity: O(n^2)
        Space complexity: O(1)
        for i in range(len(nums)):
           for j in range(i+1, len(nums)):
                remain = target - nums[i]
                if nums[j] == remain:
                    return [i, j]
        """

        """
        Time complexity: O(n)
        Space complexity: O(n) as we store numbers in hash table
        """
        hashmap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain not in hashmap.keys():
                hashmap[nums[i]] = i
            else:
                return [hashmap[remain], i]


nums = [2,7,11,15]
target = 9
#nums = [3,2,4], target = 6
#nums = [3,3], target = 6
result = Solution().twoSum(nums, target)
print("Found two sum positions at", result)
