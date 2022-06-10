"""
# Recursion - time limit exceed when the number is big
class Solution:
    def decisionTree(self, i, n: int) -> int:
        # Return 0 - cannot reach the result
        # Return 1 - possible way to go
        if (i > n):
            return 0
        elif (i == n):
            return 1
        # Sum of ways to take combination of taking 1 step or 2 steps
        return self.decisionTree(i+1, n) + self.decisionTree(i+2, n)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            return self.decisionTree(0, n)
"""


# Recursion with Memoization
class Solution:
    def decisionTree(self, i, n, memo_steps: int) -> int:
        # Return 0 - cannot reach the result
        # Return 1 - possible way to go
        if (i > n):
            return 0
        elif (i == n):
            return 1
        elif (i in memo_steps):
            # If the number of ways has already calculated, reuse it
            return memo_steps[i]
        else:
            # Sum of ways to take combination of taking 1 step or 2 steps
            memo_steps[i] = self.decisionTree(i+1, n, memo_steps) +\
                self.decisionTree(i+2, n, memo_steps)
        return memo_steps[i]

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            memo_steps = {}
            return self.decisionTree(0, n, memo_steps)


n = 5
result = Solution().climbStairs(n)
print(f"There are {result} ways to climb the {n} stairs")
