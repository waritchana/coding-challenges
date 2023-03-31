from typing import List


class Solution:
    """
    def count_1(self, i: int) -> int:
        count = 0
        while i != 0:
            i &= i - 1
            count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.count_1(i))
        return ans
    """
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans

n = 2 # output = [0,1,1]
n = 5 # output = [0,1,1,2,1,2]
output = Solution().countBits(n)
print(f'Output is {output}')
