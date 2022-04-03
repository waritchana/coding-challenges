from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] = digits[-1]+1
        return digits
    elif digits[-1] == 9 and len(digits) == 1:
            return [1, 0]
    elif digits[-1] == 9 and len(digits) > 1:
        original_digits_len = len(digits)
        digits[-1] = 0
        digits[-2] = digits[-2] + 1
        for i in range(original_digits_len-2, -1, -1):
            if digits[i] <= 9:
                return digits
            elif digits[i] > 9 and i-1 >= 0:
                digits[i] = 0
                digits[i-1] = digits[i-1] + 1
            elif digits[i] > 9 and i-1 < 0:
                digits[i] = 0
                digits.insert(0, 1)
        return digits


digits = [1,2,3] # Expect [1, 2, 4]
digits = [4,3,2,1] # Expect [4,3,2,2]
digits = [9, 9] # Expect [1, 0, 0]
output_digits = plusOne(digits)
print("Output is", output_digits)
