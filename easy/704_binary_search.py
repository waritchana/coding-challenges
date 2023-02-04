from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        # = covers the case where there is one number in the list
        while (left <= right):
            medium = (left+right)//2
            if nums[medium] > target:
                right = medium-1
            elif nums[medium] < target:
                left = medium+1
            else:
                return medium
        return -1
