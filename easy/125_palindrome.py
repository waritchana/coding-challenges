class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        alnum_string = ""
        for char in s:
            # To generate a new string with only alphanumeric (alphabets or numbers)
            if char.isalnum():
                alnum_string += char.lower()
        # Compare alnum_string with its reversed
        return alnum_string == alnum_string[::-1]
        """
        i = 0
        j = len(s)-1
        while i < j:
            # Move pointers to the middle if not alnum
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # Compare two characters of alnum
            if s[i].lower() != s[j].lower():
                return False
            # Move on to the next positions
            i += 1
            j -= 1
        # Complete the string without finding unmatched characters
        return True


print(
    "Is the string palindrome:",
    Solution().isPalindrome("A man, a plan, a canal: Panama") # True
    #Solution().isPalindrome("A") # True
    #Solution().isPalindrome(" ") # True
    #Solution().isPalindrome("race a car") # False
)
