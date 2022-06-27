class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Straightforward way works for small n,
        # time limit exceeds when n is 30 and k is 434991989
        # digits are 2^29
        """
        current_value = ''
        for i in range(1, n+1):
            if i == 1:
                current_value = '0'
            else:
                current_value = ''
                for char in prev_value:
                    if char == '0':
                        current_value += '01'
                    elif char == '1':
                        current_value += '10'
            print("row {}: {}".format(i, current_value))
            prev_value = current_value
        return current_value[k-1]
        """
        # Get the length of the final string,
        # which is the same as binary tree 2^n-1
        length = pow(2, n-1)
        # Have half of the full length to compare
        # whether K goes to left or right
        half_length = length/2
        # Value starts from zero, changes as being traversing
        is_zero = True

        # Only traverse the tree if n is more than 1
        # And starts from row 2
        if n > 1:
            for i in range(2, n+1):
                if k > half_length:
                    is_zero = not is_zero
                    k -= half_length
                half_length /= 2

        if is_zero:
            return 0
        else:
            return 1


print("kth of row nth is", Solution().kthGrammar(1, 1))
print("kth of row nth is", Solution().kthGrammar(2, 1))
print("kth of row nth is", Solution().kthGrammar(2, 2))
print("kth of row nth is", Solution().kthGrammar(3, 3))
