from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for item in strs:
            # eg. "5#Hello5#World"
            encoded += str(len(item)) + "#" + item
        return encoded


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        index_s = 0
        decoded = []
        while index_s < len(s):
            index_num = index_s
            # Find out how long is the string by getting a number
            # comes before #, and a number can be more than one digit
            while s[index_num] != "#":
                index_num += 1
            # eg. "5#Hello5#World" index num would be 1, 8
            # [0:1] [7:8]
            length_item = int(str(s[index_s:index_num]))
            # +1 to indexes to skip # added
            decoded.append(s[index_num+1:index_num+1+length_item])
            index_s = index_num + 1 + length_item
        return decoded

strs = ["Hello","World"]
codec = Codec()
print("Result of encode is", codec.encode(strs))
print("Result of encode -> decode is", codec.decode(codec.encode(strs)))
