def isValidParentheses(s: str) -> bool:
    # Empty list act like stack
    stack = []
    brackets_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    if len(s) <= 1:
        return False
    for c in s:
        # Adds open bracket to the top of the stack
        if c in brackets_map.values():
            stack.append(c)
        # Close bracket
        else:
            # See if the top of the stack has its open bracket
            if len(stack) > 0 and brackets_map[c] == stack.pop():
                continue
            # No matching open brackets available
            else:
                return False
    # All brackets have their matches, stack is empty
    if len(stack) == 0:
        return True

result = isValidParentheses("()")
print(result)
result = isValidParentheses("}(")
print(result)
result = isValidParentheses("()[]{}")
print(result)
result = isValidParentheses("(([]{}))")
print(result)
