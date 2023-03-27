from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """
    # Attempt 1
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
    """
    # Attempt 2
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            # Finish adding if value is not 9
            return digits
        elif digits[i] == 9:
            # Flip to 0 then go to the previous index to add one
            digits[i] = 0
        # For the case where string did not return because all digits are 9
    return [1] + digits


digits = [1,2,3] # Expect [1, 2, 4]
output_digits = plusOne(digits)
print("Output is", output_digits)
digits = [4,3,2,1] # Expect [4,3,2,2]
output_digits = plusOne(digits)
print("Output is", output_digits)
digits = [9, 9] # Expect [1, 0, 0]
output_digits = plusOne(digits)
print("Output is", output_digits)
