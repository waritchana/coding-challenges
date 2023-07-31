class Solution:
    def isValidParentheses(self, s: str) -> bool:
        stack = []
        brakets_table = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for character in s:
            # If character is the close bracket
            # check last added character in the stack to match
            if character in brakets_table.keys():
                if stack and stack[-1] == brakets_table[character]:
                    stack.pop()
                else:
                    return False
            # Add open bracket to stack
            else:
                stack.append(character)
        # Return True if stack is empty cause all brackets are closed
        if not stack:
            return True


result = Solution().isValidParentheses("()")
print(result)
result = Solution().isValidParentheses("}(")
print(result)
result = Solution().isValidParentheses("()[]{}")
print(result)
result = Solution().isValidParentheses("(([]{}))")
print(result)
