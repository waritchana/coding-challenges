from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # Not recursive way
    # Only work on half of the string
    for i in range(0, len(s)//2):
        tmp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = tmp
    print(f"New string is {s}")


s = ["h","e","l","l","o"]
reverseString(s)
