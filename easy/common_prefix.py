from typing import List


"""
# This method is to find common prefix at any indexes in the string
def longestCommonPrefix(strs: List[str]) -> str:
    shortest_str = min(strs, key=len)
    shortest_len = len(shortest_str)
    prefix = shortest_str[0]
    result = ""
    for index in range(shortest_len):
        count_found = 0
        for s in strs:
            if not prefix in s:
                break
            else:
                count_found += 1
        if count_found == len(strs):
            result = prefix
            prefix += shortest_str[index+1]
        elif index+1 < shortest_len:
            prefix = shortest_str[index+1]
    return result
"""
def longestCommonPrefix(strs: List[str]) -> str:
    shortest_str = min(strs, key=len)
    result = ''
    # Return empty string if any element in strs is empty
    # or strs is empty
    if "" in strs or strs == []:
        return result
    # Make first character of first string as prefix
    else:
        prefix = strs[0][0]

    # Only loop upto the shortest string's length
    for char_index in range(len(shortest_str)):
        for str_index in range(1, len(strs)):
            # Compare first string's prefix to the each string
            if strs[str_index][char_index] != strs[0][char_index]:
                return result

        # Update longest prefix after confirm matching in all strings
        result += strs[0][char_index]
        # Extend prefix to the next character to be compared next round
        if char_index+1 <= len(shortest_str)-1:
            prefix += strs[0][char_index+1]
    return result


common_prefix = longestCommonPrefix(["ab","a"])
print("Common prefix is", common_prefix)
common_prefix = longestCommonPrefix(["reflower","flow","flight"])
print("Common prefix is", common_prefix)
common_prefix = longestCommonPrefix(["",""])
print("Common prefix is", common_prefix)
common_prefix = longestCommonPrefix(["flower","flow","flight"])
print("Common prefix is", common_prefix)
common_prefix = longestCommonPrefix(["dog","racecar","car"])
print("Common prefix is", common_prefix)
