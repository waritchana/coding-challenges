def romanToInt(s: str) -> int:
    result = 0
    index = len(s) - 1
    while index >= 0:
        if s[index] == 'I':
            result += 1
            index -= 1
        elif s[index] == 'V' and s[index-1] == 'I':
            result += 4
            index -= 2
        elif s[index] == 'V':
            result += 5
            index -= 1
        elif s[index] == 'X' and s[index-1] == 'I':
            result += 9
            index -= 2
        elif s[index] == 'X':
            result += 10
            index -= 1
        elif s[index] == 'L' and s[index-1] == 'X':
            result += 40
            index -= 2
        elif s[index] == 'L':
            result += 50
            index -= 1
        elif s[index] == 'C' and s[index-1] == 'X':
            result += 90
            index -= 2
        elif s[index] == 'C':
            result += 100
            index -= 1
        elif s[index] == 'D' and s[index-1] == 'C':
            result += 400
            index -= 2
        elif s[index] == 'D':
            result += 500
            index -= 1
        elif s[index] == 'M' and s[index-1] == 'C':
            result += 900
            index -= 2
        elif s[index] == 'M':
            result += 1000
            index -= 1
    return result

result = romanToInt('III')
print("Result is:", result)
result = romanToInt('LVIII')
print("Result is:", result)
result = romanToInt('MCMXCIV')
print("Result is:", result)
