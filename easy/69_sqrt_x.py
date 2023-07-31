class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        # For x>=2. the square root is always smaller than x/2
        # and larger than 0 (0 and 1 has been taken care of)
        left = 2
        right = x//2
        while left <= right:
            mid = (left+right) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid-1
            elif mid*mid < x:
                left = mid+1
        # out of loop when right < left,
        # means right is the closest integer
        return right


print(Solution().mySqrt(4)) # return 2
#print(Solution().mySqrt(8)) # return 2 rounded down from 2.82842..
