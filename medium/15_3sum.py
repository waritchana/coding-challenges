class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sort input list to only work with the same number(s) once
        # and work with two pointers.
        nums.sort()

        for i in range(len(nums)):
            # Skip if the current number is the same as previous number
            # since it had been worked on.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    """
                    * BOTH WAYS ARE CORRECT *
                    # Move on to next pointers, move both since each number can
                    # correspond to only one other number which was added.
                    # Keeps moving if the l number is the same
                    # as previous l, since it had been worked on.
                    l += 1
                    r -= 1
                    """
                    # Move one pointer (l) after the three numbers
                    # were found. Keeps moving if the l number is the same
                    # as previous l, since it had been worked on.
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result


"""
nums = [0,1,1]
expected_results = []

nums = [0,0,0]
expected_result = [[0,0,0]]
"""

nums = [-1,0,1,2,-1,-4]
#expected_results = [[-1,-1,2],[-1,0,1]]
result = Solution().threeSum(nums)
