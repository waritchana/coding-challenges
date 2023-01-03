class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) from length of s + t -> 2n -> n
        hashmap = {}
        if len(s) != len(t):
            return False
        for each in s:
            if each not in hashmap.keys():
                hashmap[each] = 1
            else:
                hashmap[each] += 1
        for each in t:
            if each not in hashmap.keys() or hashmap[each] == 0:
                return False
            else:
                hashmap[each] -= 1
        return True
        """
        O(nlogn) from the sorted function
        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False
        """


s = "anagram"
t = "nagaram"
#s = "rat", t = "car"
result = Solution().isAnagram(s, t)
print("Is it anagram? :", result)
