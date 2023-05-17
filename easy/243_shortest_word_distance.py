from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # Set indexes to a value that represent they have not been set
        index1 = -1
        index2 = -1
        min_distance = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            elif wordsDict[i] == word2:
                index2 = i

            if (index1 > -1 and index2 > -1):
                min_distance = min(min_distance, abs(index1-index2))
                # Stop looking if distance is 1, cannot be lower
                if min_distance == 1:
                    break
        return min_distance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
"""
["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
"""
Solution().shortestDistance(wordsDict, word1, word2)
