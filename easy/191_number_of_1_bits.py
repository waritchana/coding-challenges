from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1
            # Shift to the right eg. 011 -> 01 -> 0
            n >>= 1
        return count
        """
        count = 0
        while n != 0:
            # n - 1 flips the least significant 1 to 0
            # keep flipping until all bits are 0
            n &= (n-1)
            count += 1
        return count


n = int('00000000000000000000000000001011', 2) # output = 3
#n = 00000000000000000000000010000000 # output = 1
#n = 11111111111111111111111111111101 # output = 31
output = Solution().hammingWeight(n)
print(f'Output is {output}')
