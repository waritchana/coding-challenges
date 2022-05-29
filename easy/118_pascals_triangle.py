from typing import List


def generate(numRows: int) -> List[List[int]]:
    result = []
    for numRow in range(1, numRows+1):
        row_values = []
        for numCol in range(0, numRow):
            # Numbers on the edge are one
            if numCol == 0 or numCol == (numRow-1):
                row_values.append(1)
            # Numbers in the middle are the sum of
            # the two numbers directly above it
            else:
                row_values.append(
                    result[numRow-2][numCol-1]+result[numRow-2][numCol]
                )
        result.append(row_values)
    return result


print(generate(5))
print(generate(1))
