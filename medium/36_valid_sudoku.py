from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        # Sudoku matrix is always 9
        n = 9

        # Three lists we need to check whether the number has been seen
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]

        for row in range(n):
            for col in range(n):
                value = board[row][col]
                square_index = (row//3) * 3 + (col//3)
                if value == ".":
                    continue

                # Check in set() at its position in three lists
                if (value in rows[row] or
                    value in cols[col] or
                    value in squares[square_index]
                ):
                    return False
                # Add number to each lists
                # add to set() to avoid duplicating number
                rows[row].add(value)
                cols[col].add(value)
                squares[square_index].add(value)
        return True
        """
        # Sudoku matrix is always 9
        n = 9

        # Three lists we need to check whether the number has been seen
        rows = [[0] * n for _ in range(n)]
        cols = [[0] * n for _ in range(n)]
        squares = [[0] * n for _ in range(n)]

        for row in range(n):
            for col in range(n):
                value = board[row][col]
                square_index = (row//3) * 3 + (col//3)
                if value == ".":
                    continue

                list_index = int(value) - 1
                # Check in three lists
                if (rows[row][list_index] == 1 or
                    cols[row][list_index] == 1 or
                    squares[square_index][list_index] == 1
                ):
                    return False
                # Mark value as seen in each lists
                rows[row][list_index] = 1
                cols[row][list_index] = 1
                squares[square_index][list_index] = 1
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
expected_result = True
#board =
#[["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#expected_result = False
result = Solution().isValidSudoku(board)
print("Valid sudoku:", result)
