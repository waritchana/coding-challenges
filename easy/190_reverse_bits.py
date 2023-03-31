from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Get the bit value at the ith spot
            bit = (n >> i) & 1
            # Update the value at (31-i)th spot
            result = result | bit << (31-i)
        return result


n = int('00000010100101000001111010011100', 2)
#output = 964176192 (00111001011110000010100101000000)
#n = 11111111111111111111111111111101
#output = 3221225471 (10111111111111111111111111111111)
output = Solution().reverseBits(n)
print(f'Output is {output}')
