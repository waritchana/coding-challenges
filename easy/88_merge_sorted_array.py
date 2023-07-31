from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Copy nums1 to copy_nums1 because nums1 will be modified later
        copy_nums1 = nums1[:]
        index1 = 0
        index2 = 0

        for i in range(m+n):
            # Add to nums1 when
            # 1. Exceeding nums2
            # 2. copy_nums1 number is smaller and not exceeding
            if (
                (index2 == n) or\
                (copy_nums1[index1] < nums2[index2] and index1 < m)
            ):
                nums1[i] = copy_nums1[index1]
                index1 += 1
            else:
                nums1[i] = nums2[index2]
                index2 += 1
        print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
