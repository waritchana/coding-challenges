def lengthOfLastWord(s: str) -> int:
    count = 0
    found = False
    if len(s) == 1 and s[0] != ' ':
        return 1
    # Starting from the last index to index 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            count += 1
            found = True
        # After getting last word's length and see space again
        if s[i] == ' ' and found:
            break
    return count


s = "Hello World" # Expect 5
s = "   fly me   to   the moon  " # Expect 4
s = "luffy is still joyboy" # Expect 6
length = lengthOfLastWord(s)
print("Length of the last word is:", length)
