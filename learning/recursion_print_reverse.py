"""
def helper(index, s):
    # Base case is when it has reached the end of the string
    if len(s) == 0 or index == len(s):
        return
    helper(index+1, s)
    # Start printing when base case has met and back
    print(s[index])

def print_reverse(s):
    helper(0, s)

print_reverse("ABCDEFG")
"""

def helper(index, s):
    if len(s) == 0 or index == len(s):
        return
    print(index)
    helper(index+1, s)
    print(s[index])



def print_reverse(s):
    helper(0, s)

print_reverse("ABCDEFG")
