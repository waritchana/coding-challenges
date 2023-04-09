class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        # Turn a number to string and fill 0 to meet set indexes
        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0
        # Use list instead of string as it provides better
        # time complexity when appending
        answer = []
        for i in range(n-1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")

            carry //= 2

        if carry == 1:
            answer.append("1")

        return ''.join(answer[::-1])

#a = "11", b = "1"
# Expected "100"

a = "1010"
b = "1011"
# Expected "10101"
Solution().addBinary(a, b)
