def romanToInt(s: str) -> int:
    # Runtime: 67 ms, faster than 30.46% of Python3 online submissions for Roman to Integer.
    # Memory Usage: 14.1 MB, less than 84.05% of Python3 online submissions for Roman to Integer.
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    index = 0
    result = 0
    while index < len(s):
        # For the case like IV = 5 - 1 = 4
        if (
            index+1 <= len(s)-1 and
            roman_numbers[s[index]] < roman_numbers[s[index+1]]
        ):
            result += roman_numbers[s[index+1]] - roman_numbers[s[index]]
            index += 2
        else:
            result += roman_numbers[s[index]]
            index += 1
    return result

result = romanToInt('IV')
print("Result is:", result)
result = romanToInt('III')
print("Result is:", result)
result = romanToInt('LVIII')
print("Result is:", result)
result = romanToInt('MCMXCIV')
print("Result is:", result)
result = romanToInt('MMMCDXC')
print("Result is:", result)
