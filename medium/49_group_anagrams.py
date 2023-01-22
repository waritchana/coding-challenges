from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Strategy 1 - use sorted string as a key, its value is the
        # original string
        hashmap = {}
        for string in strs:
            sorted_string_tuple = tuple(sorted(string))
            if sorted_string_tuple in hashmap.keys():
                hashmap[sorted_string_tuple].append(string)
            else:
                hashmap[sorted_string_tuple] = [string]
        return hashmap.values()
        """
        # Strategy 2 - use tuple of character counts as a key, its value is
        # the original string
        hashmap = {}
        for string in strs:
            key = [0] * 26 # count how many times the character shows up
            for character in string:
                # The difference is the position of index in the list
                # eg. ord('d') - ord('a') is 3
                key[ord(character)-ord('a')] += 1
            if tuple(key) in hashmap.keys():
                hashmap[tuple(key)].append(string)
            else:
                hashmap[tuple(key)] = [string]
        return hashmap.values()
        """


#strs = ["a"]
#strs = [""]
strs = ["eat","tea","tan","ate","nat","bat"]
result = Solution().groupAnagrams(strs)
print("Group anagrams are", result)
