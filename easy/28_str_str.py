# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack,
# or 0 when needle is an empty string.
def strStr(haystack: str, needle: str) -> int:
    needle_len = len(needle)
    if needle_len == 0:
        return 0
    # Does not need to go through all the characters, only enough that
    # contains needle.
    for i in range(len(haystack)-needle_len+1):
        if haystack[i:i+needle_len] == needle:
            return i
    return -1


haystack = "hello"
needle = "ll"
result = strStr(haystack, needle)
