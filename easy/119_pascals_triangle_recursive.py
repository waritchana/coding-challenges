from typing import List


def getRow(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return [1]
    elif numRows == 1:
        return [1, 1]
    else:
        # Pre-created a row with all 1s
        row = [1] * (numRows+1)
        # Recursively gets previous row
        prev_row = getRow(numRows-1)
        # Only calculate value for middle blocks
        for i in range(1, numRows):
            row[i] = prev_row[i-1] + prev_row[i]
        return row


print(getRow(3))
print(getRow(1))
