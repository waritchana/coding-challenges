class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = x
        for i in range(1, n):
            result *= x
        return result


print("Result of power of n is", Solution().myPow(2.00000, 10))
