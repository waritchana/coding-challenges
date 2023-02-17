def romanToInt_1(s: str) -> int:
    # Runtime: 131 ms, faster than 5.15% of Python3 online submissions for Roman to Integer.
    # Memory Usage: 14.4 MB, less than 28.14% of Python3 online submissions for Roman to Integer.
    result = 0
    index = len(s) - 1
    while index >= 0:
        if s[index] == 'I':
            result += 1
            index -= 1
        elif s[index] == 'V' and s[index-1] == 'I' and index-1 >= 0:
            result += 4
            index -= 2
        elif s[index] == 'V':
            result += 5
            index -= 1
        elif s[index] == 'X' and s[index-1] == 'I' and index-1 >= 0:
            result += 9
            index -= 2
        elif s[index] == 'X':
            result += 10
            index -= 1
        elif s[index] == 'L' and s[index-1] == 'X' and index-1 >= 0:
            result += 40
            index -= 2
        elif s[index] == 'L':
            result += 50
            index -= 1
        elif s[index] == 'C' and s[index-1] == 'X' and index-1 >= 0:
            result += 90
            index -= 2
        elif s[index] == 'C':
            result += 100
            index -= 1
        elif s[index] == 'D' and s[index-1] == 'C' and index-1 >= 0:
            result += 400
            index -= 2
        elif s[index] == 'D':
            result += 500
            index -= 1
        elif s[index] == 'M' and s[index-1] == 'C' and index-1 >= 0:
            result += 900
            index -= 2
        elif s[index] == 'M':
            result += 1000
            index -= 1
    return result


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
