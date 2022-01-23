def isPalindrome(x: int) -> bool:
    if (x < 0 or (x % 10 == 0 and x != 0)):
        return False
    second_half = 0
    # when second_half becomes bigger,
    # it means we've gone through more than half
    while (x > second_half):
        # multiply the last digit by 10 and add the second last digit
        second_half = (second_half * 10) + (x % 10)
        # remove last digit to move on the closer digit to the middle 
        x = int(x/10)
        
    # if x is odd, we get rid of middle digit
    # by remove last digit of second_half
    return x == second_half or x == int(second_half/10) 

if isPalindrome(10):
    print ("The number is a palindrome")
else:
    print ("The number is not a palindrome")
