def lengthOfLastWord(s: str) -> int:
    word_len = 0
    if len(s) == 1 and s[0].isalnum():
        return 1
    for i in range(len(s)-1, -1, -1):
        if s[i].isalnum():
            word_len += 1
        elif word_len > 1:
            return word_len
    """
    count = 0
    if len(s) == 1 and s[0] != ' ':
        return 1
    # Starting from the last index to index 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            count += 1
        # After getting last word's length and see space again
        if s[i] == ' ' and count > 0:
            break
    return count
    """

s = "Hello World" # Expect 5
s = "   fly me   to   the moon  " # Expect 4
s = "luffy is still joyboy" # Expect 6
length = lengthOfLastWord(s)
print("Length of the last word is:", length)
