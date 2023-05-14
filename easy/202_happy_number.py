class Solution:
    def get_next(self, n):
        sum = 0
        while n > 0:
            last_digit = n % 10
            sum += last_digit ** 2
            # Stop when running out of digit (n = 0)
            n = n // 10
        return sum

    def isHappy(self, n: int) -> bool:
        seen = set()
        # Stop where n = 1 (is happy)
        # or when seeing the same number again (infinity)
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1


n = 19
#n = 2
Solution().isHappy(n)
