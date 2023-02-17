class Solution:
    def fastPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        else:
            # Using fast pow method where x^n is (x^n/2) + (x^n/2)

            # Note that n/2 has to be controlled as int,
            # n will not fall into 0 condition and runs indinitely otherwise

            # Given A (half_result) is x^n/2
            # N is even; x^n = A * A
            # N is odd; x^n = A * A * x
            half_result = float(self.fastPow(x, int(n/2)))
            if (n % 2 == 0):
                return float(half_result * half_result)
            else:
                return float(half_result * half_result * x)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            # Move x to be divider
            x = 1/x
            # n is now positive
            n *= -1
        return self.fastPow(x, n)


print("Result of power of n is", Solution().myPow(2.00000, 10))
