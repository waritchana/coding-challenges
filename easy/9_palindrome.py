def isPalindrome(x: int) -> bool:
    # Not palindrome if it is a negative value and number divisible by 10
    # since first number cannot be 0
    if (x < 0) or (x % 10 == 0 and x != 0):
        return False
    second_half = 0
    # Stop when having second half exceeds and new x
    # then do the comparison
    while (x > second_half):
        # Create number backward
        # eg. original x = 24445, second_half = 5, 54, 544
        second_half = (second_half*10) + (x%10)
        # Remove last digit from original x at a time 
        x = int(x/10)

    # if x is odd, get rid of middle digit
    # by remove last digit of second_half
    return x == second_half or x == int(second_half/10)

if isPalindrome(10):
    print ("The number is a palindrome")
else:
    print ("The number is not a palindrome")
