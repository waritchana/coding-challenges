class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # "dog cat" = 7 -> split to ["dog", "cat"]
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_word_table = {}
        word_char_table = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char in char_word_table.keys():
                if char_word_table[char] != word:
                    return False
            else:
                char_word_table[char] = word
                # Avoid a case like "ab" returns True for "dog dog"
                if word not in word_char_table.keys():
                    word_char_table[word] = char
                else:
                    return False
        return True


pattern = "abba"
s = "dog cat cat dog" #True
#pattern = "abba", s = "dog cat cat fish" # False
#pattern = "aaaa", s = "dog cat cat dog" # False
Solution().wordPattern(pattern, s)
