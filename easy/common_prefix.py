from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    shortest_str = min(strs, key=len)
    shortest_len = len(shortest_str)
    prefix = shortest_str[0]
    result = ''
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


common_prefix = longestCommonPrefix(["reflower","flow","flight"])
common_prefix = longestCommonPrefix(["",""])
print("Common prefix is", common_prefix)
common_prefix = longestCommonPrefix(["flower","flow","flight"])
print("Common prefix is", common_prefix)
common_prefix = longestCommonPrefix(["dog","racecar","car"])
print("Common prefix is", common_prefix)
