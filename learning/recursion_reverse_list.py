def helper(first_index, last_index, s):
    if first_index >= last_index:
        return
    tmp = s[last_index]
    s[last_index] = s[first_index]
    s[first_index] = tmp
    helper(first_index+1, last_index-1, s)
    return s

def reverse_list(s):
    print(helper(0, len(s)-1, s))


s = ["W", "o", "r", "l", "d"]
reverse_list(s)
