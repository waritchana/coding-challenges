from typing import List

def helper(start_index, end_index, s):
    if start_index >= end_index:
        return
    # Swap
    tmp = s[start_index]
    s[start_index] = s[end_index]
    s[end_index] = tmp
    # Move on to do next index
    helper(start_index+1, end_index-1, s)
    return s


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # Recursive way
    s = helper(0, len(s)-1, s)
    print(f"New string is {s}")


s = ["h","e","l","l","o"]
reverseString(s)
